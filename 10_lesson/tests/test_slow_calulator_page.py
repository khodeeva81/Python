from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver: webdriver.Chrome):
        """
        Инициализация страницы калькулятора.

        :param driver: webdriver.Chrome - драйвер браузера Chrome.
        """
        self.driver: webdriver.Chrome = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 46)
        self.url: str = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        # Локаторы элементов страницы
        self.delay_input_locator: tuple = (By.CSS_SELECTOR, "#delay")
        self.screen_locator: tuple = (By.CLASS_NAME, "screen")

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """Устанавливает задержку работы калькулятора."""
        delay_input = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, label: str) -> None:
        """Кликает по кнопке с заданным ярлыком."""
        button_locator = (By.XPATH, f"//span[text()='{label}']")
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_result(self) -> str:
        """Получает текущий отображаемый результат."""
        # Ждем, пока результат обновится и содержимое элемента изменится
        self.wait.until(EC.text_to_be_present_in_element(self.screen_locator, "15"))
        result_element = self.driver.find_element(*self.screen_locator)
        return result_element.text

def test_slow_calculator() -> None:
    """Тестовая функция: выполнение операции с задержкой и проверка результата."""
    with webdriver.Chrome() as driver:
        calculator_page = SlowCalculatorPage(driver)
        calculator_page.open()
        calculator_row.set_delay(45)
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_button('=')

        result_text = calculator_page.get_result()
        assert "15" in result_text, f"Ожидался результат 15, но получили {result_text}"