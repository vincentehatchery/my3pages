'''
Created on Aug 14, 2013

@author: vince_alcantara
'''
import unittest
from application import app
from google.appengine.ext import testbed
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import users
import os

def setCurrentUser(email, user_id, is_admin=False):
    os.environ['USER_EMAIL'] = email or ''
    os.environ['USER_ID'] = user_id or ''
    os.environ['USER_IS_ADMIN'] = '1' if is_admin else '0'

def logoutCurrentUser():
    setCurrentUser(None, None)

class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_user_stub()
       

    def tearDown(self):
        self.testbed.deactivate()

    def testName(self):
        pass
    
    def test_home_page(self):
        rv = self.app.get('/', follow_redirects=True)
        assert 'Welcome to My 3 Pages' in rv.data

    def test_about_page(self):
        rv = self.app.get('/about', follow_redirects=True)
        assert 'About My 3 Pages' in rv.data

    def test_feedback_page(self):
        rv = self.app.get('/feedback', follow_redirects=True)
        assert 'Feedback And Ways To Contact Me' in rv.data
        
    def test_write_page(self):
        setCurrentUser('test@example.com', 'testuser')
        rv = self.app.get('/write', follow_redirects=True)
        assert 'Welcome back' in rv.data

    def test_post_write_page(self):
        setCurrentUser('test@example.com', 'testuser')
        rv = self.app.post('/write', data=dict(
            daily_entry ='this is a test'
        ),follow_redirects=True)
    
        assert 'this is a test' in rv.data
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()