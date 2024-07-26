import requests
from CompanyApi import CompanyApi

api = CompanyApi("https://x-clients-be.onrender.com")


# Проверка получения списка компаний
def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0


# Проверка получения активных компаний
def test_get_active_companies():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    assert len(full_list) > len(filtered_list)


# Проверка добавления новой компании
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id


def test_get_one_company():
    # Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]
    # Обращаемся к компании
    new_company = api.get_company(new_id)
    # Проверим id, название, описание и статус новой компании:
    assert new_company["id"] == new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["isActive"] == True
