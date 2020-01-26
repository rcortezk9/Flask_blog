from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '706654381b7c5e569dece0add128e89a'
# database
app.config['SQLALCHEMY_DATABASE-URI'] = 'squlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
