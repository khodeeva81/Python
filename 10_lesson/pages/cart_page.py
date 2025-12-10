from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.
        :param driver: экземпляр WebDriver, управляющий браузером
        """
        self.driver = driver
        self.checkout_button: tuple = (By.ID, "checkout")  # Локатор кнопки оформления заказа

    def proceed_to_checkout(self) -> None:
        """
        Переходит к оформлению заказа, нажимая кнопку 'Оформить заказ'.
        """
        checkout_btn_element = self.driver.find_element(*self.checkout_button)
        checkout_btn_element.click()