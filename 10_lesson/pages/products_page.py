from typing import Any

class ProductsPage:
    def __init__(self, driver: Any) -> None:
        """
        Инициализация страницы товаров.
        :param driver: WebDriver
        """
        self.driver = driver

    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину.
        :param product_name: название товара
        """
        pass

    def get_products_list(self) -> list:
        """
        Получает список товаров на странице.
        :return: список товаров
        """
        return []