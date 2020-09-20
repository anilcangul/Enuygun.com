from Locators.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ResultPage():

    def __init__(self,driver):
        self.driver = driver
        self.SEC_BUTTON_CSS = Locators.SEC_BUTTON_CSS
        self.SEC_DONUS_BUTTON_CSS = Locators.SEC_DONUS_BUTTON_CSS


    def gidis_sec_button_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.SEC_BUTTON_CSS))).click()
        #self.driver.find_element_by_css_selector(self.SEC_BUTTON_CSS).click()

    def donus_sec_button_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.SEC_DONUS_BUTTON_CSS))).click()
        #self.driver.find_element_by_css_selector(self.SEC_DONUS_BUTTON_CSS).click()

