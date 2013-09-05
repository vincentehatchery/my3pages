'''
Created on Aug 14, 2013

@author: vince_alcantara

forms.py:
    This module borrows from Flask-WTF and its built-in validation
'''

#from flaskext import wtf
#from flaskext.wtf import validators
from wtforms import Form, validators, TextAreaField, TextField

class My3PagesEntryForm(Form):
    daily_entry = TextAreaField('DailyEntry', [
        validators.DataRequired()
    ])
    date_entered = TextField('DailyEntered', validators=[validators.Required()])


"""
class My3PagesEntryForm(wtf.Form):
    daily_entry = wtf.TextAreaField('DailyEntry', [
        validators.Required(message="The entry can't be empty"),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    date_entered = wtf.TextField('DailyEntered', validators=[validators.Required()])
"""