class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # Ваши селекторы и действия
        self.driver.find_element(...).send_keys(username)
        self.driver.find_element(...).send_keys(password)
        self.driver.find_element(...).click()