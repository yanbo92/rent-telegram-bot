import argparse
from rent_helper import RentHelper
from telegram_sender import TelegramSender

parser = argparse.ArgumentParser(description='Push some houses to your telegram')
parser.add_argument('--token', type=str, required=True, help='Your telagram bot token')
parser.add_argument('--chat', type=int, required=True, help='Your telegram chat id')
args = parser.parse_args()

TelegramSender(args.token, args.chat, RentHelper().result)
