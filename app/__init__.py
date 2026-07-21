from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message = "Please login first."
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import all models so Flask-Migrate detects them
    from app.models import User, Employee, Department

    # Register Blueprints
    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.employee import employee
    from app.routes.leave import leave
    from app.routes.attendance import attendance
    from app.routes.export import export
    from app.routes.profile import profile
    from app.routes.department import department

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(employee)
    app.register_blueprint(leave)
    app.register_blueprint(attendance)
    app.register_blueprint(export)
    app.register_blueprint(profile)
    app.register_blueprint(department)

    return app