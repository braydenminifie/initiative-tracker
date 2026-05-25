from flask import Flask
from .extensions import db, migrate, cors
from .static_conditions import seed_conditions

def create_app(config_class="app.config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)


    #Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    #Register blueprints
    from .routes.encounter_routes import encounter_bp
    from .routes.combatant_routes import combatant_bp
    from .routes.condition_routes import condition_bp
    app.register_blueprint(encounter_bp, url_prefix="/api/encounters")
    app.register_blueprint(combatant_bp, url_prefix="/api/combatants")
    app.register_blueprint(condition_bp, url_prefix="/api/conditions")

    with app.app_context():
        db.create_all()
        seed_conditions()

    return app