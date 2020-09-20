from Locators.Locators import Locators
#from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class ReservationPage():

    def __init__(self,driver):
        self.driver = driver

        self.EMAIL_ID = Locators.EMAIL_ID
        self.PHONE_ID = Locators.PHONE_ID
        self.BIRTHDAY_ID = Locators.BIRTHDAY_ID
        self.BIRTHDATEMONTH_ID = Locators.BIRTHDATEMONTH_ID
        self.BIRTHDATEYEAR_ID = Locators.BIRTHDATEYEAR_ID
        self.NAME_ID = Locators.NAME_ID
        self.LASTNAME_ID = Locators.LASTNAME_ID
        self.PUBLIC_ID = Locators.PUBLIC_ID
        self.HEALTH_CODE_ID = Locators.HEALTH_CODE_ID
        self.ODEMEYE_ILERLE_CSS = Locators.ODEMEYE_ILERLE_CSS
        self.GENDER_MALE_ID = Locators.GENDER_MALE_ID

    def email_box_write(self,email_text):
        self.driver.find_element_by_id(self.EMAIL_ID).send_keys(email_text)

    def phone_box_write(self,phone_number):
        self.driver.find_element_by_id(self.PHONE_ID).send_keys(phone_number)
        time.sleep(1)

    def name_lastname_write(self,name_text,lastname_text):
        self.driver.find_element_by_id(self.NAME_ID).send_keys(name_text)
        time.sleep(2)
        self.driver.find_element_by_id(self.LASTNAME_ID).send_keys(lastname_text)

    def public_id_write(self,public_id_text):
        self.driver.find_element_by_id(self.PUBLIC_ID).send_keys(public_id_text)

    def birthdate_options(self,day,month,year):
        #select ile dropdown menülerdeki değerleri seçiyoruz.
        #GÜN
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.BIRTHDAY_ID))) #self.driver.find_element_by_id(self.BIRTHDAY_ID)
        self.day = Select(element)
        self.day.select_by_value(day)
        #AY
        element2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.BIRTHDATEMONTH_ID))) #self.driver.find_element_by_id(self.BIRTHDATEMONTH_ID)
        self.month = Select(element2)
        self.month.select_by_value(month)
        #YIL
        element3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.BIRTHDATEYEAR_ID))) #self.driver.find_element_by_id(self.BIRTHDATEYEAR_ID)
        self.year = Select(element3)
        self.year.select_by_value(year)
        time.sleep(1)

    def gender_button_check(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.GENDER_MALE_ID))) #self.driver.find_element_by_id(self.GENDER_MALE_ID).click()

    def health_code(self,health_code_text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.HEALTH_CODE_ID))).send_keys(health_code_text)
        #self.driver.find_element_by_id(self.HEALTH_CODE_ID).send_keys(health_code_text)
        #time.sleep(2)

    def go_to_pay(self):
        time.sleep(2)
        self.driver.find_element_by_css_selector(self.ODEMEYE_ILERLE_CSS).click()
        time.sleep(5)

