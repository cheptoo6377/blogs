from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional
from datetime import date

class MoodForm(FlaskForm):
    date = DateField("Date", default=date.today, validators=[Optional()])
    mood = IntegerField("Mood (1–10)", validators=[DataRequired(), NumberRange(min=1, max=10)])
    notes = TextAreaField("Notes", validators=[Optional()])
    submit = SubmitField("Submit")

class CBTForm(FlaskForm):
    date = DateField("Date", default=date.today, validators=[Optional()])
    thought = TextAreaField("Your Thought", validators=[DataRequired()])
    submit = SubmitField("Submit for AI Feedback")

class CheckInForm(FlaskForm):
    date = DateField("Date", default=date.today, validators=[Optional()])
    mood = IntegerField("Mood (1–10)", validators=[DataRequired(), NumberRange(min=1, max=10)])
    notes = TextAreaField("Notes", validators=[Optional()])
    submit = SubmitField("Submit Check-In")