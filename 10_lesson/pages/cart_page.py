from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

        # Локатор кнопки "Checkout" (проверьте актуальный локатор на сайте)
        self.checkout_button = (By.ID, "checkout")  # или другой локатор, например By.XPATH(...)

    def proceed_to_checkout(self):
        # Нажимаем кнопку "Checkout"
        checkout_btn_element = self.driver.find_element(*self.checkout_button)
        checkout_btn_element.click()