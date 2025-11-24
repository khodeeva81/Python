from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome()

try:

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 15)



    def images_loaded(driver):
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:

            complete = driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0",
                img)
            if not complete:
                return False
        return True


    wait.until(images_loaded)


    images = driver.find_elements(By.TAG_NAME, "img")

    if len(images) >= 3:
        third_image = images[2]
        src_value = third_image.get_attribute("src")
        print("Значение атрибута src у 3-й картинки:", src_value)
    else:
        print("На странице меньше 3 картинок.")

finally:
    driver.quit()