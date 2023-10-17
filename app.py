from flask import Flask
# from flask_migrate import Migrate
from routes.blueprint import blueprint
from routes.admin_blueprint import admin_blueprint

def create_app():
    app = Flask(__name__)  # flask app object
    return app

app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/')
app.register_blueprint(admin_blueprint, url_prefix='/admin')
# migrate = Migrate(app)  # Initializing the migration

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)