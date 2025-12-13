import pytest
import allure
import requests

BASE_URL = "https://api.kinopoisk.dev/v1.4"
API_KEY = "7HP1KVJ-KN7MHNF-K3Y3H8J-8JNW8M9"

HEADERS = {
    "accept": "application/json",
    "X-API-KEY": API_KEY
}

@allure.feature("API Тесты Kinopoisk")
@pytest.mark.parametrize("test_name, description, url, params", [
    (
        "search_movie_by_title",
        "Тест поиска фильма по названию",
        f"{BASE_URL}/movie/search",
        {"page": 1, "limit": 3, "query": "Красотка"}
    ),
    (
        "get_movie_by_id",
        "Тест получения фильма по ID",
        f"{BASE_URL}/movie/19622",
        None
    ),
    (
        "search_keywords",
        "Тест поиска ключевых слов",
        f"{BASE_URL}/keyword",
        {"page": 1, "limit": 5}
    ),
    (
        "possible_values_countries",
        "Тест получения возможных значений по странам",
        f"{BASE_URL}/possible-values-by-field",
        {"field": "countries.name"}
    ),
    (
        "negative_query",
        "Тест поиска с невалидным запросом",
        f"{BASE_URL}/movie/search",
        {"page":1, "limit":3, "query": "#@!$%&"}
    ),
])
def test_api_endpoints(test_name, description, url, params):
    """Общий тест для разных API-запросов с параметрами."""
    with allure.step(f"Выполняем тест: {test_name} - {description}"):
        response = requests.get(url, headers=HEADERS, params=params)
        assert response.status_code == 200, f"Ошибка при запросе {test_name}. Status code: {response.status_code}"
        data = response.json()
        assert "items" in data or "id" in data or "values" in data or "response" in data or "items" in data, \
            f"Некорректный ответ для {test_name}: {data}"
        # Дополнительные проверки в зависимости от теста
        if test_name == "search_movie_by_title":
            assert len(data["items"]) > 0, "Не найдены фильмы по запросу"
        elif test_name == "get_movie_by_id":
            assert data.get("id") == 19622, "ID фильма не совпадает"
        elif test_name == "search_keywords":
            assert len(data["items"]) > 0, "Ключевые слова не найдены"
        elif test_name == "possible_values_countries":
            assert isinstance(data["values"], list), "Значения по странам не являются списком"
        elif test_name == "negative_query":
            assert "items" in data, "Ответ не содержит 'items'"

        # Можно прикрепить скриншоты или вывод в Allure, если нужно
        # allure.attach(str(data), name="response_data", attachment_type=allure.attachment_type.TEXT)
