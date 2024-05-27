from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config



db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.models import Ticket
    from app.routes.tickets_bp import tickets_bp
    app.register_blueprint(tickets_bp, url_prefix="/")

    db.init_app(app)
    migrate.init_app(app, db)

    return app
