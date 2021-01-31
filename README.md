# TelegramGlutenFreeRecipesBot

A simple telegram bot that sends gluten free recipes to anyone that asks.

Telegram Bots are the new calculator in coding projects, so here you have my try, a simple telegram bot that returns a random gluten free recipe.


For this little project I used Telebot a simple, but extensible Python implementation for the Telegram Bot API. Also since my goal was to practice API calls, I used Spoonacular a food API that helps you to find thousand of recipes, basically you can get all kind of data from recipes and of course the module Requests.

In this case I made it simple, as mentioned before my goal was to create a simple bot that sends you a gluten free recipe every time you ask for it. For this I followed this steps:

1) Talked to BotFather (I know I know, best name ever) to create the bot with the token of telegram included.

2) Installed Telebot and Flask

3) Declared a couple of functions with decorators, the first one define what happens when you send the comand /start or /help to the bot.


4) The second function is the hearth of the bot, whenever you send a random message to the bot, the magic begins, the function get the message as a parameter, then we make a request to the API and get a random gluten free recipe, the result data is formated and saved in a variable we later use in the message we want to send, once we have the message the rest is simple, we just tell to the bot that he should reply to the message you sent with the recipe and photo!

5) I added a simple very very simple command to the function, if for some reason you write hello to the bot, he will say hello back, lol.

6) For the deployment I needed to use webhooks so I used Flask to do the rounting and heroku as server and voila! It's alive, my little Frankenstein is alive!!! 


If you use telegram, give it a try in here. https://t.me/GlutenFreeRecipesBot

That's all for today Folks!  

For more info you can contact me in: www.jesusramonp.com
