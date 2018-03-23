# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# database object
mysqldb = SQLAlchemy(app)

# Error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_rest.controllers import mod_rest as rest_module

# Register blueprint(s)
app.register_blueprint(rest_module)

# Build and Create the database file using SQLAlchemy
#db.create_all()