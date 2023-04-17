import string
from tokenize import String
# from tkinter.tix import Form
# from sqlalchemy import Integer
# from wtforms.fields.choices import SelectField
from wtforms import BooleanField, StringField, PasswordField, FloatField, SubmitField, DateField, SelectField, RadioField, widgets, IntegerField, FieldList, FormField, FileField
# from wtforms.fields import choices
# from wtforms.fields.datetime import DateTimeLocalField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


import pandas as pd

class InputURL(FlaskForm):

    url = StringField('Username', [DataRequired()])
    submit = SubmitField('Submit')

class SelectFile(FlaskForm):

    pdf_file = FileField('Document',validators = [FileRequired(), FileAllowed(['pdf'])])

    submit = SubmitField('Add Data')