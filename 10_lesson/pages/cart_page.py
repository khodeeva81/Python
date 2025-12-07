from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")  # Проверьте локатор!

    def proceed_to_checkout(self):
        checkout_btn_element = self.driver.find_element(*self.checkout_button)
        checkout_btn_element.click()