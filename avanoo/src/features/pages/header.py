from avanoo.src.features.pages.basepage import basePage
from selenium.webdriver.common.by import By
import json, os


class Header(basePage):
    browser = None

    locator_dictionary_header = {
    }

    def __init__(self, context):
        self.browser = context.browser