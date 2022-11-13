from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c\xae_O#H\xbdjTD\xed\xcf\x9e\x0f\xa3,\xbb\xcd:\x08\x05\xb8>\x18'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from PersonalExpenseTracker.models import User
@app.route("/")
def hello():
	return "Hello World"
@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		email = request.form.get("email",'')
		password = request.form.get("password",'')
		user = User.query.filter_by(email=email).first()
	
		obj = Bcrypt()
		if obj.check_password_hash(user.password,password):
			flash("Login successful")

	return render_template("login.html")
@app.route("/signup",methods=["GET","POST"])
def signup():
	from .validators import UserValidator
	if request.method=="POST":
		# Validation code for signup page
		firstName = request.form.get("firstName",'')
		lastName = request.form.get("lastName","")
		userName = request.form.get("userName",'')
		email = request.form.get("email",'').lower()
		password = request.form.get("password",'')
		msg = UserValidator()
		msg = msg.validate(firstName,lastName,userName,email,password)
		if msg==True:
			obj = Bcrypt()
			pwd = obj.generate_password_hash(password).decode("utf-8")
			user = User(firstName=firstName,lastName=lastName,email=email,userName=userName,password=pwd)
			db.session.add(user)
			db.session.commit()
			flash("Account created successfully")
			return redirect(url_for("login"))
		else:
			flash(msg)
	return render_template("signup.html")