'''
Created on Aug 14, 2013

@author: vince_alcantara

Description: This module details the urls and views associated with my3pages

'''

from application import app
from decorators import login_required
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
@login_required
def write_entry():
    todays_date = datetime.date.today()
    username = users.get_current_user()
    
    form = My3PagesEntryForm()

    #Determine if entry already exists
    result = My3PagesEntry.gql("WHERE username = :username AND date_entered =:todays_date", username = username, todays_date=todays_date).get()

    if (result == None):
        # Create a new entry
        entry = My3PagesEntry(username = users.get_current_user(), date_entered = datetime.date.today())
    else:
        entry = result
        # http://stackoverflow.com/questions/5117479/wtforms-how-to-prepopulate-a-textarea-field
                              
    new_key_id = entry.key
    
    print "new key id %s", new_key_id 
    
    if request.method == 'GET':
        # Display the existing entry in the form if it exists
        form.daily_entry.process_data(entry.daily_entry)
    
        return render_template('write.html', form=form, entry = entry)
    
    elif request.method == 'POST':
        #form = My3PagesEntryForm()
        if form.validate_on_submit():
            
            entry.daily_entry = form['daily_entry'].data
            
            #new_entry = My3PagesEntry(username = users.get_current_user(), daily_entry = form['entry'].data)
            entry.put()
            flash('Entry saved')
            return render_template('write.html',form=form, entry = entry)
        
@app.route('/previous_entries/')
@login_required
def previous_enties():
    
    username = users.get_current_user()
    
    entries = My3PagesEntry.query()
    
    return render_template('previous_entries.html', entries = entries)
    
    