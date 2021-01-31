

import telebot
import requests
import os
import json
from flask import Flask, request

TOKEN = "##########" #Replace with your bot token
tb = telebot.TeleBot(TOKEN)
server = Flask(__name__)

#Bot, We'll use decorators and a basic use of the telebot api

@tb.message_handler(commands=['start'])
def send_info(message):
   text = (
   "<b>Welcome to GlutenFreeRecipes Bot 🤖🌱!</b>\n\n"
   "Say Hello to the bot to get a reply from it!\n\n"
   "If you want a recipe simply write <b>recipe<b>."
   )
   tb.send_message(message.chat.id, text, parse_mode='HTML')


@tb.message_handler(commands=['help'])
def send_welcome(message):
	tb.reply_to(message, "To use this bot simply send a message and it will return a gluten free recipe")

@tb.message_handler(func=lambda message: True)
def echo_all(message):
   name = message.from_user.first_name.capitalize() 
   if 'hello'in message.text.lower():
      tb.send_message(message.chat.id, 'Hello! ' + name + ', how are you doing today?')
   else:
      url = "https://api.spoonacular.com/recipes/random?apiKey=############&number=1&diet=Gluten%20Free."

      response = requests.get(url)

#A little function to formatted the string of the python JSON object
      def jprint(obj):
    # create a formatted string of the Python JSON object
         text = json.dumps(obj, sort_keys=True, indent=4)
         return text

#Saving in a varible the data we want to extract from the recipe

      tituloRecipe = jprint(response.json()["recipes"][0]["title"]).translate({ord('"'): None})
      urlRecipe = jprint(response.json()["recipes"][0]["sourceUrl"]).translate({ord('"'): None})
      photoRecipe = jprint(response.json()["recipes"][0]["image"]).translate({ord('"'): None})
       
      recipe_message = "Sure " + name +", here is your gluten-free recipe:\n\n" + "<b>Title: </b>" + tituloRecipe + "\n" + "<b>Link: </b>" + urlRecipe + "\n\n" + "<b>Enjoy!</b>"

      tb.send_message(message.chat.id,recipe_message, parse_mode='HTML', disable_web_page_preview=True)
      tb.send_photo(message.chat.id, photoRecipe)

# Server side with Flask
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
   tb.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "it works", 200

@server.route("/")
def webhook():
   tb.remove_webhook()
   tb.set_webhook(url='glutenfreebotv2.herokuapp.com/' + TOKEN)
   return "It Works!", 200

if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

tb.infinity_polling(True)