import requests
import pytest

# Базовый URL API
BASE_URL = "https://your-yogile-api-url.com"  # замените на актуальный
# Токен (укажите сюда переменную, которую нужно заполнить)
TOKEN = "<YOUR_ACCESS_TOKEN>"

@pytest.fixture(scope="module")
def headers():
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

@pytest.fixture(scope="module")
def created_project_id(headers):
    # Создаем проект для тестов (позитивный метод POST)
    data = {
        "name": "Test Project",
        # добавьте необходимые обязательные поля по документации
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=headers, json=data)
    assert response.status_code == 201  # или 200, в зависимости от API
    project_id = response.json().get("id")
    yield project_id
    # Можно оформить удаление проекта после тестов (если API поддерживает DELETE)

# ==================== Тесты ====================

# 1. POST /api-v2/projects
def test_create_project_success(headers):
    data = {
        "name": "New Project Positive",
        # другие обязательные поля
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=headers, json=data)
    assert response.status_code == 201
    json_response = response.json()
    assert "id" in json_response

def test_create_project_negative(headers):
    data = {
        # пропущено обязательное поле или неверные данные
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=headers, json=data)
    assert response.status_code == 400  # или 422
    # дополнительно проверить сообщение об ошибке

# 2. PUT /api-v2/projects/{id}
def test_update_project_success(headers, created_project_id):
    data = {
        "name": "Updated Project Name"
        # другие изменения
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/{created_project_id}", headers=headers, json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Project Name"

def test_update_project_negative(headers):
    invalid_id = 999999  # предполагаемый несуществующий ID
    data = {
        "name": "Invalid Update"
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/{invalid_id}", headers=headers, json=data)
    assert response.status_code in [404, 400]

# 3. GET /api-v2/projects/{id}
def test_get_project_success(headers, created_project_id):
    response = requests.get(f"{BASE_URL}/api-v2/projects/{created_project_id}", headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["id"] == created_project_id

def test_get_project_negative(headers):
    invalid_id = 999999
    response = requests.get(f"{BASE_URL}/api-v2/projects/{invalid_id}", headers=headers)
    assert response.status_code in [404, 400]