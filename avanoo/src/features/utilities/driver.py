from .browsers import Browsers 
from utilities import configuration
import os
from selenium import webdriver

def get_chrome():
    chromedriver = configuration.read_chromedriver_location()
    chromeOptions = webdriver.ChromeOptions()
    cwd = os.getcwd()
    prefs = {"download.default_directory": cwd+"\\downloads", "download.prompt_for_download": False}
    chromeOptions.add_experimental_option("prefs", prefs)
    os.environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
    
def get_ie():
    iedriver = configuration.read_internetexplorer_location()
    os.environ["webdriver.ie.driver"] = iedriver
    return webdriver.Ie(iedriver)
    
def switch_browser(browser):
    return {
        Browsers.chrome : get_chrome,
        Browsers.internetexplorer : get_ie
    }.get(browser, lambda: webdriver.Firefox())()