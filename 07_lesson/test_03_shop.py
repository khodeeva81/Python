from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Класс страницы авторизации
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

# Класс страницы товаров
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        if product_name == "Sauce Labs Backpack":
            self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-backpack"]').click()
        elif product_name == "Sauce Labs Bolt T-Shirt":
            self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        elif product_name == "Sauce Labs Onesie":
            self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]').click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()

# Класс страницы корзины
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# Класс страницы оформления заказа
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

# Тестовая функция
def test_saucedemo_checkout():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Создаем страницы
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        # Открываем сайт
        driver.get("https://www.saucedemo.com/")

        # Авторизуемся
        login_page.login('standard_user', 'secret_sauce')

        # Добавляем товары
        products_page.add_product_to_cart("Sauce Labs Backpack")
        products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        products_page.add_product_to_cart("Sauce Labs Onesie")

        # Переходим в корзину
        products_page.go_to_cart()

        # Оформляем заказ
        cart_page.proceed_to_checkout()

        # Заполняем форму
        checkout_page.fill_in_form("Ирина", "Ходеева", "618425")

        # Получаем итог
        total_text = checkout_page.get_total()

        # Проверка
        assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получили {total_text}"

    finally:
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    test_saucedemo_checkout()