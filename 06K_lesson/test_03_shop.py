import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


def test_purchase():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    wait = WebDriverWait(driver, 10)
    try:
        # Открыть сайт
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Подождать, пока страница загрузится с товарами
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list")))

        # Добавляем товары в корзину
        # Sauce Labs Backpack
        backpack_add_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button")))
        backpack_add_btn.click()
        # Sauce Labs Bolt T-Shirt
        tshirt_add_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button")))
        tshirt_add_btn.click()
        # Sauce Labs Onesie
        onesie_add_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")))
        onesie_add_btn.click()

        # Перейти в корзину
        cart_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_link.click()

        # Нажать Checkout
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # Заполнить форму
        first_name = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        last_name = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        postal_code = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))

        first_name.send_keys("Иван")
        last_name.send_keys("Иванов")
        postal_code.send_keys("12345")
        continue_button.click()

        # На странице итога получить сумму
        total_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_subtotal_label")))
        total_text = total_element.text  # Например: "Item total: $39.98"

        # Проверить сумму
        # Распарсим число из текста
        import re
        match = re.search(r'\$(\d+\.\d+)', total_text)
        assert match, "Total amount not found in the text"
        total_amount = match.group(1)
        assert total_amount == "58.29", f"Expected total to be $58.29, but got ${total_amount}"

    finally:
        driver.quit()