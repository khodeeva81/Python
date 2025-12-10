from typing import Union
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class SlowCalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.
        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)
        self.url: str = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Локаторы элементов страницы
        self.delay_input_locator: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        self.screen_locator: tuple[str, str] = (By.CLASS_NAME, "screen")

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds: Union[int, float]) -> None:
        """
        Устанавливает задержку работы калькулятора.
        :param seconds: количество секунд задержки (int или float)
        """
        delay_input: WebElement = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, label: str) -> None:
        """
        Нажимает кнопку калькулятора с заданной надписью.
        :param label: текст на кнопке (например, цифра или операция)
        """
        button_locator: tuple[str, str] = (By.XPATH, f"//span[text()='{label}']")
        button: WebElement = self.wait.until(EC.element_to_be_clickable(button_locator))
        button.click()