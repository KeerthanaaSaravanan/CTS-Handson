from flask import Flask, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    """Application factory function.

    The factory pattern allows creating multiple instances of the application
    with different configurations. This is useful for testing (e.g., creating
    an app with a test configuration) and for deploying the same application
    in different environments (development, production, etc.) with different
    settings.

    Benefits:
    - Avoids circular imports by delaying the import of modules that depend
      on the app instance.
    - Allows multiple apps to exist in the same Python process (useful for
      testing).
    - Makes the application more modular and easier to configure.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from courses.routes import courses_bp
    app.register_blueprint(courses_bp, url_prefix='/api')

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

    return app