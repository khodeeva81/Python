lesson_10/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── slow_calculator_page.py
├── tests/
│   ├── test_login.py
│   ├── test_add_product.py
│   └── __init__.py
├── requirements.txt
├── README.md


## Описание
Автоматические тесты для калькулятора с задержкой на странице [Slow Calculator](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html).

## Установка зависимостей
```bash
pip install -r requirements.txt
# Инструкция по запуску тестов и просмотру отчетов

pytest --alluredir=allure-results # Запуск тестов с генерацией Allure-отчёта

allure serve allure-results # Открытие отчёта