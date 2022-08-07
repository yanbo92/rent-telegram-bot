import time
from requests import Session
from utils import read_json


class RentHelper(Session):
    def __init__(self):
        super().__init__()
        self.config = read_json("config.json")
        self.url = self.config["url"]
        self.params = self.config["params"]
        self.result = self.run()

    def run(self) -> dict:
        result = {}
        for param in self.params:
            datalist = self.get_datalist(param=param)
            for data in datalist:
                # time style 2022-08-07 22:59:41
                if time.mktime(time.strptime(data["pub_time"], '%Y-%m-%d %H:%M:%S')) - time.time() < 86400:
                    result[data["url"]] = data["title"]
        return result

    def get_datalist(self, param: dict) -> dict:
        resp = super().get(url=self.url, params=param).json()
        if resp["code"] == 0 and resp["msg"] == "success":
            return resp["data"]["dataList"]
        assert False, f"get data from {self.url} failed! code={resp['code']}, msg={resp['msg']}"


if __name__ == '__main__':
    print(RentHelper().result)

