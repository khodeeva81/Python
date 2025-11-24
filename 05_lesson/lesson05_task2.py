from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def open_and_click():

    driver = webdriver.Chrome()

    try:

        driver.get("http://uitestingplayground.com/dynamicid")
        time.sleep(2)


        button = driver.find_element(By.XPATH, "//button[contains(text(),'Button')]")


        button.click()

        time.sleep(1)

    finally:

        driver.quit()



for _ in range(3):
    open_and_click()