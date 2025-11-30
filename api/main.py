# main.py

from flask import Flask, render_template
from routes import *

app = Flask(__name__)

# Configure the app
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
from db import db
db.init_app(app)

# Register blueprints
from blueprints.home import home_bp
app.register_blueprint(home_bp)

from blueprints.auth import auth_bp
app.register_blueprint(auth_bp)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)