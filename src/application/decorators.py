'''
Created on Aug 14, 2013

@author: vince_alcantara

decorators.py: 
    Decorators are wrapper functions that are called before other functions.
    In this case we are creating two decorators:
        - login_required to be run when accessing certain pages
'''

from functools import wraps
from google.appengine.api import users
from flask import redirect, request

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not users.get_current_user():
            # redirect the user to create a google login
            return redirect(users.create_login_url(request.url))
        return func(*args, **kwargs)
    return decorated_view


