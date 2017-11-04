import os
import telebot #telegram api
from flask import Flask, request
import requests #http (https://github.com/requests/requests)
from random import randint
import time
import datetime
import schedule

TOKEN = os.environ['PP_BOT_TOKEN']
URL = os.environ['PP_BOT_URL']
REPO = os.environ['PP_BOT_REPO']
SECRET = '/' + TOKEN

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
################################################################################################################

def job():
	def start(message):
		bot.send_message(256587040, 'тест')

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


#datetime.datetime.now().date()


#приветствие, id
@bot.message_handler(commands=['start', 'help'])
def start(message):
	bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '... Твой id: ' + str(message.from_user.id))
	bot.send_message(message.chat.id, 'Я буду напоминать тебе о важных датах!')
	

	
  
################################################################################################################	
@server.route(SECRET, methods=['POST'])
def get_message():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "POST", 200
       
@server.route("/")
def web_hook():
	bot.remove_webhook()
	bot.set_webhook(url=URL+SECRET)
	return "CONNECTED", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000)) 
