#From the lecture

from lib2to3.pgen2 import driver
from operator import index
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element,target).perform()


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
    
    



