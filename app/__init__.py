# App package 
from flask import Flask
from app.webhook.routes import webhook_bp
from app.webhook.extensions import mongo

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/github_webhooks"

    mongo.init_app(app)

    app.register_blueprint(webhook_bp)

    return app
