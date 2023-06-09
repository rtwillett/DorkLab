import string
from tokenize import String
from wtforms import BooleanField, StringField, PasswordField, FloatField, SubmitField, DateField, SelectField, SelectMultipleField, RadioField, widgets, IntegerField, FieldList, FormField, FileField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


import pandas as pd

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class UserInput(FlaskForm):

    root_terms = StringField("What are you looking for (names, locations, organizations, etc.)? ",[DataRequired()])
    start_date = DateField('Start Date: ')
    end_date = DateField('End Date: ')
    filetype = MultiCheckboxField('Filetype', choices=['pdf', 'txt', 'docx', 'csv'])
    moreterms = StringField('Words to include in search:', widget=widgets.TextArea())
    filterwords = StringField('Words to exclude from search:', widget=widgets.TextArea())
    
    submit = SubmitField('Search')

class QuicksearchForm(FlaskForm):

    q = StringField('Enter a query to build a string from', widget=widgets.TextArea(), validators=[DataRequired()])

    submit = SubmitField('Submit')


