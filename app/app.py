from flask import Flask
from flask_pymongo import PyMongo
from flask_session import Session
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)  # flask app object
app.config.from_object('config')  # Configuring from Python Files
mongo = PyMongo(app)

ask_jarvis = ChatBot(
        'AskJarvis',
        storage_adapter=app.config['STORAGE_ADAPTER'],
        database_uri=app.config['MONGO_URI']
    )

trainer = ChatterBotCorpusTrainer(ask_jarvis)
# trainer.train('chatterbot.corpus.english')
trainer.train('nlpdata.english')

Session(app)

# Specify the template folder location
app.template_folder = '../templates'  # Assuming 'templates' is located one level above the 'app' module


# Specify the static folder location
app.static_folder = '../static'  # Assuming 'static' is located one level above the 'app' module

