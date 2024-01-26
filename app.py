from flask import Flask

from views import app_view
from views.admin import admin_view
from utils.error_handlers import page_not_found, method_not_allowed, internal_server_error

app = Flask(__name__)

app.register_blueprint(app_view)
app.register_blueprint(admin_view)

app.register_error_handler(404, page_not_found)
app.register_error_handler(405, method_not_allowed)
app.register_error_handler(500, internal_server_error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
