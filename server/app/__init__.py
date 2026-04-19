from flask import Flask
from .extensions import db, migrate, cors

def create_app():
    app = Flask(__name__)

    #App configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///initiative.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    #Register blueprints
    from .routes.encounter_routes import encounter_bp
    app.register_blueprint(encounter_bp, url_prefix="/api/encounters")

    return app