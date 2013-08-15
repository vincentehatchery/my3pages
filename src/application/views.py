'''
Created on Aug 14, 2013

@author: vince_alcantara

Description: This module details the urls and views associated with my3pages

'''

from application import app
from models import My3PagesEntry
from forms import My3PagesEntryForm
from flask import render_template, request, flash, redirect, url_for
import datetime
from flask_cache import Cache
from google.appengine.api import users


cache = Cache(app)

@app.route('/')
def home_page():
    return render_template('home.html')

#
@app.route('/write/', methods = ['GET', 'POST'])
def write_entry():
    todays_date = datetime.date.today().strftime("%d-%m-%y")
    #entry= My3PagesEntry(username='vincent@infration.com', date_entered=todays_date, entry='this') 
    form = My3PagesEntryForm()

    if request.method == 'GET':
     #   return render_template('write.html', entry=entry )
      # return render_template('write.html')
        return render_template('write.html', form=form)
    
    elif request.method == 'POST':
        #form = My3PagesEntryForm()
        if form.validate_on_submit():
            new_entry = My3PagesEntry(username = users.get_current_user(), daily_entry = form['entry'].data)
            new_entry.put()
            flash('Entry saved')
            return render_template('write.html',form=form)
        
"""
@app.route('/write/new', methods = ['GET','POST'])
def new_write_entry():
    form = My3PagesEntryForm()
    if form.validate_on_submit():
        new_entry = My3PagesEntry(username = users.get_current_user(), daily_entry = form['entry'].data)
        new_entry.put()
        flash('Entry saved')
        return redirect(url_for('write_entry'))
    return render_template('new_entry.html',form=form)
    
   """ 