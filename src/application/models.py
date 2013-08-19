'''
Created on Aug 14, 2013

@author: vince_alcantara
'''
from google.appengine.ext import ndb

"""
My3pages only uses one model - My3PagesEntry.  It contains:
- username: the user who entered the post
- date_entered: the day (without time) of when the user wrote the entry
- daily_entry: the written entry
"""

class My3PagesEntry(ndb.Model):
    username = ndb.UserProperty(required = True)
    date_entered = ndb.DateProperty(required = True)
    daily_entry = ndb.TextProperty()