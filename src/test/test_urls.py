'''
Created on Aug 14, 2013

@author: vince_alcantara
'''
import unittest
from application import app

class Test(unittest.TestCase):


    def setUp(self):
        self.app = app.test_client()


    def tearDown(self):
        pass


    def testName(self):
        pass

    
    def test_home_page(self):
        rv = self.app.get('/', follow_redirects=True)
        assert "writer's block" in rv.data
    def test_write_page(self):
        rv = self.app.get('/write', follow_redirects=True)
        assert 'Welcome back' in rv.data

    def test_post_write_page(self):
        rv = self.app.post('/write', data=dict(
            username='alcantara@news.com.au',
            daily_entry ='this is a test'
        ),follow_redirects=True)
        
        print rv.data
        assert 'this is a test' in rv.data
        

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()