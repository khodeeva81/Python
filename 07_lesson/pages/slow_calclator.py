# pages/slow_calculator.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        # Локаторы
        self.delay_input_locator = (By.CSS_SELECTOR, "#delay")
        self.screen_locator = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, label):
        button_locator = (By.XPATH, f"//span[text()='{label}']")
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_result(self):
        self.wait.until(EC.text_to_be_present_in_element(self.screen_locator, "15"))
        result_element = self.driver.find_element(*self.screen_locator)
        return result_element.text