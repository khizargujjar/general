Feature:verify data through insights

  Scenario: Verify the comments with Corporate groups
    Given user is at login page
    When user sign in with "email" and "password"
    Then user moves to filter reports page
    And user changes the programme to "Tenet Healthcare - Essentials of Innovation"
    And verify that "No Results" exist against this request
    And user changes the programme to "Tenet Healthcare - Essentials of Accountability"
    And click on Group dropdown to choose group and categories
    Then user choose the "Group" and "Corporate" from dropdowns
    And verify the number of items is "+273"
    And hover on a keyword to get details
    Then user click on that keyword
    Then verify "Load More" button exist
    And verify all the mention comments
    Then user cancel the "Positive" comments
    And user cancel the "Neutral" comments
    And user cancel the "Negative" comments
    Then verify all mixed sentiments
    Then user selects the "Neutral" comments
    And user cancel the "Mixed" comments
    Then verify "Load More" button exist
    Then verify all neutral sentiments
    Then user selects the "Positive" comments
    And user cancel the "Neutral" comments
    Then verify "Load More" button exist
    Then verify all positive sentiments
    Then user selects the "Negative" comments
    And user cancel the "Positive" comments
    Then verify "Load More" button exist
    Then verify all negative sentiments

  Scenario: Verify the comments with Location filter and launch date filter//Selecting different groups and launch dates
    Given user is at login page
    When user sign in with "email" and "password"
    Then user moves to filter reports page
    And user changes the programme to "Tenet Healthcare - Foundations of Interpersonal Skills"
    And verify that "No Results" exist against this request
    And user changes the programme to "Tenet Healthcare - Essentials of Accountability"
    And click on Group dropdown to choose group and categories
    Then user choose the "Location" and "ABRAZO ARROWHEAD CAMPUS" from dropdowns
    Then user click on launch date to select time period
    And select beginning month "July 2018" and ending month "September 2018"
    And verify the number of items is "+80"
    And hover on a keyword to get details
    Then user click on that keyword
    Then verify "Load More" button exist
    And verify the number of actions on that keyword
    And verify all the mention comments
    Then user cancel the "Neutral" comments
    And user cancel the "Negative" comments
    And user cancel the "Mixed" comments
    Then verify "Load More" button exist
    Then verify all positive sentiments
    Then user selects the "Negative" comments
    And user cancel the "Positive" comments
    Then verify "Load More" button exist
    Then verify all negative sentiments
    Then user selects the "Neutral" comments
    And user cancel the "Negative" comments
    Then verify "Load More" button exist
    Then verify all neutral sentiments
    Then user selects the "Mixed" comments
    And user cancel the "Neutral" comments
    Then verify "Load More" button exist
    Then verify all mixed sentiments

  Scenario: Verify the comments with Location from groupby filter
    Given user is at login page
    When user sign in with "email" and "password"
    Then user moves to filter reports page
    And user select "location" from group by filter
    And user changes the programme to "Tenet Healthcare - Foundations of Interpersonal Skills"
    And verify that "No Results" exist against this request
    And user changes the programme to "Tenet Healthcare - Essentials of Accountability"
    And click on Group dropdown to choose group and categories
    Then user choose the "Location" and "ABRAZO ARROWHEAD CAMPUS" from dropdowns
    And verify the number of items is "+80"
    And hover on a keyword to get details
    Then user click on that keyword
    Then verify "Load More" button exist
    And verify the number of actions on that keyword
    And verify all the mention comments
    Then user cancel the "Neutral" comments
    And user cancel the "Negative" comments
    And user cancel the "Mixed" comments
    Then verify "Load More" button exist
    Then verify all positive sentiments
    Then user selects the "Negative" comments
    Then user cancel the "Positive" comments
    Then verify "Load More" button exist
    Then verify all negative sentiments
    Then user selects the "Neutral" comments
    Then user cancel the "Negative" comments
    Then verify "Load More" button exist
    Then verify all neutral sentiments
    Then user selects the "Mixed" comments
    Then user cancel the "Neutral" comments
    Then verify "Load More" button exist
    Then verify all mixed sentiments