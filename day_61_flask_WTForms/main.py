from secrets import token_hex

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = EmailField(
        label="Email", validators=[DataRequired(), Length(max=30), Email()]
    )
    password = PasswordField(
        label="Password", validators=[DataRequired(), Length(min=8, max=30)]
    )
    login = SubmitField("Login")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = token_hex(16)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
