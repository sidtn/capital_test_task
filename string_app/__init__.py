from flask import Blueprint

bp = Blueprint("string_app", __name__)

from string_app import handlers
