# tests/test_slow_calculator.py

import pytest
from selenium import webdriver
from pages.slow_calculator import SlowCalculatorPage

def test_slow_calculator():
    driver = webdriver.Chrome()
    calculator_page = SlowCalculatorPage(driver)
    try:
        calculator_page.open()
        calculator_page.set_delay(45)
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_button('=')
        result_text = calculator_page.get_result()
        assert "15" in result_text, f"Ожидался результат 15, но получили {result_text}"
    finally:
        driver.quit()
