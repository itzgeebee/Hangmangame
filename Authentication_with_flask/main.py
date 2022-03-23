# How to create an authentication page with flask
# import required files
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

login_manager = LoginManager()
app = Flask(__name__)
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FILES'] = "static/files"
db = SQLAlchemy(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
db.create_all()

# initialize login manager.
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    """ Register new users and hash and salt passwords for security"""
    if request.method == "POST":
        try:
            new_user = User(
                email=request.form["email"],
                password=generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8),
                name=request.form["name"])
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            error = "email already exists"
            return redirect(url_for("login", error=error))
            # return render_template("login.html", error=error)
        else:

            login_user(new_user)
            return redirect(url_for("secrets", name=new_user.name))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    error = request.args.get("error")
    if error is None:
        error = ""
    if request.method == "POST":
        user_email = request.form.get("email")
        user_password = request.form.get("password")
        user = User.query.filter_by(email=user_email).first()
        if not user:
            error = "Invalid email"
        else:
            if check_password_hash(pwhash=user.password, password=user_password):
                flash("Success")
                login_user(user)
                return redirect(url_for("secrets", name=user.name))
            else:
                error = "Invalid password"

    return render_template("login.html", error=error, logged_in=current_user.is_authenticated)


@app.route('/secrets/<name>', methods=["GET", "POST"])
@login_required
def secrets(name):
    print(current_user.name)

    return render_template("secrets.html", name=name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download/')
@login_required
def download():
    """ function for flask downloads """
    return send_from_directory(app.config['FILES'],
                               path="cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
