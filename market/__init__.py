from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '6993ea4c4cf889c15ca5bf1b'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'  # Redirect to login page if not logged in
login_manager.login_message_category = 'info'  # Flash message category for login prompt


# 🔥 Register the user loader here
from market.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes and migrations last to avoid circular imports
from market import routes
from flask_migrate import Migrate

migrate = Migrate(app, db)
