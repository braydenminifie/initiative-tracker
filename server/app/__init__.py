from flask import Flask
from .extensions import db, migrate, cors

def create_app(config_class="app.config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)


    #Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    #Register blueprints
    from .routes.encounter_routes import encounter_bp
    app.register_blueprint(encounter_bp, url_prefix="/api/encounters")

    return app