#Imports from the lecture
import multiprocessing
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from unittest import TestCase
from app.helper import add_dummy_data

#Imports for unittests
import unittest
from app import create_app, db
import sqlalchemy as sa
from unittest import TestCase
from app.config import TestConfig
from app.models import User, Post, Comments


loginurl = "http://localhost:5000/login"
homepage = "http://localhost:5000"

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()
        time.sleep(1) 
        self.driver = webdriver.Chrome()
        self.driver.get(homepage)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.server_process.terminate()
        self.driver.close()
        self.driver.quit()

    # #Test new post as unauthenticated
    # def test_new_post_unauthenticated(self):
    #     #create user
    #     newpostElement = self.driver.find_element(By.ID, "newpost")
    #     newpostElement.click()
    #     TitleElement = self.driver.find_element(By.ID, "newPostTitleInput")
    #     TitleElement.send_keys("Titletest")
    #     BodyElement = self.driver.find_element(By.ID, "newPostBodyInput")
    #     BodyElement.send_keys("BodyTest")
    #     time.sleep(3)
    #     PostButton = self.driver.find_element(By.ID, "submit")
    #     PostButton.click()
        
    #     self.assertEqual(self.driver.current_url, "http://localhost:5000/login")
    #     time.sleep(3)
    
    #Test wrong nonexistant test
    def test_nonexistant_user(self):
        #create user
        self.driver.get(loginurl)
        time.sleep(3)
        usernameElement = self.driver.find_element(By.ID, "usernameInput")
        usernameElement.send_keys("test1")
        passwordElement = self.driver.find_element(By.ID, "passwordInput")
        passwordElement.send_keys("cat")
        time.sleep(3)
        submitElement = self.driver.find_element(By.ID, "logIn")
        submitElement.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login")
        time.sleep(3)

    def test_search(self):
            time.sleep(5)
            searchbox = self.driver.find_element(By.ID, "textToSearch")
            searchbox.send_keys("X13")
            searchbutton = self.driver.find_element(By.ID, "submitSearch")
            searchbutton.click()
            endofsearchtext = self.driver.find_element(By.ID, "endofsearch")
            self.assertNotNull(endofsearchtext)

    def test_signuplink(self):
        signup = self.driver.find_element(By.ID, "signuplink")
        signup.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/sign-up")
    
    def test_loginlink(self):
        login = self.driver.find_element(By.ID, "loginlink")
        login.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login")
    
    def test_thinkmadhome(self):
        thinkmad = self.driver.find_element(By.ID, "ThinkMad-logo")
        thinkmad.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login")
    
    def test_signup_button(self):
        signupbutton = self.driver.find_element(By.ID, "signupbutton")
        signupbutton.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/sign-up")

    def test_wrong_email_signup(self):
        usernamefield = self.driver.find_element(By.ID, "signUpUsername")
        usernamefield.send_keys("sersangy")
        emailfield = self.driver.find_element(By.ID, "signUpEmail")
        emailfield.send_keys("sersanggmail.com")
        passwordfield = self.driver.find_element(By.ID, "signUpPassword")
        passwordfield.send_keys("password")
        confirmpasswordfield = self.driver.find_element(By.ID, "signUpConfirmPassword")
        confirmpasswordfield.send_keys("password")
        pronouns = self.driver.find_element(By.ID, "pronouns-0")
        pronouns.click()
        time.sleep(4)
        signupbutton = self.driver.find_element(By.ID, "signUp")
        signupbutton.click()

        self.assertEqual(self.driver.current_url, "http://localhost:5000/sign-up")

    def test_wrong_confirmpassword_signup(self):
        usernamefield = self.driver.find_element(By.ID, "signUpUsername")
        usernamefield.send_keys("sersangy")
        emailfield = self.driver.find_element(By.ID, "signUpEmail")
        emailfield.send_keys("sersang@gmail.com")
        passwordfield = self.driver.find_element(By.ID, "signUpPassword")
        passwordfield.send_keys("password")
        confirmpasswordfield = self.driver.find_element(By.ID, "signUpConfirmPassword")
        confirmpasswordfield.send_keys("wrongconfirmpassword")
        pronouns = self.driver.find_element(By.ID, "pronouns-0")
        pronouns.click()
        time.sleep(4)
        signupbutton = self.driver.find_element(By.ID, "signUp")
        signupbutton.click()
        
        self.assertEqual(self.driver.current_url, "http://localhost:5000/sign-up")







 
    

    



