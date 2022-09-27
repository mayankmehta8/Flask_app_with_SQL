from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.static_folder = 'static'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 't17_altf4'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class RegForm(FlaskForm):
    user = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submitf = SubmitField('Register')

    def validate_username(self, user):
        existing_user = User.query.filter_by(username=user.data).first()
        if existing_user:
            raise ValidationError('That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    user = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submitf = SubmitField('Login')

@app.route("/")
def main():
    return render_template("index.html") 

@app.route("/updates")
def update():
    return render_template("updates.html")

@app.route("/login", methods=["GET",'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.user.data).first()
        if existing_user:
            if existing_user.password==form.password.data:
                return redirect("https://discord.gg/hmvnvNb4aX",code=302)
    return render_template("login.html",form=form)
    
@app.route("/register", methods=["GET","POST"])
def register():
    form=RegForm()
    if form.validate_on_submit():
        nuser=User(username=form.user.data,password=form.password.data)
        db.session.add(nuser)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html",form=form)
@app.route("/about")
def about():
    return render_template("about.html")
if __name__=='__main__':
    app.run(debug=True)
    