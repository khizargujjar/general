from behave import *
from avanoo.src.features.pages.groupStatsPage import groupStatsPage
from avanoo.src.features.pages.signinpage import SignInPage
import time

use_step_matcher("re")

class groupSteps():
    @step('user selects program "(?P<program>.+)"')
    def step_impl(context, program):
        selectProgram = groupStatsPage(context)
        selectProgram.changeProgramme(program)

    @step("click on Group dropdown to select group and subgroup")
    def step_impl(context):
        group = groupStatsPage(context)
        group.clickOnGroup()

    @then('user choose the group "(?P<group>.+)" and sub group "(?P<subGroup>.+)" from dropdowns')
    def step_impl(context, group, subGroup):
        selectGroup = groupStatsPage(context)
        selectGroup.chooseGroup(group, subGroup)

    @then("user click on launch date")
    def step_impl(context):
        date = groupStatsPage(context)
        date.launchDate()

    @step('select starting month "(?P<start>.+)" and ending month "(?P<end>.+)"')
    def step_impl(context, start, end):
        date = groupStatsPage(context)
        date.setDate(start, end)

    @step('verify that "(?P<columnName>.+)" column exists')
    def step_impl(context, columnName):
        column = groupStatsPage(context)
        column.verifyColumnExist(columnName)

    @then("user click on edit columns button")
    def step_impl(context):
        edit = groupStatsPage(context)
        edit.editColumn()

    @step('selects "(?P<group>.+)" from first column of pop up')
    def step_impl(context, group):
        select = groupStatsPage(context)
        select.selectGroup(group)

    @then('user uncheck the "(?P<column>.+)" from pop up')
    def step_impl(context, column):
        uncheck = groupStatsPage(context)
        uncheck.selectColumn(column)

    @then("user click on save changes button")
    def step_impl(context):
        save = groupStatsPage(context)
        save.saveChanges()

    @step('verify that "(?P<columnName>.+)" column does not exist')
    def step_impl(context, columnName):
        column = groupStatsPage(context)
        column.verifyColumnNotExist(columnName)

    @then('check that "(?P<rows>.+)" row exist')
    def step_impl(context, rows):
        checkRow = groupStatsPage(context)
        checkRow.verifyRow(rows)

    @then('check data in "(?P<row>.+)" row')
    def step_impl(context, row):
        data = groupStatsPage(context)
        data.checkData(row)

    @then('verify that data in "(?P<row>.+)" row is changed by changing program')
    def step_impl(context, row):
        data = groupStatsPage(context)
        data.verifyData(row)

    @then('user check the "(?P<engagement>.+)" and "(?P<interaction>.+)" checkbox')
    def step_impl(context, engagement, interaction):
        check = groupStatsPage(context)
        check.selectCheckbox(engagement, interaction)
