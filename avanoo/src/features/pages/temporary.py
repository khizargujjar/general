from selenium.webdriver.common.by import By
import json, os
from avanoo.src.features.pages.header import Header
from selenium.webdriver.support.ui import Select
from avanoo.src.features.utilities import driver
from array import *

class temporary():
    def __init__(self):
        self.arrayKeyword = []
        self.random = 0

temp = temporary()

def set_keywordArray(arr2):
    temp.arrayKeyword = arr2

def set_random(rand):
    temp.random = rand