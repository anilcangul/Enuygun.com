from selenium import webdriver
import time
import unittest
import sys; print('Python %s on %s' % (sys.version, sys.platform))
from Pages.Homepage import Homepage
from Pages.ResultPage import ResultPage
from Pages.ReservationPage import ReservationPage
#from Locators.Locators import Locators
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC


class BaseTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  ## path : Scripts/Geckodriver.exe copied.
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies() #cookielerden dolayı bazı formlar dolu geldiği için siliyoruz.
        cls.home = Homepage(cls.driver)


    def  test_001Page_Load(self):
        driver = self.driver
        driver.get("https://www.enuygun.com/")
        assert "ENUYGUN" in driver.title             ## Check Title

    def test_002Search(self):
        global neredenText
        global nereyeText
        neredenText = "istanbul"
        nereyeText = "izmir"
        driver = self.driver
        Search = Homepage(driver)
        Search.search_City(neredenText,nereyeText)

    def test_003Date_Click(self):
        driver = self.driver
        date = Homepage(driver)
        date.date_Click()
        #time.sleep(1)

    def test_004Ucuza_Bilet_Bul_Button_click(self):
        driver = self.driver
        ucuza = Homepage(driver)
        ucuza.ucuza_bilet_bul_button_click()
        time.sleep(2)
        arama_url=driver.current_url
        self.assertIn("{}-{}".format(neredenText,nereyeText),self.driver.current_url,"Arama Sonucu Yanlış Link = {}".format(arama_url))
        #Arama sonucunun yanlış olması durumunda assert fırlatıcak.

    def test_005Result_Gidis_Sec_Button_Click(self):
        driver = self.driver
        sec = ResultPage(driver)
        sec.gidis_sec_button_click()
        #time.sleep(2)

    def test_006Result_Donus_Sec_Button_Click(self):
        driver = self.driver
        sec2 = ResultPage(driver)
        bilet_sec = driver.current_url
        sec2.donus_sec_button_click()
        time.sleep(3)
        self.assertIn("rezervasyon",self.driver.current_url,"\nUçak Bileti Seçilemedi.Hata Alınan Sayfa = {}".format(bilet_sec))
        #Uçak bileti seçilemezse  assert fırlatıcak.




    def test_007Email_write(self):
        driver = self.driver
        email_text = "anilcan.gul@outlook.com"
        emailwrite = ReservationPage(driver)
        emailwrite.email_box_write(email_text)
        #time.sleep(2)

    def test_008Phone_Number_write(self):
        driver = self.driver
        phone_number = 38444444
        phonewrite = ReservationPage(driver)
        phonewrite.phone_box_write(phone_number)
        #time.sleep(2)
    
    #Cinsiyet > Tc ve Ad-Soyad yazımı sırasında otomatik seçiliyor cookieleri silmeme rağmen böyle gelmesi Tc veya İsim üzerinden cinsiyet seçtirdiğinizi düşündürdü.
    #Cinsiyetin Otomatik seçilmediği durumlarda bu kod birimi açılabilir.
    """
    def test_009Gender_male_check(self):
        driver = self.driver
        gender = ReservationPage(driver)
        gender.gender_button_check()
    """
    
    def test_010Name_lastname_box_write(self):
        driver = self.driver
        name_text = "Anılcan"
        lastname_text = "Gül"
        name_lastname = ReservationPage(driver)
        name_lastname.name_lastname_write(name_text,lastname_text)

    def test_011Public_Id_box_write(self):
        driver = self.driver
        public_id_text = "51199999198" #Tc değiştirebilirsiniz.
        public_id = ReservationPage(driver)
        public_id.public_id_write(public_id_text)

    def test_012Birthdate_options_check(self):
        driver = self.driver
        day = "02"
        month = "03"
        year = "1997"
        birthdate = ReservationPage(driver)
        birthdate.birthdate_options(day,month,year)

    def test_013Health_code_write(self):
        driver = self.driver
        health_code_text = "L2H4457217" #hes kodununun gerçelilik süresi 01.10.20 'dir
        health = ReservationPage(driver)
        health.health_code(health_code_text)

    def test_014Go_to_pay(self):
        driver = self.driver
        pay = ReservationPage(driver)
        rezervasyon_url = driver.current_url
        pay.go_to_pay()
        time.sleep(4)
        self.assertIn("rezervasyon-odeme",self.driver.current_url,"\nRezervasyon Yapılamadı. Hata Alınan Sayfa = {}".format(rezervasyon_url))
        #Kullanıcı Bilgilerinin yanlış olması durumunda assert fırlatıcak.





    @classmethod
    def test_015tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()