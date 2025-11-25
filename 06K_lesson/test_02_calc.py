import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator_operations():
    # Инициализация WebDriver для Chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    try:
        # Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Вводим значение 45 в поле #delay
        delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Ждем, пока значение в поле #delay станет равным "45"
        wait.until(lambda d: delay_input.get_attribute("value") == "45")

        # Нажимаем кнопку 7
        button_7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='7']")))
        button_7.click()

        # Нажимаем кнопку +
        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='+']")))
        plus_button.click()

        # Нажимаем кнопку 8
        button_8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='8']")))
        button_8.click()

        # Нажимаем =
        equals_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='=']")))
        equals_button.click()

        # Проверка результата — ожидание появления текста внутри элемента с классом "result"
        result_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
        result_text = result_element.text

        # Проверяем, что результат равен "15" и отображается через 45 секунд
        assert result_text == "15", f"Expected result '15', but got '{result_text}'"
    finally:
        driver.quit()