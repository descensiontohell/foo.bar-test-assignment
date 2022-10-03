import os
from flask import Flask
from dotenv import load_dotenv


def setup_config(app: Flask):
    load_dotenv()
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_DB")
    secret_key = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@localhost:5432/{db}"
    app.config["SECRET_KEY"] = secret_key if secret_key else os.urandom(32)
