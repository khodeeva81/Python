from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.
        :param driver: экземпляр WebDriver, управляющий браузером
        """
        self.driver = driver

        # Локаторы элементов формы
        self.first_name_input: tuple[str, str] = (By.ID, "first-name")
        self.last_name_input: tuple[str, str] = (By.ID, "last-name")
        self.zip_code_input: tuple[str, str] = (By.ID, "postal-code")
        self.continue_button: tuple[str, str] = (By.ID, "continue")
        self.finish_button: tuple[str, str] = (By.ID, "finish")
        self.total_label: tuple[str, str] = (By.CLASS_NAME, "summary_total_label")

    def fill_in_form(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполняет форму с данными покупателя и переходит к следующему шагу.
        :param first_name: имя покупателя
        :param last_name: фамилия покупателя
        :param zip_code: почтовый индекс
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)