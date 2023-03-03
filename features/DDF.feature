@FunctionalTests
Feature: Excel sheet

  Background: Entering data with Excel sheet
    Given Chrome is opened and Asian Paints app is opened
    Then User clicks on Not Now Alert notification
    Then User clicks on Accept all cookies

  @SmokeTest
  Scenario: Validate Enquire Now functionality with valid data
    When User clicks on Paints&Colours link
    When User tries to enter invalid <name> and <email> and <mobile> and <pincode> for first data
    When User clicks on Enquire Now button
    Then It shows error
    And Browser is closed
