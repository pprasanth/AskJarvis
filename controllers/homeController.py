from flask import render_template, request
from chatterbot import ChatBot
from app import app

class HomeController():
    def home():
        return render_template("home.html")
    
    def ask_jarvis():
        english_bot = ChatBot(
            'AskJarvis',
            storage_adapter=app.config['STORAGE_ADAPTER'],
            database_uri=app.config['MONGO_URI']
        )
        userText = request.args.get('msg')
        return str(english_bot.get_response(userText))
