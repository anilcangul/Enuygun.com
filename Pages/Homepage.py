from Locators.Locators import Locators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Homepage():

    # Constructor
    def __init__(self,driver):
        self.driver = driver

        self.NEREDEN_ID = Locators.NEREDEN_ID
        self.ISTANBUL_ID = Locators.ISTANBUL_ID
        self.NEREYE_ID = Locators.NEREYE_ID
        self.TRABZON_ID = Locators.TRABZON_ID
        self.GIDIS_TARIHI_ID = Locators.GIDIS_TARIHI_ID
        self.DONUS_TARIHI_ID = Locators.DONUS_TARIHI_ID
        self.GIDIS_GUN_CSS = Locators.GIDIS_GUN_CSS
        self.DONUS_GUN_CSS = Locators.DONUS_GUN_CSS
        self.UCUZA_BILET_BUL_BUTTON = Locators.UCUZA_BILET_BUL_BUTTON_CSS

    def search_City(self,neredenText,nereyeText):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.NEREDEN_ID))).send_keys(neredenText,Keys.ARROW_DOWN,Keys.ENTER)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.NEREYE_ID))).send_keys(nereyeText,Keys.ARROW_DOWN,Keys.ENTER)
        time.sleep(1)
        #self.driver.find_element_by_id(self.NEREDEN_ID).send_keys(neredenText,Keys.ARROW_DOWN,Keys.ENTER)
        #self.driver.find_element_by_id(self.NEREYE_ID).send_keys(nereyeText,Keys.ARROW_DOWN,Keys.ENTER)

    def date_Click(self):

        # Çift tırnak işaretindeki kod parçalarını time.sleep() ile kullanıyorum fakat WebdriverWait kullanmayı tercih ettim. (Otomasyonu hızlandırma açısından önemli, ve verilen işlemin gerçekleşmesini bekliyor.)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.GIDIS_TARIHI_ID))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.GIDIS_GUN_CSS))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, Locators.DONUS_TARIHI_ID))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.DONUS_GUN_CSS))).click()

        """
        self.driver.find_element_by_id(self.GIDIS_TARIHI_ID).click()
        self.driver.find_element_by_css_selector(self.GIDIS_GUN_CSS).click()
        self.driver.find_element_by_id(self.DONUS_TARIHI_ID).click()
        self.driver.find_element_by_css_selector(self.DONUS_GUN_CSS).click()
        """

    def ucuza_bilet_bul_button_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.UCUZA_BILET_BUL_BUTTON_CSS))).click()
        #self.driver.find_element_by_css_selector(self.UCUZA_BILET_BUL_BUTTON).click()











