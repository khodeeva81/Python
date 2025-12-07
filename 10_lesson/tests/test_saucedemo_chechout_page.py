from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        """
        Конструктор страницы авторизации.

        :param driver: WebDriver — экземпляр драйвера браузера.
        """
        self.driver: WebDriver = driver

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию на сайте — вводит логин и пароль, нажимает кнопку входа.

        :param username: str — имя пользователя.
        :param password: str — пароль пользователя.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()


class ProductsPage:
    def __init__(self, driver: WebDriver):
        """
        Конструктор страницы товаров.

        :param driver: WebDriver — экземпляр драйвера браузера.
        """
        self.driver: WebDriver = driver

    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину по названию.

        :param product_name: str — название продукта.
        :return: None
        """
        if product_name == "Sauce Labs Backpack":
            self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-backpack"]').click()
        elif product_name == "Sauce Labs Bolt T-Shirt":
            self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        elif product_name == "Sauce Labs Onesie":
            self.driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]').click()

    def go_to_cart(self) -> None:
        """
        Переход в корзину — клик по значку корзины.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()


class CartPage:
    def __init__(self, driver: WebDriver):
        """
        Конструктор страницы корзины.

        :param driver: WebDriver — экземпляр драйвера браузера.
        """
        self.driver: WebDriver = driver

    def proceed_to_checkout(self) -> None:
        """
        Переходит к оформлению заказа — нажимает кнопку Checkout.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        """
        Конструктор страницы оформления заказа.

        :param driver: WebDriver — экземпляр драйвера браузера.
        """
        self.driver: WebDriver = driver

    def fill_in_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа и нажимает Continue.

        :param first_name: str — имя покупателя.
        :param last_name: str — фамилия покупателя.
        :param postal_code: str — почтовый индекс.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total(self) -> str:
        """
        Получает итоговую сумму заказа со страницы.

        :return: str — строка с суммой заказа (например, "Total: $58.29").
        """
        total_element = self.driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]')
        return total_element.text