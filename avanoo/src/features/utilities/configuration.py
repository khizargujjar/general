import configparser
import os
import sys
import platform
from .browsers import Browsers

projectRoot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class QA_Params(object):
    def __init__(self):
        self.company_no = None

qa_params = QA_Params()

def is_64bit():
    return sys.maxsize > 2**32

def getConfig():
    configFilePath = os.path.join(projectRoot, "src", "config.ini")
    configParser = configparser.RawConfigParser()
    configParser.read(configFilePath)
    return configParser

config = getConfig()

def get_setting(parent, key):
    return config.get(parent, key)

def get_browser():
    return Browsers.get_browser(get_setting("selenium", "driver"))
    
def read_chromedriver_location():
    return os.path.join(projectRoot, "lib", get_chromedriver())

def read_internetexplorer_location():
    return os.path.join(projectRoot, "lib", "IEDriverServer.exe")
    
def is_windows():
    return platform.system().lower() == "windows"
    
def is_linux():
    return platform.system().lower() == "linux"
    
def get_chromedriver():
    # return "chromedriver.exe" if is_windows() else "chromedriver64" if is_64bit() else "chromedriver"
    return "chromedriver.exe" if is_windows() else "chromedriver"

def get_email(email):
    email_without_no = get_setting("data", email)
    # email_without_no = email_without_no.replace("XXX", get_company_no())
    return email_without_no

def get_password(password):
    return get_setting("data", password)

def get_url(url):
    return get_setting("URL", url)

def set_company_no(value):
    qa_params.company_no = value

def get_company_no():
    return qa_params.company_no