from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


service = Service()


driver = webdriver.Firefox(service=service)

try:

    driver.get("http://the-internet.herokuapp.com/login")


    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")


    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")


    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()


    message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")


    print(message.text.strip())

finally:

    driver.quit()