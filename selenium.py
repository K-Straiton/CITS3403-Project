#From the lecture
from lib2to3.pgen2 import driver
from operator import index
from selenium.webdriver.support.ui import Select

 
#Unittest imports
import os
os.environ['DATABASE_URL'] = 'sqlite://'

from datetime import datetime, timezone, timedelta
import unittest
from app import app, db
import sqlalchemy as sa
from app.models import *

localHost = "http://localhost:5000/"


class SeleniumTests(TestCase):

    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()
        add_test_data_to_db()

        self.server_thread = multiprocessing.Process(target=self.testApp.run)
        self.server_thread.start()

        self.driver = webdriver.Chrome()
        self.driver.get(localHost)

        #Setting it as headless
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
    
    



