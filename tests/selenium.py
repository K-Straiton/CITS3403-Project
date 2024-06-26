#Imports from the lecture
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestCase

#Imports for unittests
from app import create_app, db
import sqlalchemy as sa
from unittest import TestCase
from app.config import TestConfig

loginurl = "http://localhost:5000/login"
homepage = "http://localhost:5000"
signuppage = "http://localhost:5000/sign-up"

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(homepage)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.server_process.terminate()
        self.driver.close()

    #Test wrong nonexistant test
    def test_nonexistant_user(self):
        self.driver.get(loginurl)
        usernameElement = self.driver.find_element(By.ID, "usernameInput")
        usernameElement.send_keys("test1")
        passwordElement = self.driver.find_element(By.ID, "passwordInput")
        passwordElement.send_keys("cat")
        submitElement = self.driver.find_element(By.ID, "logIn")
        submitElement.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login")

    def test_search(self):
        self.driver.get(homepage)
        searchbox = self.driver.find_element(By.ID, "textToSearch")
        searchbox.send_keys("X13")
        searchbutton = self.driver.find_element(By.ID, "submitSearch")
        searchbutton.click()
        endofsearchtext = self.driver.find_element(By.ID, "endofsearch")
        self.assertTrue(endofsearchtext!=None)

    def test_signuplink(self):
        self.driver.get(homepage)
        signup = self.driver.find_element(By.ID, "signuplink")
        signup.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/sign-up")

    def test_loginlink(self):
        self.driver.get(homepage)
        login = self.driver.find_element(By.ID, "loginlink")
        login.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/login")

    def test_thinkmadhome(self):
        self.driver.get(homepage)
        thinkmad = self.driver.find_element(By.ID, "ThinkMad-logo")
        thinkmad.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/")

    def test_signup_button(self):
        self.driver.get(homepage)
        signupbutton = self.driver.find_element(By.ID, "signuplink")
        signupbutton.click()
        self.assertEqual(self.driver.current_url, "http://localhost:5000/sign-up")

    def test_wrong_email_signup(self):
        self.driver.get(signuppage)
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
        signupbutton = self.driver.find_element(By.ID, "signUp")
        signupbutton.click()

        self.assertEqual(self.driver.current_url, "http://localhost:5000/sign-up")

    def test_wrong_confirmpassword_signup(self):
        self.driver.get(signuppage)
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
        signupbutton = self.driver.find_element(By.ID, "signUp")
        signupbutton.click()

        self.assertEqual(self.driver.current_url, "http://localhost:5000/sign-up")

