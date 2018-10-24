from behave import *

from avanoo.src.features.pages.reportsPage import reportsPage
from avanoo.src.features.pages.signinpage import SignInPage
import time

use_step_matcher("re")

class avanooSteps():
    @step("user moves to filter reports page")
    def go_to_page(context):
        reportPage = reportsPage(context)
        reportPage.goToReports()
        time.sleep(5)

    @step("click on Group dropdown to choose group and categories")
    def step_impl(context):
        group = reportsPage(context)
        group.clickOnGroup()

    @then('user choose the "(?P<group>.+)" and "(?P<all>.+)" from dropdowns')
    def step_impl(context, group, all):
        selectGroup = reportsPage(context)
        selectGroup.chooseGroup(group, all)

    @step('user changes the programme to "(?P<program>.+)"')
    def step_impl(context, program):
        programme = reportsPage(context)
        programme.changeProgramme(program)

    @step('verify that "(?P<result>.+)" exist against this request')
    def step_impl(context, result):
        noResult = reportsPage(context)
        noResult.verifyResult(result)

    @step("verify the all number of items")
    def step_impl(context):
        verifyItems = reportsPage(context)
        verifyItems.verifyItems()

    @then("user click on launch date to select time period")
    def step_impl(context):
        date = reportsPage(context)
        date.launchDate()

    @step('select beginning month "(?P<start>.+)" and ending month "(?P<end>.+)"')
    def step_impl(context, start, end):
        date = reportsPage(context)
        date.setDate(start, end)

    @step("hover on a keyword to get details")
    def step_impl(context):
        hover = reportsPage(context)
        hover.hoverOnKeyword()
        hover.getDetailsOfKeyword()

    @step('verify the number of items is "(?P<count>.+)"')
    def step_impl(context, count):
        verifyItems = reportsPage(context)
        verifyItems.verifyItems(count)

    @then("user click on that keyword")
    def step_impl(context):
        job = reportsPage(context)
        job.clickOnKeyword()

    @step('user cancel the "(?P<comment>.+)" comments')
    def step_impl(context, comment):
        cancel = reportsPage(context)
        cancel.clickOnCancel(comment)

    @step("verify the number of actions on that keyword")
    def step_impl(context):
        actions = reportsPage(context)
        actions.verifyActions()

    @step('user select "(?P<group>.+)" from group by filter')
    def step_impl(context, group):
        date = reportsPage(context)
        date.groupby(group)

    # @then('verify "(?P<data>.+)" tag is present on upper side')
    # def step_impl(context, data):
    #     date = reportsPage(context)
    #     date.upperside(data)

    @then('verify "(?P<loadbutton>.+)" button exist')
    def step_impl(context, loadbutton):
        loadMore = reportsPage(context)
        loadMore.load_more_button(loadbutton)

    @then('user selects the "(?P<comment>.+)" comments')
    def step_impl(context, comment):
        select = reportsPage(context)
        select.selectComment(comment)

    @step("verify all the mention comments")
    def step_impl(context):
        mentions = reportsPage(context)
        mentions.verifyMentionsComments()

    @then("verify all positive sentiments")
    def step_impl(context):
        selectGroup = reportsPage(context)
        selectGroup.verifyPositiveComments()

    @then("verify all negative sentiments")
    def step_impl(context):
        selectGroup = reportsPage(context)
        selectGroup.verifyNegativeComments()

    @then("verify all neutral sentiments")
    def step_impl(context):
        selectGroup = reportsPage(context)
        selectGroup.verifyNeutralComments()

    @then("verify all mixed sentiments")
    def step_impl(context):
        mixed = reportsPage(context)
        mixed.verifyMixedComments()
