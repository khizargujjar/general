from behave import *

from avanoo.src.features.pages.avanooPage import corporatePage
from avanoo.src.features.pages.signinpage import SignInPage

use_step_matcher("re")

class avanooSteps():
    @step("user moves to get started page")
    def go_to_page(context):
        getstartedPage = corporatePage(context)
        getstartedPage.goToCorporatePage()

    @step('click on "(?P<getStarted>.+)" button')
    def step_impl(context, getStarted):
        getStartedButton = corporatePage(context)
        getStartedButton.click_on_button(getStarted)

    @then("user click on one of the trees")
    def step_impl(context):
        trees = corporatePage(context)
        trees.clickOnTree()

    @step("click on menu and verify left bar")
    def step_impl(context):
        menu = corporatePage(context)
        menu.clickOnMenu()
        menu.verifyLeftBar()

    @step("play the video")
    def step_impl(context):
        play = corporatePage(context)
        play.playVideo()

    @then("user rate the video")
    def step_impl(context):
        rate = corporatePage(context)
        rate.rateVideo()
        # rate.download_certificate()

    @then("verify the name and date on certificate")
    def step_impl(context):
        verifyCertificate = corporatePage(context)
        verifyCertificate.verify_certificate()
        verifyCertificate.download_certificate()
