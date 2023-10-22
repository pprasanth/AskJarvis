from flask import Blueprint
from controllers.adminAuthController import admin_login, admin_login_view, admin_logout
from controllers.dashboardController import dashboard
from controllers.jarvisController import JavisController
from controllers.scrapperController import ScrapperController

admin_blueprint = Blueprint('admin_blueprint', __name__)

admin_blueprint.route('/', methods=['GET'])(admin_login_view)
admin_blueprint.route('/login', methods=['POST'])(admin_login)
admin_blueprint.route('/logout', methods=['GET'])(admin_logout)
admin_blueprint.route('/dashboard', methods=['GET'])(dashboard)

admin_blueprint.route('/jarvis/list', methods=['GET'])(JavisController.list)
admin_blueprint.route('/jarvis/train', methods=['GET'])(JavisController.train_jarvis)
admin_blueprint.route('/jarvis/tags', methods=['GET'])(JavisController.javis_tags)
admin_blueprint.route('/jarvis/save_tags', methods=['POST'])(JavisController.save_tags)
admin_blueprint.route('/jarvis/save', methods=['POST'])(JavisController.save_jarvis)
admin_blueprint.route('/jarvis/train_conversation', methods=['GET'])(JavisController.train_conversation)
admin_blueprint.route('/jarvis/load-more-chat', methods=['GET'])(JavisController.load_more_chat)
admin_blueprint.route('/jarvis/save_jarvis_conversation', methods=['POST'])(JavisController.save_jarvis_conversation)

admin_blueprint.route('/scrapper/new_scrap', methods=['GET'])(ScrapperController.new_scrapper)
admin_blueprint.route('/scrapper/settings', methods=['GET'])(ScrapperController.scrapper_settings)