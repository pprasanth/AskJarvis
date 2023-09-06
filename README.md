# AIChatbot

[![Python 3.7.9](https://img.shields.io/badge/python-3.7.9-blue.svg)](https://www.python.org/downloads/release/python-379/)
[![MongoDB 7.0.1](https://img.shields.io/badge/mongodb-7.0.1-green.svg)](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-7.0.1.zip)

## Prequesties:
1. Install venv within the project folder ```python -m venv venv```
2. Activate venv by running command ```venv\Scripts\activate```
3. Install required dependencies from requirements.txt ```pip install -r ./requirements.txt```
4. Install moongodb from mongodb server and extract in the path or directly install msi folder

## MongoDB Manual setup
If you installing mongodb manually through zip file then, follow below steps
1. Download zip file from MondoDB server or above MongoDB version icon.
2. Extract to the path and copy the ```mongodb-server-path/bin``` to the env path variable and restart the command prompt
3. Create a MongoDB folder somewhere safer and can be accessible thru dbpath settings.

Now MongoDB setup done manually.

To start mongodb, open command line and run ```mongod -dbpath path-to\mongodb-folder```

## Run the application

1. Activate venv by running command ```venv\Scripts\activate```
2. ```(venv) c:\\path-to-AIChatbot\: py main.py```