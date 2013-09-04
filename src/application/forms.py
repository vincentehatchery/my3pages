'''
Created on Aug 14, 2013

@author: vince_alcantara

forms.py:
    This module borrows from Flask-WTF and its built-in validation
'''

from flaskext import wtf
from flaskext.wtf import validators

class My3PagesEntryForm(wtf.Form):
    daily_entry = wtf.TextAreaField('DailyEntry', validators=[validators.Required()])
    date_entered = wtf.TextField('DailyEntered', validators=[validators.Required()])
