#Imports from the lecture
import multiprocessing
import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from unittest import TestCase

#Imports for unittests
import unittest
from app import create_app, db
import sqlalchemy as sa
from unittest import TestCase
from app.config import TestConfig
from app.models import *


localHost = "http://localhost:5000/"

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.server_process.terminate()
        self.driver.close()

    def test_login_page(self):
        time.sleep(10) 
        self.assertTrue(True)

    

    



