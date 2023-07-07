from flask import Flask

from config import FlaskConfig
from library.exceptions import exception_handler
from routes.claims.route import claims_bp
from routes.roles.route import roles_bp
from routes.route import generic_bp
from routes.user_claims.route import user_claims_bp
from routes.users.route import users_bp
from swagger import initialize_flasgger


def create_app():
    try:
        app = Flask(__name__)

        initialize_flasgger(app)

        app.config.from_object(FlaskConfig())
        app.register_error_handler(Exception, exception_handler)

        # Blueprints
        app.register_blueprint(generic_bp, url_prefix="/api/v1")

        app.register_blueprint(users_bp, url_prefix="/api/v2/user")
        app.register_blueprint(roles_bp, url_prefix="/api/v2/role")
        app.register_blueprint(claims_bp, url_prefix="/api/v2/claim")
        app.register_blueprint(user_claims_bp, url_prefix="/api/v2/user-claim")

        return app
    except Exception as e:
        raise Exception(f"Error while creating app: {e}")


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
