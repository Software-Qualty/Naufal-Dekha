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

    def login(self, username, password):
        # Temukan input email dan password
        time.sleep(2)
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")

        # Masukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(2)
        # Klik tombol login
        button = self.driver.find_element(By.ID, "button")
        button.click()

        # Tunggu alert muncul
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # Tangani alert dengan menerima (klik OK)
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            # Jika alert tidak muncul dalam 10 detik, tangani sesuai kebutuhan
            pass

        print("Login berhasil")

    def logout(self):
        # Temukan tombol logout di navbar dan klik
        time.sleep(10)
        logout = self.driver.find_element(By.XPATH, "//a[@class='navbar-item' and text()='Logout']")
        logout.click()

    
        #if logout.get_attribute("logout") :
            #logout.click()
            #print("Logout successful")
        #else:
            #print("Attribute not found")
    
    # Tunggu alert muncul
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # Tangani alert dengan menerima (klik OK)
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            # Jika alert tidak muncul dalam 10 detik, tangani sesuai kebutuhan
            pass

        print("Logout berhasil")


    def test_createTopikSentimen(self):
        # Buka halaman web
        self.driver.get("https://trensentimen.my.id/")

        # Login
        self.login("bocil123@gmail.com", "bocil1234")

        self.logout()

if __name__ == "__main__":
    unittest.main()