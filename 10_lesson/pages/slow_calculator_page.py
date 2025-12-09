# slow_calculator_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        # Локаторы элементов страницы
        self.delay_input_locator = (By.CSS_SELECTOR, "#delay")
        self.screen_locator = (By.CLASS_NAME, "screen")

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds):
        """Устанавливает задержку работы калькулятора."""
        delay_input = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, label):
        """Кликает по кнопке с заданным ярлыком."""
        button_locator = (By.XPATH, f"//span[text()='{label}']")
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_result(self):
        """Получает текущий отображаемый результат."""
        # Ждем, пока результат обновится и содержимое элемента изменится на "15"
        self.wait.until(EC.text_to_be_present_in_element(self.screen_locator, "15"))
        result_element = self.driver.find_element(*self.screen_locator)
        return result_element.text