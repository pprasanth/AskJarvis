from flask import Blueprint
from controllers.homeController import home

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(home)