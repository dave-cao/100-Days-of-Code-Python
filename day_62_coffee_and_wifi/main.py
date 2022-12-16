import csv
from csv import writer

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label="Cafe Name", validators=[DataRequired()])
    location = StringField(
        label="Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    open_time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired()])
    closing_time = StringField(
        label="Closing Time e.g. 5:30PM", validators=[DataRequired()]
    )
    coffee_rating = SelectField(
        label="Coffee Rating", choices=["✘", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️"]
    )
    wifi_rating = SelectField(
        label="Wifi Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪"]
    )
    outlet_rating = SelectField(
        label="Outlet Rating", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌"]
    )
    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = [
            form.cafe.data,
            form.location.data,
            form.open_time.data,
            form.closing_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.outlet_rating.data,
        ]

        with open("./cafe-data.csv", "a") as csv:
            writer(csv).writerow(new_cafe)

        return redirect(url_for("cafes"))

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
