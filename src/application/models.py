'''
Created on Aug 14, 2013

@author: vince_alcantara
'''
from google.appengine.ext import db

"""
My3pages only uses one model - My3PagesEntry.  It contains:
- username: the user who entered the post
- date_entered: the day (without time) of when the user wrote the entry
- daily_entry: the written entry
"""

class My3PagesEntry(db.Model):
    username = db.UserProperty(required = True)
    date_entered = db.DateProperty(auto_now_add = True)
    daily_entry = db.TextProperty()