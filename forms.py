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

# class UserInput(FlaskForm):

#     root_terms = StringField('Entity', [DataRequired()])
#     start_date = DateField('Start Date')
#     end_date = DateField('End Date')
#     # filetype = SelectMultipleField('Subject Timeframe', choices = [('pdf', 'PDF'), ('txt', 'txt')])
#     # filetype = MultiCheckboxField('Filetype', choices=['pdf', 'txt'])

#     submit = SubmitField('Submit')

class UserInput(FlaskForm):

    root_terms = StringField("Enter your search terms: ",[DataRequired()])
    start_date = DateField('Start Date: ')
    end_date = DateField('End Date: ')
    filetype = MultiCheckboxField('Filetype', choices=['pdf', 'txt'])
    search_engines = MultiCheckboxField('Search Engines', choices=["google", "yandex"])

    submit = SubmitField('Search')

class QuicksearchForm(FlaskForm):

    q = StringField('Additional Information', widget=widgets.TextArea()) #StringField('Entity', [DataRequired()])

    submit = SubmitField('Submit')


