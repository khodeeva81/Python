from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_pay_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()


    fields = ['button[name="add-to-cart-sauce-labs-backpack"]',
                 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]',
                  'button[name="add-to-cart-sauce-labs-onesie"]']

    for locator in fields:
        field = driver.find_element(By.CSS_SELECTOR, locator )
        field.click()

    driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ирина")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Ходеева")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("618425")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]')

    total = driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]')
    assert "$58.29" in total.text, f"Ожидался результат '$58.29', но получили {total.text}"

    driver.quit()