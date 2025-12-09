import pytest
import allure
from selenium import webdriver
# Ваши импорты страниц
# from your_pages import LoginPage, ProductsPage, CartPage, CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Полный сценарий оформления заказа")
@allure.description("Тест проверяет завершение покупки: вход, добавление товара, оформление заказа")
@allure.feature("Покупка товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_full_checkout_flow(driver):
    with allure.step("Открытие главной страницы и вход"):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)

        with allure.step("Ввод логина и пароля"):
            login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товара в корзину и переход к корзине"):
        products_page = ProductsPage(driver)
        with allure.step("Выбор продукта 'Sauce Labs Backpack'"):
            products_page.add_product_to_cart("Sauce Labs Backpack")
        with allure.step("Переход в корзину"):
            products_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

    with allure.step("Заполнение данных и оформление заказа"):
        checkout_page = CheckoutPage(driver)
        with allure.step("Ввод имени, фамилии, почтового индекса"):
            checkout_page.fill_in_form("Ivan", "Ivanov", "12345")
        with allure.step("Получение итоговой суммы заказа"):
            total = checkout_page.get_total()

        with allure.step(f"Проверка, что итоговая сумма отображается корректно: {total}"):
            assert "$" in total, "Итоговая сумма не найдена или некорректна"