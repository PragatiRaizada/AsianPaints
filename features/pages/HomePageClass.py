from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# Creating class to store all variables and methods

class HomePageClass:

    def __init__(self, driver):
        self.driver = driver

        # Making variables, using Element locator value (Element Properties)

        self.PaintsandColoursButtonElement = "//span[@class='iconTextLinks__text visible-in-Desktop' and contains(., 'PAINTS & COLOURS')]"
        self.HoverSubmenu = "//li[@class='nav-item active']"

        #Alert Notification
        self.FrameElement = "//*[@id='__st_fancy_popup']/iframe"
        self.NotNowElement= "//input[@value='Not Now']"

        # Accept COOKIES
        self.AcceptCookies = "//*[text() = 'ACCEPT ALL COOKIES']"


    # Making methods for each element


    def click_NotNow_button(self):

        Frame = self.driver.find_element(By.XPATH, self.FrameElement)
        self.driver.switch_to.frame(Frame)

        clickNotNowButton = self.driver.find_element(By.XPATH, self.NotNowElement)
        clickNotNowButton.click()

        time.sleep(5)
        self.driver.switch_to.default_content()


    def click_AcceptCookies_button(self):
        AcceptCookiesButton = self.driver.find_element(By.XPATH, self.AcceptCookies)
        AcceptCookiesButton.click()


    def click_PaintsandColours_button(self):
        PaintsandColoursButton = self.driver.find_element(By.XPATH, self.PaintsandColoursButtonElement)
        PaintsandColoursButton.click()


    def Hover(self):

        # Find the 'Paints & Colours' menu element
        paints_menu = self.driver.find_element(By.XPATH,"//a[@data-target='#PAINTSCOLOURS']")

        # Hover over the menu using ActionChains
        hover = ActionChains(self.driver).move_to_element(paints_menu)
        hover.perform()

    def submenubox(self):

        # After hovering over using XPATH to see if it is active( box is visible)
        submenu = self.driver.find_element(By.XPATH,self.HoverSubmenu)
        return submenu




