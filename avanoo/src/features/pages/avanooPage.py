from selenium.webdriver.common.by import By
import json, os
from avanoo.src.features.pages.header import Header
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from random import *

class corporatePage(Header):
    driver = None
    browser = None

    Locator_corporate_buttons = {
        "getStarted": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[2]/div/div/div[2]/button'),
        "tree1": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/ul/li[1]'),
        "tree2": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/ul/li[2]'),
        "tree3": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/ul/li[3]'),
        "tree4": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/ul/li[4]'),
        "tree5": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/ul/li[5]'),
        "playButton": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[2]/span/img'),
        "menu": (By.XPATH, '/html/body/div[2]/a'),
        "checkIn": (By.XPATH, 'html/body/div[3]/navigation-menu/div/div/div[1]/ul/li'),
        "rate": (By.XPATH, '//*[@id="video-complete-modal"]/div/div/div[1]/div[1]/div[5]/ul[1]/li[7]'),
        "nameOnCertificate": (By.XPATH, '//*[@id="video-complete-modal"]/div/div/div[1]/div[3]/div[1]/div[1]/div[2]'),
        "dateOnCertificate": (By.XPATH, '//*[@id="video-complete-modal"]/div/div/div[1]/div[3]/div[1]/div[1]/div[5]'),
        "download": (By.XPATH, '//*[@id="video-complete-modal"]/div/div/div[1]/div[3]/div[2]/a'),
        "close": (By.XPATH, '//*[@id="video-complete-modal"]/div/div/div[1]/div[3]/div[3]')
    }

    def goToCorporatePage(self):
        self.browser.get("https://pre-artemiy.avanoo.com//pdtest_generic/13748/fbd1f075d8ce4b22b4ed521c7919b0cb/1171125/wipe_info,self_growth_18,day18c")
        return str(self.browser.current_url) == "https://pre-artemiy.avanoo.com//pdtest_generic/13748/fbd1f075d8ce4b22b4ed521c7919b0cb/1171125/wipe_info,self_growth_18,day18c"
        time.sleep(5)

    def click_on_button(self, button):
        if button == "Get Started":
            self.click(self.browser.find_element(*self.Locator_corporate_buttons['getStarted']))
            time.sleep(5)

    def clickOnTree(self):
        i = randint(1, 5)
        if i == 1:
            self.click(self.browser.find_element(*self.Locator_corporate_buttons['tree1']))
            time.sleep(5)
        elif i == 2:
            self.click(self.browser.find_element(*self.Locator_corporate_buttons['tree2']))
            time.sleep(5)
        elif i == 3:
            self.click(self.browser.find_element(*self.Locator_corporate_buttons['tree3']))
            time.sleep(5)
        elif i == 4:
            self.click(self.browser.find_element(*self.Locator_corporate_buttons['tree4']))
            time.sleep(5)
        elif i == 5:
            self.click(self.browser.find_element(*self.Locator_corporate_buttons['tree5']))
            time.sleep(5)

    def clickOnMenu(self):
        self.click(self.browser.find_element(*self.Locator_corporate_buttons['menu']))
        time.sleep(3)

    def verifyLeftBar(self):
        elem = self.browser.find_elements(*self.Locator_corporate_buttons['checkIn'])
        self.getText(elem[0]) == "Check-In"
        self.getText(elem[1]) == "Watch"
        self.getText(elem[2]) == "Act"
        self.getText(elem[3]) == "Track Progress"
        self.getAttributes(elem[0], 'class') == "checkin no-hover"
        self.getAttributes(elem[1], 'class') == "watch no-hover active"
        self.getAttributes(elem[2], 'class') == "act no-hover"
        self.getAttributes(elem[3], 'class') == "track-progress no-hover"

    def playVideo(self):
        self.click(self.browser.find_element(*self.Locator_corporate_buttons['playButton']))
        time.sleep(15)

    def rateVideo(self):
        self.click(self.browser.find_element(*self.Locator_corporate_buttons['rate']))
        time.sleep(5)

    def download_certificate(self):
        self.click(self.browser.find_element(*self.Locator_corporate_buttons['download']))
        time.sleep(10)
        self.click(self.browser.find_element(*self.Locator_corporate_buttons['close']))
        time.sleep(3)

    def verify_certificate(self):
        name = self.browser.find_element(*self.Locator_corporate_buttons['nameOnCertificate'])
        date = self.browser.find_element(*self.Locator_corporate_buttons['dateOnCertificate'])
        n = self.getText(name)
        d = self.getText(date)
