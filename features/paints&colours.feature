Feature:  Paints&Colours page

  Background: Entering data with Excel sheet
    Given Chrome is opened and Asian Paints app is opened
    Then User clicks on Not Now Alert notification
    Then User clicks on Accept all cookies

  Scenario: Successfully Hovering over Paints&Colours link
    When User hovers over Paints&Colours link
    Then Validate hover menu appears
    And Browser is closed

  Scenario: Successful navigation on Paints&Colours page
    When User clicks on Paints&Colours link
    Then It shows Paints&Colours page
    And Browser is closed

  Scenario: Successful navigation on Paint Selector page
    When User clicks on Paints&Colours link
    And User clicks on Paint Selector link
    Then It shows Paint Selector page
    And Browser is closed

  Scenario Outline: Validate Enquire Now functionality with valid data on chrome
    When User clicks on Paints&Colours link
    When User enters <validname> and <validemail> and <validmobile> and <validpincode>
    When User clicks on Enquire Now button
    Then It shows Thank You in the same page
    And Browser is closed

    Examples:
      | validname  | validemail       | validmobile | validpincode |
      | john       | jhon@gmail.com   | 9899999999  | 110058       |
      | mary       | mary23@gmail.com | 9999999999  | 110023       |


  Scenario Outline: Validate Enquire Now functionality with invalid data
    When User clicks on Paints&Colours link
    When User enters <invalidname> and <invalidemail> and <invalidmobile> and <invalidpincode>
    When User clicks on Enquire Now button
    Then It shows error in the same page
    And Browser is closed

    Examples:
      | invalidname  | invalidemail     | invalidmobile | invalidpincode |
      | @@@@         | jhong@mailcom    | 999999        | 11005111       |
      | ####         | mary23gmail.com  | 99@#99999     | 1123           |



