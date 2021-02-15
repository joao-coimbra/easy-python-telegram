import telegram
import logging
import os
from telegram_chat.keys import *
logging.basicConfig(
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO
  )
bot = telegram.Bot(
  token=TELEGRAM_TOKEN
  )

def sendMessage(text):
  bot.sendMessage(
    chat_id=CHAT_ID,
    text=text
    )
  
def sendImage(img, local=True):
  if local:
    bot.sendPhoto(
      chat_id=CHAT_ID,
      photo=open(f'{os.getcwd()}\\{img}', 'rb')
      )
  else:
    bot.sendPhoto(
      chat_id=CHAT_ID,
      photo=img
      )