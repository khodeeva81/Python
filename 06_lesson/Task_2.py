from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    wait = WebDriverWait(driver, 10)


    input_field = wait.until(EC.presence_of_element_located((By.ID, "newButtonName")))
    input_field.send_keys("SkyPro")


    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Blue']")))
    button.click()


    button_text = button.text
    print(f'"{button_text}"')
finally:
    driver.quit()
