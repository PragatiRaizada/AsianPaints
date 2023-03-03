import time
from behave import *
from datafiles import ExcelUtils
from selenium.webdriver.common.by import By
from features.pages.PaintsandColoursPageClass import PaintsandColoursPageClass
from features.utility.ConfigClass import ConfigClass

# Writing steps according to "DDF" feature file

@when("User tries to enter invalid {name} and {email} and {mobile} and {pincode} for first data")
def step_impl(context, name, email, mobile, pincode):

    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")

    # It will enter the data like name,email,mobile and pincode mentioned in Excel file

    name = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 1)
    email = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 2)
    mobile = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 3)
    pincode = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 4)

    # It will call the methods to enter in the text fields of name,email,mobile & pincode

    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)
    PaintsandColoursPage.enter_username_textbox(name)
    time.sleep(1)

    PaintsandColoursPage.enter_useremail_textbox(email)
    time.sleep(1)

    PaintsandColoursPage.enter_usermobile_textbox(mobile)
    time.sleep(1)

    PaintsandColoursPage.enter_userpincode_textbox(pincode)
    time.sleep(1)

@then("It shows error")
def step_impl(context):

    # It will check after entering wrong data and clicking on EnquireNow Button if the Error message is displayed or not
    # by passing the test if : no error is shown
    # by failing the test if: error is not shown

    time.sleep(2)
    PaintsandColoursPage = PaintsandColoursPageClass(context.driver)

    if (PaintsandColoursPage.Error()):
        assert True
        print("Test is passed and Error is visible")
        ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 5, "Passed")
    else:
        print("Test is failed and Error is not visible")
        ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 5, "Failed")
        assert False
    time.sleep(2)

