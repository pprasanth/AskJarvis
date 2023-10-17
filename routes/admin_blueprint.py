from flask import Blueprint
from controllers.adminAuthController import admin_login, admin_login_view
from controllers.dashboardController import dashboard

admin_blueprint = Blueprint('admin_blueprint', __name__)

admin_blueprint.route('/', methods=['GET'])(admin_login_view)
admin_blueprint.route('/login', methods=['POST'])(admin_login)
admin_blueprint.route('/dashboard', methods=['GET'])(dashboard)
