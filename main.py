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


#тест
@bot.message_handler(commands=['inf'])
def inf(message):
	while True:
		bot.send_message(256587040, 'Я буду напоминать тебе о важных датах!')
		time.sleep(3600)  

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
