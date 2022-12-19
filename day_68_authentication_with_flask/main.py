from flask import (Flask, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "any-secret-key-you-choose"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Flask login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # if the user already exists
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists! Please login instead.")
            return redirect(url_for("login"))

        name = request.form.get("name")
        password = generate_password_hash(
            request.form.get("password"), method="pbkdf2:sha256", salt_length=8
        )
        new_user = User(
            email=request.form.get("email"),
            password=password,
            name=name,
        )
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

        login_user(new_user)
        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        # check if user exists
        if not user:
            flash("This email doesn't exist in our database!")
            return render_template("login.html")

        # Check passwords
        pwhash = user.password
        if check_password_hash(pwhash=pwhash, password=password):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            flash("Incorrect password!")
            return render_template("login.html")

    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    name = request.args.get("name")
    return render_template("secrets.html", name=name)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
