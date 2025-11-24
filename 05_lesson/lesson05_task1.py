from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def click_button():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/classattr")

    try:
        button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        button.click()
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        time.sleep(2)
        driver.quit()


click_button()
click_button()
click_button()