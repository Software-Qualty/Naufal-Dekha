import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tunggu sebelum menutup WebDriver
        time.sleep(5)
        self.driver.quit()

    def forgotPass(self):
       forgot_button = self.driver.find_element(By.XPATH, "//a[@href='sendOTP.html")
       forgot_button.click()    



    def test_createTopikSentimen(self):
        # Buka halaman web
        self.driver.get("https://trensentimen.my.id/")

        self.forgotPass()

if __name__ == "__main__":
    unittest.main()