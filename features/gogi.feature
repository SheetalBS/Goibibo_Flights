Feature: flights

  Scenario: verify user is able to search flight options
    Given Launch the browser
    When open Goibibo home page
    And click on one way
    And enter the depart location
    And enter the destination location
    And select the depart date
    And select the adults,children and infant count by using "+" and "-" icons
    And select radio button
    And click on "search flights" button
    Then verify that flight options are displayed