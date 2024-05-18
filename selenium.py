#Imports from the lecture
from lib2to3.pgen2 import driver
from operator import index
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium import webdriver

#Imports for unittests
import os
os.environ['DATABASE_URL'] = 'sqlite://'
from datetime import datetime, timezone, timedelta
import unittest
from app import app, db
import sqlalchemy as sa

from app.models import *

localHost = "http://localhost:5000/"

class SeleniumTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        #add_test_data_to_db()

        self.server_thread = multiprocessing.Process(target=self.testApp.run)
        self.server_thread.start()
        self.driver = webdriver.Chrome()
        self.driver.get(localHost)

        #Setting it as headless
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
    
    def tearDown(self):
        self.server_thread.terminate()
        self.driver.close()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    
if __name__ == '__main__':
    unittest.main(verbosity=5)
    
    



