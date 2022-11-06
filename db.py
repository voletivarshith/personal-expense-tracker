from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
class User(db):
    id = db.Column(db.Integer,primary_key=True,)