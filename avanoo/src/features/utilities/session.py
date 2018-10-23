from utilities import configuration
from selenium import webdriver
from enum import Enum

class Stage(Enum):
	step = 1
	feature = 2
	scenario = 3
	lifetime = 4

desiredclearance = configuration.get_setting("selenium", "clear_cookies")

def clear_cookies_if_required(entity_type, context):
	if entity_type == Stage[desiredclearance]:
		context.browser.delete_all_cookies()
		print("deleting cookies")
	
		
		