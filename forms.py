import string
from tokenize import String
# from tkinter.tix import Form
# from sqlalchemy import Integer
# from wtforms.fields.choices import SelectField
from wtforms import BooleanField, StringField, PasswordField, FloatField, SubmitField, DateField, SelectField, SelectMultipleField, RadioField, widgets, IntegerField, FieldList, FormField, FileField
# from wtforms.fields import choices
# from wtforms.fields.datetime import DateTimeLocalField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


import pandas as pd

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class UserInput(FlaskForm):

    entity = StringField('Entity', [DataRequired()])
    startdate = DateField('Start Date')
    enddate = DateField('End Date')
    # filetype = SelectMultipleField('Subject Timeframe', choices = [('pdf', 'PDF'), ('txt', 'txt')])
    # filetype = MultiCheckboxField('Filetype', choices=['pdf', 'txt'])

    submit = SubmitField('Submit')


class UserInputAP(FlaskForm):

    entity = StringField("Enter your search terms: ",[DataRequired()])
    startdate = DateField('Start Date: ')
    enddate = DateField('End Date: ')
    filetype = MultiCheckboxField('Filetype', choices=['pdf', 'txt'])
    search_engines = MultiCheckboxField('Label', choices=["google", "yandex"])

    submit = SubmitField('Search')


