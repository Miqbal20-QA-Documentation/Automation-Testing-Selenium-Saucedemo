import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCheckout(unittest.TestCase):
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=s)

    def test_checkout_products(self):
        # Init
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Wait for initialize, in seconds
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        except ValueError:
            driver.quit()

        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # Add Products
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)

        # Checkout
        driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        time.sleep(1)
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        driver.find_element(By.ID, "first-name").send_keys("Muhammad")
        time.sleep(1)
        driver.find_element(By.ID, "last-name").send_keys("Iqbal")
        time.sleep(1)
        driver.find_element(By.ID, "postal-code").send_keys("5123")
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        driver.find_element(By.ID, "finish").click()
        time.sleep(1)

        # Verification
        response_data = driver.find_element(By.CLASS_NAME, "title").text
        self.assertIn('CHECKOUT: COMPLETE!', response_data)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
