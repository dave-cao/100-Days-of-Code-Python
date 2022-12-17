# Keeping all my forms here
from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


# Form to edit movie
class EditMovie(FlaskForm):
    rating = DecimalField(
        label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired(), NumberRange(min=0, max=10)]
    )
    review = StringField(
        label="Your Review", validators=[DataRequired()]
    )
    submit = SubmitField("Done")



# Form to add movie
class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

