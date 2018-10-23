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
#    And verify that these columns "LEARNERS", "PARTICIPATION", "VIDEOS WATCHED" and "COMPLETION" exists
    And verify that "LEARNERS" columns exists
    And verify that "PARTICIPATION" columns exists
    And verify that "VIDEOS WATCHED" columns exists
    And verify that "COMPLETION" columns exists
    And verify that "THANKS" columns exists
    Then user click on edit columns button
    And selects "Org Level/Title" from first column
    Then user uncheck the "Learners" from second column
    And user uncheck the "Participation" from second column
    And user uncheck the "Videos Watched" from second column
    And user uncheck the "Completion" from second column
    And user uncheck the "Thanks" from third column
    Then user click on save changes button