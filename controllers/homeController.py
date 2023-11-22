from flask import render_template, request
from chatterbot import ChatBot
from app import ask_jarvis

class HomeController():
    def home():
        return render_template("home.html")
    
    def ask_jarvis():
        userText = request.args.get('msg')
        return str(ask_jarvis.get_response(userText))
