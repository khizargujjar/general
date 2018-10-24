from lib2to3.fixes.fix_input import context
from selenium.webdriver.common.by import By
import json, os
from avanoo.src.features.pages.header import Header
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from avanoo.src.features.utilities import driver
import time
import datetime
from array import *
from avanoo.src.features.pages.temporary import *
from random import *

class reportsPage(Header):
    driver = None
    browser = None

    Locator_click_buttons = {
        "groupAllDropdown": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[3]/a[1]'),
        "groupDropdown": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[3]/div/div/div/div[1]/div/button'),
        "groupsList": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[3]/div/div/div/div[1]/div/ul/li'),
        "allDropdown": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[3]/div/div/div/div[2]/div/button'),
        "allList": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[3]/div/div/div/div[2]/div/ul/li'),
        "mentions": (By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/p[1]'),
        "positive": (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/p[1]'),
        "neutral": (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/p[2]'),
        "negative": (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/p[3]'),
        "mixed": (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/p[4]'),
        "reflection": (By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/p[1]'),
        "action": (By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/p[2]'),
        "cancelPositive": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/ul/li[1]/a/span[2]'),
        "cancelNeutral": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/ul/li[2]/a/span[2]'),
        "cancelNegative": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/ul/li[3]/a/span[2]'),
        "cancelMixed": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/ul/li[4]/a/span[2]'),
        "verifyMixed": (By.XPATH, "html/body/div[2]/div/div/div/div[5]/div/div[2]/div[3]/div[2]/comment-list/div/div[1]/div"),
        "program": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[2]/a'),
        "programFilter": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[2]/div/div/div/button'),
        "programsList": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[2]/div/div/div/ul/li/a'),
        "noResults": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[2]/div[2]/div[1]/div/div/p[1]'),
        "allItems": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[1]/ul/li[1]/a/div/span[4]'),
        "launchDate": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[4]/a[2]'),
        "begin": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[4]/div[2]/div/div[1]/div[2]/div'),
        "beginDate": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[4]/div[2]/div/div[1]/div[2]/div/ul[1]/li'),
        "end": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div'),
        "endDate": (By.XPATH, '/html/body/div[2]/div/div/div/div[4]/filter-config/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/ul[1]/li'),
        "jobMentions": (By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/p[1]'),
        "jobPositive": (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/p[1]'),
        "jobNeutral": (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/p[2]'),
        "jobNegative": (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/p[3]'),
        "jobMixed": (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/p[4]'),
        "keyword": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[2]/div[2]/div[2]/word-cloud/div/div/span'),
        "allSentiments": (By.XPATH, 'html/body/div[2]/div/div/div/div[5]/div/div[2]/div[3]/div[2]/comment-list/div/div[1]/div'),
        "actions": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[2]/div[3]/div[2]/comment-list/div/div/div/div/div[3]/span[1]'),
        "groupby": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[1]/div/button/span[3]'),
        "grouplist": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[1]/div/ul/li[2]/a'),
        "loadmore": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[2]/div[3]/div[2]/pagination/div/div/button'),
        "clickPositive": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/ul/li[1]/a/span[1]'),
        "clickNeutral": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/ul/li[2]/a/span[1]'),
        "clickNegative": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/ul/li[3]/a/span[1]'),
        "clickMixed": (By.XPATH, '/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/ul/li[4]/a/span[1]')
    }

    def goToReports(self):
            self.browser.get("https://pre.avanoo.com/report/#/f5e120e5-f/inter")
            return str(self.browser.current_url) == "https://pre.avanoo.com/report/#/f5e120e5-f/inter"
            time.sleep(8)

    def clickOnGroup(self):
        self.click(self.browser.find_element(*self.Locator_click_buttons['groupAllDropdown']))
        time.sleep(3)

    def chooseGroup(self, groupName, all):
        self.click(self.browser.find_element(*self.Locator_click_buttons['groupDropdown']))
        groups = self.browser.find_elements(*self.Locator_click_buttons['groupsList'])
        for i in range(0, len(groups)):
            if self.getText(groups[i]) == groupName:
                groups[i].click()
        time.sleep(2)

        self.click(self.browser.find_element(*self.Locator_click_buttons['allDropdown']))
        allList = self.browser.find_elements(*self.Locator_click_buttons['allList'])
        for index in range(0, len(allList)):
            if self.getText(allList[index]) == all:
                self.click(allList[index])
        time.sleep(2)

    def verifyItems(self, count):
        time.sleep(1)
        value = self.getText(self.browser.find_element(*self.Locator_click_buttons['allItems']))
        assert value == count

    def clickOnCancel(self, comment):
        time.sleep(1)
        if comment == "Positive":
            self.click(self.browser.find_element(*self.Locator_click_buttons['cancelPositive']))
        elif comment == "Neutral":
            time.sleep(2)
            self.click(self.browser.find_element(*self.Locator_click_buttons['cancelNeutral']))
        elif comment == "Negative":
            time.sleep(2)
            self.click(self.browser.find_element(*self.Locator_click_buttons['cancelNegative']))
        elif comment == "Mixed":
            time.sleep(2)
            self.click(self.browser.find_element(*self.Locator_click_buttons['cancelMixed']))
        time.sleep(1)

    def changeProgramme(self, filter):
        self.click(self.browser.find_element(*self.Locator_click_buttons['program']))
        self.click(self.browser.find_element(*self.Locator_click_buttons['programFilter']))
        programs = self.browser.find_elements(*self.Locator_click_buttons['programsList'])
        for i in range(0, len(programs)):
            if self.getText(programs[i]) == filter:
                programs[i].click()
        time.sleep(3)

    def verifyResult(self, result):
        value = self.browser.find_element(*self.Locator_click_buttons['noResults'])
        a = self.getText(value)
        assert self.getText(value) == result

    def launchDate(self):
        self.click(self.browser.find_element(*self.Locator_click_buttons['launchDate']))

    def setDate(self, start, end):
        self.click(self.browser.find_element(*self.Locator_click_buttons['begin']))
        startdate = (self.browser.find_elements(*self.Locator_click_buttons['beginDate']))
        for i in range(0, len(startdate)):
            if self.getText(startdate[i]) == start:
                startdate[i].click()
        time.sleep(2)

        self.click(self.browser.find_element(*self.Locator_click_buttons['end']))
        endDate = (self.browser.find_elements(*self.Locator_click_buttons['endDate']))
        for i in range(0, len(endDate)):
            if self.getText(endDate[i]) == end:
                endDate[i].click()
        time.sleep(2)

    def hoverOnKeyword(self):
        keywords = self.browser.find_elements(*self.Locator_click_buttons['keyword'])
        time.sleep(2)
        i = randint(1, 22)
        for index in range(0, len(keywords)):
            if index == i:
                set_random(i)
                ActionChains(self.browser).move_to_element(keywords[index]).perform()
        time.sleep(1)

    def getDetailsOfKeyword(self):
        time.sleep(2)
        mentions = self.getText(self.browser.find_element(*self.Locator_click_buttons['jobMentions']))
        positive = self.getText(self.browser.find_element(*self.Locator_click_buttons['jobPositive']))
        neutral = self.getText(self.browser.find_element(*self.Locator_click_buttons['jobNeutral']))
        negative = self.getText(self.browser.find_element(*self.Locator_click_buttons['jobNegative']))
        mixed = self.getText(self.browser.find_element(*self.Locator_click_buttons['jobMixed']))
        reflection = self.getText(self.browser.find_element(*self.Locator_click_buttons['reflection']))
        action = self.getText(self.browser.find_element(*self.Locator_click_buttons['action']))
        a, b = positive.split(' ')
        c, d = neutral.split(' ')
        e, f = negative.split(' ')
        g, h = mixed.split(' ')
        i, j = reflection.split(' ')
        k, l = action.split(' ')
        array1 = [a, c, e, g, i, k, mentions]
        set_keywordArray(array1)
        time.sleep(1)

    def clickOnKeyword(self):
        keyword = self.browser.find_elements(*self.Locator_click_buttons['keyword'])
        for index in range(0, len(keyword)):
            if index == temp.random:
                self.click(keyword[index])
        time.sleep(2)

    def selectComment(self, comment):
        time.sleep(1)
        if comment == "Positive":
            self.click(self.browser.find_element(*self.Locator_click_buttons['clickPositive']))
        elif comment == "Neutral":
            time.sleep(1)
            self.click(self.browser.find_element(*self.Locator_click_buttons['clickNeutral']))
        elif comment == "Negative":
            time.sleep(1)
            self.click(self.browser.find_element(*self.Locator_click_buttons['clickNegative']))
        elif comment == "Mixed":
            time.sleep(1)
            self.click(self.browser.find_element(*self.Locator_click_buttons['clickMixed']))
        time.sleep(1)

    def groupby(self, group):
        self.click(self.browser.find_element(*self.Locator_click_buttons['groupby']))
        grouplist = self.browser.find_elements(*self.Locator_click_buttons['grouplist'])
        for i in range(0, len(grouplist)):
            if self.getText(grouplist[i]) == group:
                grouplist[i].click()
        time.sleep(5)

    def load_more_button(self, loadbutton):
        button = self.browser.find_element(*self.Locator_click_buttons['loadmore'])
        for x in range(1, 20):
            if self.getText(button) == loadbutton:
                self.click(button)
                time.sleep(2)

    def verifyActions(self):
        count = 0
        actions = self.browser.find_elements(*self.Locator_click_buttons['actions'])
        for i in range(0, len(actions)):
            if self.getText(actions[i]) == "Action":
                count = count + 1
        time.sleep(3)
        assert count == int(temp.arrayKeyword[5])

    def verifyMentionsComments(self):
        time.sleep(1)
        allMentions = self.browser.find_elements(*self.Locator_click_buttons['allSentiments'])
        mentions = int(temp.arrayKeyword[6])
        time.sleep(2)
        assert mentions == len(allMentions)

    def verifyPositiveComments(self):
        allPositive = self.browser.find_elements(*self.Locator_click_buttons['allSentiments'])
        positive = int(temp.arrayKeyword[0])
        assert positive == len(allPositive)

    def verifyNegativeComments(self):
        allNegative = self.browser.find_elements(*self.Locator_click_buttons['allSentiments'])
        negative = int(temp.arrayKeyword[2])
        assert negative == len(allNegative)

    def verifyNeutralComments(self):
        allNeutral = self.browser.find_elements(*self.Locator_click_buttons['allSentiments'])
        neutral = int(temp.arrayKeyword[1])
        assert neutral == len(allNeutral)

    def verifyMixedComments(self):
        allMixed = self.browser.find_elements(*self.Locator_click_buttons['allSentiments'])
        mixed = int(temp.arrayKeyword[3])
        assert mixed == len(allMixed)