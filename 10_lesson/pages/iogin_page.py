from typing import Any

class LoginPage:
    def __init__(self, driver: Any) -> None:
        """
        Инициализация страницы логина.
        :param driver: экземпляр WebDriver (например, ChromeDriver)
        """
        self.driver = driver

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.
        :param username: логин пользователя
        :param password: пароль пользователя
        """
        # Тут ваш код для входа
        pass

    def is_login_button_present(self) -> bool:
        """
        Проверяет наличие кнопки входа.
        :return: True, если кнопка есть
        """
        # Тут ваш код для проверки
        return True