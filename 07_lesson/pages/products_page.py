from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        product_map = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }
        locator_value = product_map.get(product_name)
        if locator_value:
            locator = f'button[name="{locator_value}"]'
            self.driver.find_element(By.CSS_SELECTOR, locator).click()
        else:
            raise ValueError(f"Нет такого продукта: {product_name}")

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()