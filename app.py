from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from validators import UserValidator
app = Flask(__name__)
app.secret_key='c\xae_O#H\xbdjTD\xed\xcf\x9e\x0f\xa3,\xbb\xcd:\x08\x05\xb8>\x18'
# db = SQLAlchemy(app)
@app.route("/")
def hello():
	return "Hello World Hey"
@app.route("/login")
def login():
	return render_template("login.html")
@app.route("/signup",methods=["GET","POST"])
def signup():
	if request.method=="POST":
		# Validation code for signup page
		firstName = request.form.get("firstName",'')
		lastName = request.form.get("lastName","")
		userName = request.form.get("userName",'')
		email = request.form.get("email",'')
		password = request.form.get("password",'')
		msg = UserValidator()
		msg = msg.validate(firstName,lastName,userName,email,password)
		if msg==True:
			flash("Account created successfully")
			return redirect(url_for("login"))
		else:
			flash(msg)
	return render_template("signup.html")

if __name__=="__main__":
	app.run(debug=True)