from flask import Blueprint
from controllers.homeController import HomeController

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(HomeController.home)
blueprint.route('/get', methods=['GET'])(HomeController.ask_jarvis)
