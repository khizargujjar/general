import unittest
from webbrowser import browser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
from avanoo.src.features.pages.header import Header
from avanoo.src.features.utilities import driver
from selenium import webdriver

sys.path.append("..")
from utilities import configuration
import time

class SignInPage(Header):

    browser = None
    header = None

    locator_dictionary = {
        "emailField": (By.XPATH, '//*[@id="user_email"]'),
        "password": (By.XPATH, '//*[@id="user_password"]'),
        "signInButton": (By.XPATH, '//*[@id="top-row"]/div[2]/a'),
        "signIn": (By.XPATH, "//button[text()= 'Login']"),
        "LogIn": (By.XPATH, '//*[@id="et-secondary-nav"]/li/a'),
        "journal": (By.XPATH, '//*[@id="wrapper"]/navigation-menu/div/div[1]/div[1]/ul/li[2]/a'),
        "dayOne": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div/div[1]/div/div[1]/div[4]/div[1]/div[4]/div/div[1]/div[1]/div'),
        "commentField": (By.XPATH, '//*[@id="textCommentNew"]'),
        "postComment":(By.XPATH, '//*[@id="btnCommentPost"]'),
        "video": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]'),
        "viewLesson": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[1]/div/div/a'),
        "writeAction": (By.XPATH, '//*[@id="discussion-comment-box"]/div[2]/div[1]/div[1]/div[1]/textarea'),
        "commentBox": (By.XPATH, '//*[@id="textCommentNew"]'),
        "postAction": (By.XPATH, '//*[@id="btnCommentPost"]'),
        "close": (By.XPATH, '//*[@id="discussion-comment-box"]/div[2]/div/div[1]/div[1]/a'),
        "commentDiv": (By.XPATH, '//*[@id="public-reflections"]/div[2]'),
        "edit": (By.XPATH, '//*[@id="public-reflections"]/div[2]/div[1]'),
        "activityFeed": (By.XPATH, '//*[@id="wrapper"]/navigation-menu/div/div[1]/div[1]/ul/li[1]'),
        "addBuddy": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div'),
        "firstBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[1]/div[1]/div[1]/div[3]'),
        "secondBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[2]/div[1]/div[1]/div[3]'),
        "thirdBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[3]/div[1]/div[1]/div[3]'),
        "done":(By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div/div[1]/div[2]')
    }

    def __init__(self, context):
        self.browser = context.browser
        self.header = Header(context)
    
    def get_page_Url(self):
        return str(self.browser.current_url)

    def assertUrl(self, url):
        assert url in self.get_page_Url()

    def selectSignIn(self):
        self.click(self.browser.find_element(*self.locator_dictionary['signIn']))
        time.sleep(3)

    def inputEmail(self, email):
        self.sendKeys(self.browser.find_element(*self.locator_dictionary['emailField']), configuration.get_email(email))

    def inputPassword(self, password):
        self.sendKeys(self.browser.find_element(*self.locator_dictionary['password']), configuration.get_password(password))

    def clickOnJournal(self):
        time.sleep(3)
        self.click(self.browser.find_element(*self.locator_dictionary['journal']))

    def clickOnComment(self):
        time.sleep(3)
        self.click(self.browser.find_element(*self.locator_dictionary['dayOne']))

    def addComment(self, comment):
        self.sendKeys(self.browser.find_element(*self.locator_dictionary['commentField']), comment)

    def postComment(self):
        self.click(self.browser.find_element(*self.locator_dictionary['postComment']))

    def hoverOnVideo(self):
        elem = self.browser.find_element(*self.locator_dictionary['video'])
        hover = ActionChains(driver)
        time.sleep(5)
        hover.move_to_element(elem)
        elem.click()
        # hover.perform()
        time.sleep(4)
        # self.click(self.browser.find_element(*self.locator_dictionary['viewLesson']))

    def writeAction(self, comment):
        obj = self.browser.find_element(*self.locator_dictionary['writeAction'])
        obj.click()
        time.sleep(2)
        close = self.browser.find_element(*self.locator_dictionary['close'])
        close.click()
        obj.click()
        self.sendKeys(self.browser.find_element(*self.locator_dictionary['writeAction']), comment)
        time.sleep(3)

    def postAction(self):
        time.sleep(2)
        self.click(self.browser.find_element(*self.locator_dictionary['postAction']))
        time.sleep(4)

    def clickOnEdit(self):
        div = self.browser.find_element(*self.locator_dictionary['commentDiv'])
        div.click()
        edit = self.browser.find_element(*self.locator_dictionary['edit'])
        hover = ActionChains(driver)
        time.sleep(5)
        hover.move_to_element(edit)
        self.browser.find_element(*self.locator_dictionary['edit']).click()
        time.sleep(5)

    def clickOnActivity(self):
        ele = self.browser.find_element(*self.locator_dictionary['activityFeed'])
        time.sleep(2)
        ele.click()
        time.sleep(2)

    def addBuddy(self):
        elem = self.browser.find_element(*self.locator_dictionary['addBuddy'])
        time.sleep(2)
        elem.click()
        time.sleep(3)

    def addFirstBuddy(self):
        element = self.browser.find_element(*self.locator_dictionary['firstBuddy'])
        time.sleep(2)
        element.click()
        time.sleep(2)

    def verifyBuddy(self, done):
        elements = self.browser.find_elements(*self.locator_dictionary['done'])
        for index in range(0, len(elements)):
            if self.getText(elements[index]) == done:
                break

    def addSecondBuddy(self):
        element = self.browser.find_element(*self.locator_dictionary['secondBuddy'])
        time.sleep(2)
        element.click()
        time.sleep(2)

    def addThirdBuddy(self):
        element = self.browser.find_element(*self.locator_dictionary['thirdBuddy'])
        time.sleep(2)
        element.click()
        time.sleep(2)

    def commentJavaScr(self, comment):
        box = self.browser.find_element(*self.locator_dictionary['commentBox'])
        box.click()
        close = self.browser.find_element(*self.locator_dictionary['close'])
        close.click()
        time.sleep(2)
        box.click()
        obj = self.browser.find_element(*self.locator_dictionary['writeAction'])
        time.sleep(2)
        self.sendKeys(obj, comment)
        time.sleep(3)
