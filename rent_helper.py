import time
import logging
from requests import Session
from utils import read_json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class RentHelper(Session):
    def __init__(self):
        super().__init__()
        self.config = read_json("config.json")
        self.url = self.config["url"]
        self.filters = self.config["filter"]
        self.params = self.config["params"]
        self.result = self.run()

    def get_datalist(self, param: dict) -> dict:
        resp = super().get(url=self.url, params=param).json()
        if resp["code"] == 0 and resp["msg"] == "success":
            return resp["data"]["dataList"]
        assert False, f"get data from {self.url} failed! code={resp['code']}, msg={resp['msg']}"

    def run(self) -> dict:
        result = {}
        for param in self.params:
            datalist = self.get_datalist(param=param)
            log.info(f"origin data : {datalist}")
            for data in datalist:
                # time style 2022-08-07 22:59:41
                # within 8 hours
                # if abs(time.mktime(time.strptime(data["pub_time"], '%Y-%m-%d %H:%M:%S')) - time.time()) < 29000:
                if len(self.filters) > 0:
                    for f in self.filters:
                        if f in data["title"]:
                            result[data["url"]] = data["title"]
                else:
                    result[data["url"]] = data["title"]
        return result


