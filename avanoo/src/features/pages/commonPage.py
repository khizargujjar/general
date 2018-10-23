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


class commonPage(Header):
    driver = None
    browser = None

    Locator_common_buttons = {
        "groupStat": (By.XPATH, '/html/body/div[1]/div/div/ul/li[5]/a'),
    }

    def clickLeftMenu(self, button):
        if button == "Group Stats":
            self.click(self.browser.find_element(*self.Locator_common_buttons['groupStat']))
            time.sleep(2)
