import time
import telegram


class TelegramSender:
    def __init__(self, token: str, chat_id: int, houses: dict):
        self.bot = telegram.Bot(token)
        self.houses = houses
        self.chat = chat_id
        self.run()

    def generate_markdown(self, house) -> str:
        return f"[{self.houses[house]}]({house})"

    def send_markdown(self, text, chat_id):
        self.bot.send_message(text=text, chat_id=chat_id, parse_mode="Markdown")

    def run(self):
        for house in self.houses.keys():
            self.send_markdown(text=self.generate_markdown(house), chat_id=self.chat)
            time.sleep(3)
