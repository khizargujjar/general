from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

class basePage:

    locator_dictionary_button = {
        "loader": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]')
    }

    def __init__(self, context):
        self.browser = context.browser

    def click(self, element):
        try:
            element.click()
        except:
            try:
                time.sleep(2)
                self.wait = WebDriverWait(self.browser, 10)
                self.wait.until(EC.element_to_be_clickable(element))
                element.click()
            except:
                ActionChains(self.browser).move_to_element(element).perform()
                time.sleep(3)
                element.click()

    def sendKeys(self, element, strKeys):
        try:
            element.send_keys(strKeys)
        except NoSuchElementException:
            self.wait = WebDriverWait(self.browser, 10)
            self.wait.until(EC.visibility_of_element_located(element))
            element.send_keys(strKeys)

    def getText(self, element):
        try:
            return element.text
        except NoSuchElementException:
            self.wait = WebDriverWait(self.browser, 10)
            self.wait.until(EC.visibility_of_element_located(element))
            return element.text

    def getValue(self, element):
        try:
            element.get_value()
        except:
            self.wait = WebDriverWait(self.browser, 10)
            self.wait.until(EC.visibility_of_element_located(element))
            element.getValue()

    def isElementDisplayed(self, element):
        self.wait = WebDriverWait(self.browser, 10)
        self.wait.until(EC.visibility_of(element))
        return element.is_displayed()

    def getAttributes(self, element, attributes):
        return element.get_attribute(attributes)

    def get_download_file(self, fileName):
        cwd = os.getcwd()
        downloadfolder = cwd+"\\downloads\\"
        return os.path.isfile(downloadfolder + fileName)

    def remove_download_files(self):
        cwd = os.getcwd()
        downloadfolder = cwd + "\\downloads\\"
        fileList = os.listdir(downloadfolder)
        for fileName in fileList:
            os.remove(downloadfolder + "\\" + fileName)

    # def wait_till_loading(self):
    #     loading = self.browser.find_element(*self.locator_dictionary_button['loader'])
    #     try:
    #         if self.getAttributes(loading, 'class') == "zero-state loading":
    #             return
    #     # except:
    #


