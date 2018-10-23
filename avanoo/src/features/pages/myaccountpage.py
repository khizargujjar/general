import unittest
from selenium.webdriver.common.by import By
import sys
from avanoo.src.features.pages.header import Header
sys.path.append("..")

class MyAccount(Header):

    browser = None

    locator_dictionary = {
    }

    def __init__(self, context):
        self.browser = context.browser