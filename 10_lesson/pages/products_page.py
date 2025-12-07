from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_template = "//div[contains(@class,'inventory_item') and .//div[text()='%s']]//button[contains(text(),'Add to cart')]"
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_name):
        locator = (By.XPATH, self.add_to_cart_button_template % product_name)
        add_button = self.driver.find_element(*locator)
        add_button.click()

    def go_to_cart(self):
        cart_icon_element = self.driver.find_element(*self.cart_icon)
        cart_icon_element.click()