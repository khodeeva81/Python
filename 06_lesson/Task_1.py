from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/ajax")


    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton"))
    )
    button.click()


    success_message = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    text = success_message.text


    print(text)

except TimeoutException:
    print("Элемент не появился в отведённое время!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:

    driver.quit()
