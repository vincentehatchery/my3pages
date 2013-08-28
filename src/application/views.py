'''
Created on Aug 14, 2013

@author: vince_alcantara

Description: This module details the urls and views associated with my3pages

'''

from application import app
from decorators import login_required
from models import My3PagesEntry
from forms import My3PagesEntryForm
from flask import render_template, request, flash, redirect
import datetime
from flask_cache import Cache
from google.appengine.api import users

    

cache = Cache(app)

@app.route('/')
def home_page():
    username = users.get_current_user()
    return render_template('home.html', username=username)

@app.route('/logout/')
def logout_page():
    if users.get_current_user():
        return redirect(users.create_logout_url('/logged_out'))
    else:
        return redirect('/')

@app.route('/logged_out/')
def loggedout_page():
    if not users.get_current_user():
        return  render_template('logged_out.html')


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
                              
    #new_key_id = entry.key
    #print "new key id %s", new_key_id 
 
    if request.method == 'GET':
        # Display the existing entry in the form if it exists
        form.daily_entry.process_data(entry.daily_entry)
    
        return render_template('write.html', form=form, entry = entry, username=username)
    
    elif request.method == 'POST':
        #form = My3PagesEntryForm()
        if form.validate_on_submit():
            
            entry.daily_entry = form['daily_entry'].data
            
            entry.put()
            todays_datetime = datetime.datetime.today()
            flash(u"Entry last saved:%s" % (todays_datetime))
            return render_template('write.html',form=form, entry = entry, username=username)
        
@app.route('/previous_entries/')
@login_required
def previous_enties():
    
    username = users.get_current_user()
    
    entries = My3PagesEntry.gql("WHERE username =:username", username = username)
    
    return render_template('previous_entries.html', entries = entries, username=username)
    
@app.route('/inspiration/')
def inspiration_page():
    
    username = users.get_current_user()
    
    return render_template('inspiration.html', username=username)

@app.route('/feedback/')
def feedback_page():
    
    username = users.get_current_user()
    
    return render_template('feedback.html', username=username)
 
@app.route('/previous_entries/<int:entry_id>')
def previous_entries_edit(entry_id):
    entry = My3PagesEntry.get_by_id(entry_id)
    form = My3PagesEntryForm()
    
    form.daily_entry.process_data(entry.daily_entry)
    
    return render_template('write.html',form=form, entry=entry, username=entry.username)
    