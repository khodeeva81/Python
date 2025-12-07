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
        """
        Открывает страницу калькулятора в браузере.

        :return: None
        """
        self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку (промедление) на выполнение работы калькулятора.

        :param seconds: int - количество секунд задержки.
        :return: None
        """
        delay_input = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, label: str) -> None:
        """
        Нажимает кнопку калькулятора по ее ярлыку.

        :param label: str - текст на кнопке для нажатия.
        :return: None
        """
        button_locator = (By.XPATH, f"//span[text()='{label}']")
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_result(self) -> str:
        """
        Возвращает текущий текстовое значение результата калькулятора.

        :return: str - результат отображаемый в элементе `.screen`.
        """
        # Ждем, пока в элементе появится ожидаемый результат ("15" или другой)
        self.wait.until(EC.text_to_be_present_in_element(self.screen_locator, "15"))
        result_element = self.driver.find_element(*self.screen_locator)
        return result_element.text


# Тестовая функция
def test_slow_calculator() -> None:
    """
    Тестовая функция для проверки работы калькулятора с задержкой.

    Открывает страницу, устанавливает задержку, выполняет простую арифметическую операцию,
    и проверяет результат.

    :return: None
    """
    driver: webdriver.Chrome = webdriver.Chrome()
    calculator_page: SlowCalculatorPage = SlowCalculatorPage(driver)
    try:
        calculator_page.open()
        calculator_page.set_delay(45)
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_button('=')

        result_text: str = calculator_page.get_result()
        assert "15" in result_text, f"Ожидался результат 15, но получили {result_text}"
    finally:
        driver.quit()