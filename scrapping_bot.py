import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
import requests
from bs4 import BeautifulSoup
from os import getenv

token = getenv('token')

updater = Updater(
    token=token)

dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi human")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def medium_new(update, context):
    link = scrapping_medium()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=link)


start_handler = CommandHandler('getnew', medium_new)
dispatcher.add_handler(start_handler)

updater.start_polling()


def scrapping_medium():
    URL = 'https://medium.com/tag/programming'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    div_elements = soup.find(
        'div', {"class": "hk l"})

    for elements in div_elements:
        link = elements['href']

    return link
