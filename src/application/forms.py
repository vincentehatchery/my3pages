'''
Created on Aug 14, 2013

@author: vince_alcantara

forms.py:
    This module borrows from Flask-WTF and its built-in validation
'''

from flaskext import wtf
from flaskext.wtf import validators

class My3PagesEntryForm(wtf.Form):
    entry = wtf.TextAreaField('Entry', validators=[validators.Required()])
