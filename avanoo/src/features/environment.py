from utilities import screenshot
from utilities import configuration
from utilities import driver
from utilities import session
from pages.basepage import *


def before_step(context, step):
    pass

def after_step(context, step):
    session.clear_cookies_if_required(session.Stage.step, context)
    if step.status == "failed":
        print("step failed")

def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    session.clear_cookies_if_required(session.Stage.scenario, context)
    if scenario.status == "failed":
        screenshot.capture_failure(context, scenario)

def before_feature(context, feature):
    pass

def after_feature(context, feature):
    session.clear_cookies_if_required(session.Stage.feature, context)
    pass

def before_all(context):
    browsertype = configuration.get_browser()
    context.browser = driver.switch_browser(browsertype)
    context.browser.maximize_window()
    context.browser.get("https://pre.avanoo.com/auth/login#/f5e120e5-f/inter")

def after_all(context):
    basepage = basePage(context)
    basepage.remove_download_files()
    context.browser.quit()
