# test_slow_calculator.py

import pytest
import allure
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage

@allure.title("Тест калькулятора с задержкой и проверкой результата")
def test_slow_calculator():
    """Тестовая функция: выполнение операции с задержкой и проверка результата."""
    with webdriver.Chrome() as driver:
        calculator_page = SlowCalculatorPage(driver)

        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки в 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Нажатие кнопки '7'"):
            calculator_page.click_button('7')

        with allure.step("Нажатие кнопки '+'"):
            calculator_page.click_button('+')

        with allure.step("Нажатие кнопки '8'"):
            calculator_page.click_button('8')

        with allure.step("Нажатие кнопки '='"):
            calculator_page.click_button('=')

        with allure.step("Получение и проверка результата"):
            result_text = calculator_page.get_result()

        assert "15" in result_text, f"Ожидался результат 15, но получили {result_text}"