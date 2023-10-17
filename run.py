from app import app

from routes.blueprint import blueprint
from routes.admin_blueprint import admin_blueprint

# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)