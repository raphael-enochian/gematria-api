# -*- coding: utf-8 -*-
# Gematria-API (c) Raphael Enochian

from flask import Flask
from flask.ext.restful import Api
from flask.ext.redis import FlaskRedis
import logging


rest_extension = Api()
redis_store = FlaskRedis()


def create_app():
    gematria_api = Flask(__name__)
    gematria_api.config.from_envvar('SETTINGS')
    # rest_extension.init_app(gematria_api)
    return gematria_api
