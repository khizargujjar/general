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

class groupStatsPage(Header):
    driver = None
    browser = None

    Locator_groupStats_buttons = {
        "program": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[2]/a'),
        "programFilter": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[2]/div/div/div'),
        "programsList": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[2]/div/div/div/ul/li/a'),
        "groupAllDropdown": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[3]/a[1]'),
        "groupDropdown": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[3]/div/div/div/div[1]/div/button'),
        "groupsList": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[3]/div/div/div/div[1]/div/ul/li/a'),
        "subGroup": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[3]/div/div/div/div[2]/div/button'),
        "subGroupsList": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[3]/div/div/div/div[2]/div/ul/li/a'),
        "launchDate": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[4]/a[2]'),
        "begin": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[4]/div[2]/div/div[1]/div[2]/div/button'),
        "beginDate": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[4]/div[2]/div/div[1]/div[2]/div/ul/li/a'),
        "end": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/button'),
        "endDate": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/filter-config/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/ul/li/a'),
        "columnNames": (By.XPATH, '//*[@id="tblTeamStatsData"]/thead/tr/th/span'),
        "editColumn": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/button'),
        "firstColumn": (By.XPATH, '//*[@id="teamStatsColumns"]/div/div/div[2]/div[2]/div/table/tbody/tr/td[2]'),
        "saveChanges": (By.XPATH, '//*[@id="teamStatsColumns"]/div/div/div[3]/button[2]'),
        "checkboxes": (By.XPATH, '//*[@id="teamStatsColumns"]/div/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div'),
        "row": (By.XPATH, '//*[@id="tblTeamStatsData"]/tbody/tr/td/p[1]'),
        "data": (By.XPATH, '//*[@id="tblTeamStatsData"]/tbody/tr/td'),
        "corporateRow": (By.XPATH, '//*[@id="tblTeamStatsData"]/tbody/tr[3]/td/p[1]'),
        "corporateData": (By.XPATH, '//*[@id="tblTeamStatsData"]/tbody/tr[3]/td')
    }

    def changeProgramme(self, filter):
        time.sleep(3)
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['program']))
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['programFilter']))
        programs = self.browser.find_elements(*self.Locator_groupStats_buttons['programsList'])
        for i in range(0, len(programs)):
            if self.getText(programs[i]) == filter:
                programs[i].click()
        time.sleep(2)

    def clickOnGroup(self):
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['groupAllDropdown']))
        time.sleep(3)

    def chooseGroup(self, groupName, all):
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['groupDropdown']))
        groups = self.browser.find_elements(*self.Locator_groupStats_buttons['groupsList'])
        for i in range(0, len(groups)):
            if self.getText(groups[i]) == groupName:
                groups[i].click()
        time.sleep(1)
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['subGroup']))
        subGroups = self.browser.find_elements(*self.Locator_groupStats_buttons['subGroupsList'])
        for index in range(0, len(subGroups)):
            if self.getText(subGroups[index]) == all:
                self.click(subGroups[index])
        time.sleep(2)

    def launchDate(self):
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['launchDate']))

    def setDate(self, start, end):
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['begin']))
        startdate = (self.browser.find_elements(*self.Locator_groupStats_buttons['beginDate']))
        for i in range(0, len(startdate)):
            if self.getText(startdate[i]) == start:
                startdate[i].click()
        time.sleep(1)
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['end']))
        endDate = (self.browser.find_elements(*self.Locator_groupStats_buttons['endDate']))
        for i in range(0, len(endDate)):
            if self.getText(endDate[i]) == end:
                endDate[i].click()
        time.sleep(2)

    def verifyColumnExist(self, column):
        columns = (self.browser.find_elements(*self.Locator_groupStats_buttons['columnNames']))
        for i in range(0, len(columns)):
            if self.getText(columns[i]) == column:
                assert self.getText(columns[i]) == column
        time.sleep(1)

    def editColumn(self):
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['editColumn']))

    def selectGroup(self, group):
        time.sleep(1)
        groups = self.browser.find_elements(*self.Locator_groupStats_buttons['firstColumn'])
        for i in range(0, len(groups)):
            if self.getText(groups[i]) == group:
                self.click(groups[i])
        # time.sleep(1)

    def selectColumn(self, column):
        columns = self.browser.find_elements(*self.Locator_groupStats_buttons['firstColumn'])
        checkboxes = self.browser.find_elements(*self.Locator_groupStats_buttons['checkboxes'])
        for i in range(0, len(columns)):
            if self.getText(columns[i]) == column:
                if self.getAttributes(checkboxes[i], 'class') == "icheckbox_square-blue checked":
                    self.click(columns[i])
        time.sleep(1)

    def saveChanges(self):
        self.click(self.browser.find_element(*self.Locator_groupStats_buttons['saveChanges']))
        time.sleep(1)

    def verifyColumnNotExist(self, column):
        columns = (self.browser.find_elements(*self.Locator_groupStats_buttons['columnNames']))
        for i in range(0, len(columns)):
            if self.getText(columns[i]) != column:
                continue
        time.sleep(1)

    def verifyRow(self, row):
        time.sleep(2)
        rows = self.browser.find_elements(*self.Locator_groupStats_buttons['row'])
        for i in range(0, len(rows)):
            if self.getText(rows[i]) == row:
                assert self.getText(rows[i]) == row

    def checkData(self, row):
        array2 = []
        rows = self.browser.find_elements(*self.Locator_groupStats_buttons['data'])
        for i in range(0, len(rows)):
            if self.getText(rows[i]) == row:
                for j in range(0, 16):
                    array2.insert(j, self.getText(rows[i + j + 1]))
                set_arrayData(array2)

        time.sleep(1)

    def verifyData(self, row):
        array3 = []
        rows = self.browser.find_elements(*self.Locator_groupStats_buttons['data'])
        for i in range(0, len(rows)):
            if self.getText(rows[i]) == row:
                for j in range(0, 16):
                    array3.insert(j, self.getText(rows[i + j + 1]))
                # set_arrayData(array3)
        assert temp.arrayData != array3
        time.sleep(1)

    def selectCheckbox(self, engagement, interaction):
        columns = self.browser.find_elements(*self.Locator_groupStats_buttons['firstColumn'])
        checkboxes = self.browser.find_elements(*self.Locator_groupStats_buttons['checkboxes'])
        for i in range(0, len(columns)):
            if self.getText(columns[i]) == engagement:
                if self.getAttributes(checkboxes[i], 'class') == "icheckbox_square-blue":
                    self.click(columns[i])
                    self.click(columns[i])
        time.sleep(1)
        for j in range(0, len(columns)):
            if self.getText(columns[j]) == interaction:
                if self.getAttributes(checkboxes[j], 'class') == "icheckbox_square-blue":
                    self.click(columns[j])
                    self.click(columns[j])
        time.sleep(1)