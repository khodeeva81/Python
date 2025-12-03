from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_in_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total(self):
        total_element = self.driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]')
        return total_element.text