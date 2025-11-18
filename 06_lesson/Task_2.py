from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")


    input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#textInput")))
    input_field.clear()
    input_field.send_keys("SkyPro")


    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#blueButton")))
    blue_button.click()


    button_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#blueButton"), "Click me"))
    updated_button_text = driver.find_element(By.CSS_SELECTOR, "#blueButton").text
    print(f'"{updated_button_text}"')

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
