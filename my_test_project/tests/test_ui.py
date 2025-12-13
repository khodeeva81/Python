import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для инициализации и финализации драйвера
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()  # Укажите путь, если нужен
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Поиск фильмов")
def test_search_movie(driver):
    """Тест поиска фильма по названию"""
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")
    search_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    with allure.step("Вводим название фильма и отправляем поиск"):
        search_input.send_keys("Красотка" + Keys.RETURN)
    # Проверка появления результатов
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.element")))
    assert "Красотка" in driver.page_source
    allure.attach(driver.get_screenshot_as_png(), name="search_results", attachment_type=allure.attachment_type.PNG)

@allure.feature("Открытие страницы фильма")
def test_open_movie_page(driver):
    """Тест открытия страницы конкретного фильма"""
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")
    search_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    with allure.step("Вводим название фильма и отправляем поиск"):
        search_input.send_keys("Красотка" + Keys.RETURN)
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'element')]/a")))
    with allure.step("Кликаем на первый результат"):
        first_result.click()
    wait.until(EC.title_contains("Красотка"))
    assert "Красотка" in driver.title
    allure.attach(driver.get_screenshot_as_png(), name="movie_page", attachment_type=allure.attachment_type.PNG)

@allure.feature("Фильтры")
def test_filter_movies(driver):
    """Тест использования фильтра по жанру"""
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")
    try:
        with allure.step("Переходим к жанрам и выбираем Комедии"):
            filter_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Жанры")))
            filter_button.click()
            comedy_filter = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Комедии")))
            comedy_filter.click()
            assert "Комедии" in driver.page_source
    except Exception as e:
        pytest.fail(f"Ошибка при фильтрации: {e}")

@allure.feature("Детали фильма")
def test_movie_details(driver):
    """Проверка отображения деталей фильма"""
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")
    search_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    search_input.send_keys("Красотка" + Keys.RETURN)
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'element')]/a")))
    first_result.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Описание')]")))
    assert "Описание" in driver.page_source

@allure.feature("Раздел ТОП-250")
def test_top_250(driver):
    """Переход к разделу ТОП-250"""
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.kinopoisk.ru/")
    top_250_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Топ-250")))
    top_250_link.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'ТОП-250')]")))
    assert "ТОП-250" in driver.page_source