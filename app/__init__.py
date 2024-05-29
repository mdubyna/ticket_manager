from flask import Flask
from flask_migrate import Migrate
from flask_security import SQLAlchemySessionUserDatastore, Security

from config import Config
from app.routes.tickets_bp import tickets_bp
from app.routes.groups_bp import groups_bp
from app.routes.users_bp import users_bp
from app.routes.home_page import home_bp
from app.models import db, User, Role


migrate = Migrate()


def create_app() -> Flask:
    """
    Function for app creating
    :return:
    Flask app
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(tickets_bp, url_prefix="/")
    app.register_blueprint(groups_bp, url_prefix="/")
    app.register_blueprint(users_bp, url_prefix="/")
    app.register_blueprint(home_bp, url_prefix="/")

    db.init_app(app)
    migrate.init_app(app, db)

    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)

    with app.app_context():
        db.create_all()
        create_initial_data(user_datastore)

    return app


def create_initial_data(
        user_datastore: SQLAlchemySessionUserDatastore
) -> None:
    """
    Function for creating initial data
    :param user_datastore:
    :return:
    None
    """
    roles = [
        {"name": "admin", "description": "Administrator"},
        {"name": "manager", "description": "Manager"},
        {"name": "analyst", "description": "Analyst"},
    ]

    users = [
        {
            "email": "admin@admin.com",
            "password": "$2b$12$sCPhUXUnMqhAAJBiCX"
                        "nyNeQiAmeNX.CuQcKGkIXdieL7wmeJA.UUO",
            "roles": ["admin"]
        },
        {
            "email": "manager@manager.com",
            "password": "$2b$12$sCPhUXUnMqhAAJBiCX"
                        "nyNeQiAmeNX.CuQcKGkIXdieL7wmeJA.UUO",
            "roles": ["manager"]
        },
        {
            "email": "analyst@analyst.com",
            "password": "$2b$12$sCPhUXUnMqhAAJBiCX"
                        "nyNeQiAmeNX.CuQcKGkIXdieL7wmeJA.UUO",
            "roles": ["analyst"]
        },
    ]

    for role in roles:
        if not user_datastore.find_role(role["name"]):
            user_datastore.create_role(**role)

    for user in users:
        if not user_datastore.find_user(email=user["email"]):
            user_datastore.create_user(**user)

    db.session.commit()
