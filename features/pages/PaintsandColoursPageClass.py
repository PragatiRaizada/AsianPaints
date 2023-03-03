from selenium.webdriver.common.by import By

# Creating class to store all variables and methods
class PaintsandColoursPageClass:

    def __init__(self, driver):
        self.driver = driver

        # Element locator value(Element Properties)

        self.usernameTextBoxElement = "//input[@id='enquire-name']"
        self.usermobileTextBoxElement = "//input[@id='enquire-mobile']"
        self.useremailTextBoxElement = "//input[@id='enquire-email']"
        self.userpincodeTextBoxElement = "//input[@id='enquire-pincode']"

        self.EnquireNowButtonElement = "//button[contains(text(),'ENQUIRE NOW')]"

        self.PaintSelectorsButtonElement = "//h2[contains(text(),'Paint Selector')]"
        self.AllColours = "//span[contains(text(), 'ALL COLOURS') and @class ='colourName']"

        self.ErrorMessage = "//*[text() = 'Username is not valid']"
        self.ThankYou = "thankYouTitle"


    # Making methods for each Text element

    def enter_username_textbox(self, uname):
        usernameTextBox = self.driver.find_element(By.XPATH, self.usernameTextBoxElement)
        usernameTextBox.send_keys(uname)

    def enter_usermobile_textbox(self, umobile):
        usermobileTextBox = self.driver.find_element(By.XPATH, self.usermobileTextBoxElement)
        usermobileTextBox.send_keys(umobile)

    def enter_useremail_textbox(self, uemail):
        useremailTextBox = self.driver.find_element(By.XPATH, self.useremailTextBoxElement)
        useremailTextBox.send_keys(uemail)

    def enter_userpincode_textbox(self, upincode):
        userpincodeTextBox = self.driver.find_element(By.XPATH, self.userpincodeTextBoxElement)
        userpincodeTextBox.send_keys(upincode)


    # Making methods for each Button

    def click_EnquireNow_button(self):
        EnquireNowButton = self.driver.find_element(By.XPATH, self.EnquireNowButtonElement)
        EnquireNowButton.click()

    def click_PaintSelectors_button(self):
        PaintSelectorsButton = self.driver.find_element(By.XPATH, self.PaintSelectorsButtonElement)
        PaintSelectorsButton.click()

    def PaintSelector_Page(self):
        PaintSelectorPage = self.driver.find_element(By.XPATH, self.AllColours)
        return PaintSelectorPage


    # Making methods for thankyou and Error message , displayed after clicking on EnquireNow Button

    def ThankYouText(self):
        ThankYouText = self.driver.find_element(By.CLASS_NAME, self.ThankYou).text
        return ThankYouText

    def Error(self):
        ErrorShown = self.driver.find_element(By.XPATH, self.ErrorMessage)
        return ErrorShown




