Feature:check group stats

  Scenario:change different filters of group stats
    Given user is at login page
    When user sign in with "email" and "password"
    Then user moves to filter reports page
    And click on "Group Stats" from left menu
    And user selects program "Tenet Healthcare - Outstanding Customer Service at Tenet Healthcare"
    And click on Group dropdown to select group and subgroup
    Then user choose the group "Org Level/Title" and sub group "DIRECTOR" from dropdowns
    Then user click on launch date
    And select starting month "July 2018" and ending month "September 2018"
    Then check that "Alabama, Tennessee and Missouri Group" row exist
    And check that "Arizona Group" row exist
    And check that "Corporate" row exist
    And check that "Miami-Dade Group" row exist
    And check that "Michigan, Pennsylvania and Illinois Group" row exist
    And check that "Northern California Group" row exist
    And check that "Palm Beach Group" row exist
    And check that "Shared Services Group" row exist
    And check that "South Carolina and Massachusetts Group" row exist
    And check that "Southern California Group" row exist
    And check that "TPR" row exist
    And check that "TPR Consolidated" row exist
    And check that "Texas Group" row exist
    Then check data in "Corporate" row
    And user selects program "Tenet Healthcare - Essentials of Accountability"
    Then check that "Alabama, Tennessee and Missouri Group" row exist
    And check that "Arizona Group" row exist
    And check that "Corporate" row exist
    And check that "Miami-Dade Group" row exist
    And check that "Michigan, Pennsylvania and Illinois Group" row exist
    And check that "Northern California Group" row exist
    And check that "Palm Beach Group" row exist
    And check that "Shared Services Group" row exist
    And check that "South Carolina and Massachusetts Group" row exist
    And check that "Southern California Group" row exist
    And check that "TPR" row exist
    And check that "TPR Consolidated" row exist
    And check that "Texas Group" row exist
    Then verify that data in "Corporate" row is changed by changing program
    And verify that "LEARNERS" column exists
    And verify that "PARTICIPATION" column exists
    And verify that "VIDEOS WATCHED" column exists
    And verify that "COMPLETION" column exists
    And verify that "THANKS" column exists
    Then user click on edit columns button
    And selects "Org Level/Title" from first column of pop up
    Then user uncheck the "Learners" from pop up
    And user uncheck the "Participation" from pop up
    And user uncheck the "Videos Watched" from pop up
    And user uncheck the "Completion" from pop up
    And user uncheck the "Thanks" from pop up
    Then user click on save changes button
    And verify that "LEARNERS" column does not exist
    And verify that "PARTICIPATION %" column does not exist
    And verify that "VIDEOS WATCHED" column does not exist
    And verify that "COMPLETION" column does not exist
    And verify that "THANKS" column does not exist
    Then user click on edit columns button
    Then user check the "ENGAGEMENT" and "INTERACTIONS" checkbox