import time
from hamcrest import *
from behave import *
from features.pages.HomePageClass import HomePageClass
from features.pages.PaintsandColoursPageClass import PaintsandColoursPageClass

# Writing steps according to "paints&colours" feature file

@given(u'Chrome is opened and Asian Paints app is opened')
def step_impl(context):

    # It will check if the expectedTitle == actualTitle and will actualTitle

    time.sleep(5)
    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title

    print("Page title is: " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@then("User clicks on Not Now Alert notification")
def step_impl(context):

    # Calling Not Now method
    context.driver.implicitly_wait(5)

    NotNowvalue= HomePageClass(context.driver)
    NotNowvalue.click_NotNow_button()

@then("User clicks on Accept all cookies")
def step_impl(context):

    # Calling Cookies method
    HomePage = HomePageClass(context.driver)
    HomePage.click_AcceptCookies_button()


@when(u'User hovers over Paints&Colours link')
def step_impl(context):

    # Calling the hover method(or function) to move the mouse over to paints&colours button

    time.sleep(3)
    hover = HomePageClass(context.driver)
    hover.Hover()


@then(u'Validate hover menu appears')
def step_impl(context):

    # Wait for the sub-menu to appear and then checking if it appears or not

    time.sleep(3)
    HomePage = HomePageClass(context.driver)
    if (HomePage.submenubox()):
        print("Working")
    else:
        print("hover not working")

    '''
    # OR 
    You can also use :
    if (context.driver.find_element(By.XPATH, HomePage.HoverSubmenu)):
        print("Working")
    else:
        print("hover not working")
    '''

@step("Browser is closed")
def step_impl(context):
    pass

# Scenario 2 (not common steps)

@when(u'User clicks on Paints&Colours link')
def step_impl(context):

    # Calling the "click_PaintsandColours_Button" method(or function) to move perform the clicking action

    time.sleep(2)
    HomePage = HomePageClass(context.driver)
    HomePage.click_PaintsandColours_button()


@then(u'It shows Paints&Colours page')
def step_impl(context):

    # It will check if the expectedTitle == actualTitle and will actualTitle

    time.sleep(5)
    expectedTitle = "Paints & Textures for Interior & Exterior Walls - Asian Paints"
    actualTitle = context.driver.title

    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


# Scenario 3 (not common steps)

@when(u'User clicks on Paint Selector link')
def step_impl(context):

    # Scrolling from top to bottom till the page reaches the section where "PaintSelector" is reached

    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, 2100)")

    # Calling the "click_PaintsSelector_Button" method(or function) to move perform the clicking action

    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)
    PaintsandColoursPage.click_PaintSelectors_button()


@then(u'It shows Paint Selector page')
def step_impl(context):

    # It will check if PaintSelector Page is reached
    # by checking the XPATH of an element there which was not present in the previous page using IF ELSE

    time.sleep(2)
    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)

    if(PaintsandColoursPage.PaintSelector_Page()):
        print("Paint Selector page is visible")
    else:
        print("Paint Selector page is not visible")

    '''
    or
    This can be used:
    if(context.driver.find_element(By.XPATH, PaintsandColoursPage.AllColours)):
        print("Paint Selector page is visible")
    else:
        print("Paint Selector page is not visible")
    '''

# Scenario 4 (not common steps)

@when(u'User enters {uname} and {uemail} and {umobile} and {upincode}')
def step_impl(context, uname, uemail, umobile, upincode):

    #It will enter the data like name,email,mobile and pincode from the examples mentioned in feature file

    time.sleep(2)

    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)
    PaintsandColoursPage.enter_username_textbox(uname)
    time.sleep(1)

    PaintsandColoursPage.enter_useremail_textbox(uemail)
    time.sleep(1)

    PaintsandColoursPage.enter_usermobile_textbox(umobile)
    time.sleep(1)

    PaintsandColoursPage.enter_userpincode_textbox(upincode)
    time.sleep(1)


@When(u'User clicks on Enquire Now button')
def step_impl(context):

    #It will call the "click_EnquireNow_button" method(or function) and perform the action mentioned  inside it

    time.sleep(2)
    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)
    PaintsandColoursPage.click_EnquireNow_button()


@then(u'It shows Thank You in the same page')
def step_impl(context):

    #It will check if ecpectedText ==actualText and print the actualText

    time.sleep(2)
    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)
    expectedText = " Thank you!"
    actualText = PaintsandColoursPage.ThankYouText()

    print(actualText)
    assert_that(expectedText, actualText, "Text is not same")

    '''
    or use: Using Variable
    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)
    expectedText = " Thank you!"
    actualText = context.driver.find_element(By.CLASS_NAME, PaintsandColoursPage.ThankYou).text
    print(actualText)
    assert_that(expectedText, actualText, "Text is not same")

    Or use: Using XPATH
    if (context.driver.find_element(By.XPATH, "//h2[contains(text(),' Thank you!')]")):
        print("Thank You is visible")
    else:
        print("Thank You is not visible")
    '''

# Scenario 5 (not common steps)

@then(u'It shows error in the same page')
def step_impl(context):

    #It will check after entering wrong data and clicking on EnquireNow Button if the Error message is displayed or not

    time.sleep(2)
    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)

    if(PaintsandColoursPage.Error()):
        print("Error is visible")
    else:
        print("Error is not visible")

    '''
    OR use:
    if(context.driver.find_element(By.XPATH, PaintsandColoursPage.ErrorMessage)):
        print("Error is visible")
    else:
        print("Error is not visible")
    '''

