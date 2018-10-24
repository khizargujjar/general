from behave import *

from avanoo.src.features.pages.commonPage import commonPage
from avanoo.src.features.pages.signinpage import SignInPage

use_step_matcher("re")

class commonSteps():
    @given("user is at login page")
    def step_impl(context):
        signinPage = SignInPage(context)
        signinPage.assertUrl("https://pre.avanoo.com/auth/login#/f5e120e5-f/inter")

    @when('user sign in with (?P<email>.+) and "(?P<password>.+)"')
    def step_impl(context, email, password):
         signinPage = SignInPage(context)
         signinPage.inputEmail(email)
         signinPage.inputPassword(password)
         signinPage.selectSignIn()

    @then("user click on journal")
    def step_impl(context):
        journal = SignInPage(context)
        journal.clickOnJournal()

    @step("user click on comment in day 1")
    def step_impl(context):
        comment = SignInPage(context)
        comment.clickOnComment()

    @step('write "(?P<comment>.+)" in comment field')
    def step_impl(context, comment):
        comment = SignInPage(context)
        comment.addComment(comment)

    @step("post this comment")
    def step_impl(context):
        postComment = SignInPage(context)
        postComment.postComment()

    @then("user hover on video of day 1 and click on view lesson and action")
    def step_impl(context):
        hover = SignInPage(context)
        hover.hoverOnVideo()

    @step('write "(?P<action>.+)" in action field')
    def step_impl(context, action):
        object = SignInPage(context)
        object.commentJavaScr(action)

    @step("click on post action button")
    def step_impl(context):
        post = SignInPage(context)
        post.postAction()

    @step("user click on edit button")
    def step_impl(context):
        edit = SignInPage(context)
        edit.clickOnEdit()

    @then("user click on Activity feed")
    def step_impl(context):
        activity = SignInPage(context)
        activity.clickOnActivity()

    @step("click on add a buddy")
    def step_impl(context):
        buddy = SignInPage(context)
        buddy.addBuddy()

    @then("user add first buddy")
    def step_impl(context):
        firstBuddy = SignInPage(context)
        firstBuddy.addFirstBuddy()

    @then("user add second buddy")
    def step_impl(context):
        secondBuddy = SignInPage(context)
        secondBuddy.addSecondBuddy()

    @then("user add third buddy")
    def step_impl(context):
        thirdBuddy = SignInPage(context)
        thirdBuddy.addThirdBuddy()

    @step('verify that it is "(?P<done>.+)" marked')
    def step_impl(context, done):
        verifyFirst = SignInPage(context)
        verifyFirst.verifyBuddy(done)

    @when("user want to edit the action")
    def step_impl(context):
        edit = SignInPage(context)
        edit.clickOnEdit()

    @step('click on "(?P<leftMenu>.+)" from left menu')
    def step_impl(context, leftMenu):
        button = commonPage(context)
        button.clickLeftMenu(leftMenu)
