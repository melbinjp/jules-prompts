from flask import Flask

from pantry.api import admin, orders
from pantry.notifications.worker import start_worker


def create_app():
    app = Flask(__name__)
    app.register_blueprint(orders.bp)
    app.register_blueprint(admin.bp)
    start_worker(app)  # sends order emails from a thread in this process
    return app
