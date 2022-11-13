from .app import db
from datetime import date
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    userName = db.Column(db.String(20),unique=True,nullable=True)
    firstName = db.Column(db.String(20),unique=False,nullable=True)
    lastName = db.Column(db.String(20),unique=False,nullable=True)
    email = db.Column(db.String(20),unique=True,nullable=True)
    password = db.Column(db.String(60),nullable=True)
    expense = db.relationship('Budget',backref='creator',lazy=True)
    def __repr__(self):
        return str(self.userName)
    def __str__(self):
        return str(self.userName)
class Budget(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Integer,nullable=True)
    created = db.Column(db.Date,default=date.today)
    user = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=True)
    categories = db.relationship("Expense",backref="",lazy=True)
    is_active = db.Column(db.Boolean,default=True)
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category = db.Column(db.String(20),unique=True)
    def __repr__(self):
        return self.category
class Expense(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    budget = db.Column(db.Integer,db.ForeignKey("budget.id"),nullable=True)
    amount = db.Column(db.Integer,default=0)
    category = db.Column(db.Integer,db.ForeignKey("category.id"))