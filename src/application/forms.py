'''
Created on Aug 14, 2013

@author: vince_alcantara

forms.py:
    This module borrows from Flask-WTF and its built-in validation
    
    The form contains two entries:
    1) daily_entry : a text area for typing the user's 3 pages
    2) date_entered : a hidden entry used to display the client date not the server date.  See the javascript file display_date.js
'''

#from flaskext import wtf
#from flaskext.wtf import validators
from wtforms import Form, validators, TextAreaField, TextField

class My3PagesEntryForm(Form):
    daily_entry = TextAreaField('DailyEntry', [
        validators.DataRequired()
    ])
    date_entered = TextField('DateEntered')


