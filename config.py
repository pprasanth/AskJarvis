import os

# Each Flask web application contains a secret key which used to sign session cookies for protection against cookie data tampering.
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
# In my case it is, "F:\DataScience_Ai\hobby_projects\mvc_project\src"
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode, that will refresh the page when you make changes.
DEBUG = True

# Connect to the database
STORAGE_ADAPTER = 'chatterbot.storage.MongoDatabaseAdapter'
MONGO_URI = 'mongodb://localhost:27017/chatterbot'

PASSWORD_MD5_HASH = 'MAC188'

SESSION_TYPE = "mongodb"
SESSION_PERMANENT = True
PERMANENT_SESSION_LIFETIME = 1800
SESSION_COOKIE_MAX_AGE = 1800
SESSION_USE_SIGNER = True
SECRET_KEY = "ASK_JARVIS_MAC188"
