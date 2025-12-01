import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_saucedemo_checkout():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        login_page.login('standard_user', 'secret_sauce')

        # Добавление товаров
        products_page.add_product_to_cart("Sauce Labs Backpack")
        products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        products_page.add_product_to_cart("Sauce Labs Onesie")

        # Переход в корзину
        products_page.go_to_cart()

        # Оформление заказа
        cart_page.proceed_to_checkout()

        # Заполнение формы
        checkout_page.fill_in_form("Ирина", "Ходеева", "618425")

        # Проверка суммы
        total_text = checkout_page.get_total()
        assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получили {total_text}"

    finally:
        driver.quit()

# Запуск
if __name__ == "__main__":
    test_saucedemo_checkout()