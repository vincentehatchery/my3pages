'''
Created on Aug 14, 2013

@author: vince_alcantara

Description: This module details the urls and views associated with my3pages

'''
import os
from application import app
from decorators import login_required
from models import My3PagesEntry
from forms import My3PagesEntryForm
from flask import render_template, request, flash, redirect, send_from_directory
import datetime
#from dateutil import tz
#import time
from flask_cache import Cache
from google.appengine.api import users


    

cache = Cache(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home_page():
    #username = users.get_current_user()
    #form = My3PagesEntryForm(request.form)
    #return render_template('index.html', username=username, form=form)
        
    return redirect('/write')

@app.route('/about/')
def about_page():
    username = users.get_current_user()
    form = My3PagesEntryForm(request.form)
    
    return render_template('about.html', username=username, form=form)

@app.route('/login/')
def login_page():
    if (not users.get_current_user()):
        return redirect(users.create_login_url('/write'))
    else:
        return redirect('/')

@app.route('/logout/')
def logout_page():
    if users.get_current_user():
        return redirect(users.create_logout_url('/logged_out'))
    else:
        return redirect('/')

@app.route('/logged_out/')
def loggedout_page():
    form = My3PagesEntryForm(request.form)
    if not users.get_current_user():
        return  render_template('logged_out.html', form=form)


@app.route('/write/', methods = ['GET', 'POST'])
#@login_required
def write_entry():
    username = users.get_current_user()
    
    form = My3PagesEntryForm(request.form)
    
    
    #Get today's date from the query string
    qs_todays_date = request.args.get('date_entered')

    if (qs_todays_date == None):
        # query string is empty, assign todays_date to be the server's date
        todays_date = datetime.date.today()
    else:
        todays_date = datetime.datetime.strptime(qs_todays_date, '%Y-%m-%d').date()
        
    #js_todays_date = form['date_entered'].data
  #  todays_datetime = datetime.datetime.fromtimestamp(js_todays_date/1000.0)
   
   # print "todays date is begin", qs_todays_date
#     print "todays_datetime is begin", todays_datetime
    
    #print "todays_date", todays_date

    #Determine if entry already exists
    result = My3PagesEntry.gql("WHERE username = :username AND date_entered =:todays_date", username = username, todays_date=todays_date).get()

    if (result == None):
        # Create a new entry
        entry = My3PagesEntry(username = username, date_entered = todays_date)
        #form.date_entered = datetime.date.today()
    else:
        entry = result
        # http://stackoverflow.com/questions/5117479/wtforms-how-to-prepopulate-a-textarea-field
                              
    #new_key_id = entry.key
    #print "new key id %s", new_key_id 
 
    if request.method == 'GET':
        # Display the existing entry in the form if it exists
        # Convert the daily entry in to a format the form can read
        form.daily_entry.process_data(entry.daily_entry)
    
        return render_template('write.html', form=form, entry = entry, username=username)
    
    elif request.method == 'POST':
        #Get the form again
           
        if form.validate():
            
           # print "todays date is post", js_todays_date
           # python_todays_date = float(js_todays_date)/1000
          #  print "pythons todays date is post", python_todays_date
          #  new_todays_date = python_todays_date
            
            entry.daily_entry = form['daily_entry'].data
            if not users.get_current_user():
            # redirect the user to create a google login
                return redirect(users.create_login_url(request.url))
        
            entry.put()
            flash("Entry saved successfully")
            return render_template('write.html',form=form, entry = entry, username=username)
        else:
            flash("Please correct the below errors:")
            return render_template('write.html',form=form, entry = entry, username=username)
        
@app.route('/write_new/', methods = ['GET','POST'])
@login_required
def write_new():
    """
    Retrieve the entry for this username for the specific date and populate the form
    """
    form = My3PagesEntryForm(request.form)
    username = users.get_current_user()
    string_date = form['date_entered'].data
    #specific_date = string_date
    specific_date = datetime.datetime.strptime(string_date, '%Y-%m-%d').date()
    
    #print "The specific date is", specific_date
    
    result = My3PagesEntry.gql("WHERE username = :username AND date_entered =:specific_date", username = username, specific_date = specific_date).get()
    if (result == None):
        # Create a new entry and blank form
        entry = My3PagesEntry(username = users.get_current_user(), date_entered = specific_date)
        print "found no match"
    else:
        entry = result
        form.daily_entry.process_data(entry.daily_entry)
        print "found match"
        
    return render_template('write.html', form=form, entry = entry, username=username)

@app.route('/write/?date_entered=<specific_date>', methods = ['GET','POST'])
@login_required
#TODO Ensure that only the user who created the entry can access their entry
def write_specific_date(specific_date):
    """
    Retrieve the entry for this username for the specific date and populate the form
    """
    form = My3PagesEntryForm(request.form)
    username = users.get_current_user()
    #string_date = form['date_entered'].data
    #specific_date = string_date
    #specific_date = datetime.datetime.strptime(string_date, '%Y-%m-%d').date()
    
    #print "The specific date is", specific_date
    
    result = My3PagesEntry.gql("WHERE username = :username AND date_entered =:specific_date", username = username, specific_date = specific_date).get()
    if (result == None):
        # Create a new entry and blank form
        entry = My3PagesEntry(username = users.get_current_user(), date_entered = specific_date)
        print "found no match"
    else:
        entry = result
        form.daily_entry.process_data(entry.daily_entry)
        print "found match"
        
    return render_template('write.html', form=form, entry = entry, username=username)


@app.route('/previous_entries/')
@login_required
def previous_entries():
    form = My3PagesEntryForm(request.form)
    username = users.get_current_user()
    
    entries = My3PagesEntry.gql("WHERE username =:username ORDER BY date_entered DESC", username = username)
    
    return render_template('previous_entries.html', entries = entries, username=username, form=form)

    
@app.route('/inspiration/')
def inspiration_page():
    
    username = users.get_current_user()
    form = My3PagesEntryForm(request.form)
    return render_template('inspiration.html', username=username, form=form)

@app.route('/feedback/')
def feedback_page():
    
    username = users.get_current_user()
    form = My3PagesEntryForm(request.form)
    return render_template('feedback.html', username=username, form=form)
 
@app.route('/previous_entries/<int:entry_id>')
def previous_entries_edit(entry_id):
    entry = My3PagesEntry.get_by_id(entry_id)
    form = My3PagesEntryForm()
    
    form.daily_entry.process_data(entry.daily_entry)
    
    return render_template('write.html',form=form, entry=entry, username=entry.username)
    