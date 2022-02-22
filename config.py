import os
import pathlib


class Config:
    __base_dir = pathlib.Path(__file__).resolve().parent
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{str(__base_dir)}/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
