from flask import Flask, render_template
from dotenv import load_dotenv
import os


load_dotenv()
host = os.getenv('FLASK_RUN_HOST')
port = os.getenv('FLASK_RUN_PORT')


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    @app.route('/')
    def home():
        return render_template('home.html')

    from .views import chat_views
    app.register_blueprint(chat_views.bp)

    return app
