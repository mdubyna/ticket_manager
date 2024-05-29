import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "you-will-never-guess")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = os.environ.get(
        "SECURITY_PASSWORD_SALT",
        "ab3d3a0f6984c4f5hkao41509b097a7bd498e903f3c9b2eea667h16",
    )
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
