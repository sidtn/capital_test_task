from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(testing=False):
    application = Flask(__name__)
    application.url_map.strict_slashes = False

    if testing:
        application.config["TESTING"] = True
        application.config["SQLALCHEMY_DATABASE_URI"] = config.TEST_DB_URI
    else:
        application.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI

    db.init_app(application)
    migrate.init_app(application, db)

    from string_app import bp as string_app_bp

    application.register_blueprint(string_app_bp)

    return application


app = create_app()
