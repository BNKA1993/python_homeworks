import pytest
from faker import Faker
import allure

from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable
from CompanyTable import CompanyTable

# Конфигурация базового URL для API и строки подключения к базе данных
base_url = 'https://x-clients-be.onrender.com'
db_url = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'

# Инициализация объектов для работы с API и базой данных
db_emp = EmployeeTable(db_url)
db_com = CompanyTable(db_url)
emp = EmployeeApi(base_url)
Faker.seed()
fake = Faker("ru_RU")

# Генерация данных для тестирования
api_creds_emp = {
    'lastName': fake.last_name(),
    'email': fake.email(),
    'url': fake.url(),
    'phone': fake.random_number(digits=11, fix_len=True),
    'isActive': False
}

dict_creds_emp = {
    'first_name': fake.first_name(),
    'last_name': fake.last_name(),
    'email': fake.email(),
    'middle_name': fake.first_name_male(),
    'is_active': True,
    'phone': fake.random_number(digits=11, fix_len=True),
    'birthdate': '2005-04-26',
    'url': fake.url()
}
is_active = True
num_emps = 3  # Количество создаваемых сотрудников

@allure.epic("hw9")
@allure.feature("сотрудник компании")
class TestEmployee:

    @allure.story("получить сотрудника/список сотрудников")
    def test_get_list_employees(self):
        """
        Проверяет получение списка сотрудников компании через API и БД.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Проверка, что у компании нет сотрудников в базе данных
        list_emp_db = db_emp.get_list_emps_by_id_company(company_id)
        assert len(list_emp_db) == 0

        # Создание нескольких сотрудников
        for _ in range(num_emps):
            db_emp.create_employee(company_id, is_active, dict_creds_emp)

        # Проверка количества созданных сотрудников
        assert len(db_emp.get_list_id_emps_by_id_company(company_id)) == num_emps

        result_api = emp.get_list_employee(params={"company": company_id})
        result_db = db_emp.get_list_emps_by_id_company(company_id)
        assert len(result_api) == len(result_db)

        # Сравнение ID сотрудников, полученных через API и БД
        for i in range(num_emps):
            assert result_api[i]["id"] == result_db[i]["id"]

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("получить сотрудника по ID")
    def test_get_employee_by_id(self):
        """
        Проверяет получение сотрудника по ID через API и БД.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Создание нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # Получение сотрудника по ID
        get_new_emp = emp.get_employee_by_id(id_new_emp)

        # Проверка значений ключей ответа
        assert get_new_emp["id"] == id_new_emp
        assert get_new_emp["firstName"] == list_id_new_emp[0][4]
        assert get_new_emp["lastName"] == list_id_new_emp[0][5]
        # Проверка email (возможно, возвращается null)
        assert get_new_emp["isActive"] == list_id_new_emp[0][1]
        assert get_new_emp["middleName"] == list_id_new_emp[0][6]
        # Проверка avatar_url (возможно, возвращается как url)
        assert get_new_emp["avatar_url"] == list_id_new_emp[0][10]
        assert get_new_emp["phone"] == list_id_new_emp[0][7]
        assert get_new_emp["birthdate"] == '2003-04-26'

        # Проверка, что сотрудник присутствует в списке сотрудников компании
        list_emps = db_emp.get_list_emps_by_id_company(company_id)
        emp_list_id = list_emps[-1][0]
        assert emp_list_id == get_new_emp["id"]

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative. Получить сотрудника без ID")
    def test_get_employee_by_id_without_id(self):
        """
        Проверяет получение сотрудника без передачи ID.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Создание нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)

        # Получение сотрудника без ID
        get_new_emp = emp.get_employee_by_id_without_id()
        assert get_new_emp["statusCode"] == 500
        assert get_new_emp["message"] == 'Internal server error'

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative. Получить список сотрудников без ID компании")
    @pytest.mark.xfail(reason="company_id is required")
    def test_get_list_employee_without_company_id(self):
        """
        Проверяет получение списка сотрудников без передачи ID компании.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        result = db_emp.get_list_emps_by_id_company(company_id)
        assert len(result) == 1

        # Удаление компании
        db_com.delete_company(company_id)

    @allure.story("создание сотрудника")
    def test_create_employee(self):
        """
        Проверяет создание нового сотрудника и его получение через API и БД.
        """
        # Создание новой компании
        db_com.create_company('Company Empoyees 8')
        company_id = db_com.get_max_id()

        # Проверка, что у компании нет сотрудников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        len_before = len(emp_list_f)
        assert len_before == 0

        # Создание нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # Проверка, что создан 1 сотрудник
        emp_list = db_emp.get_list_emps_by_id_company(company_id)
        id_emp_create = emp_list[-1]['id']
        len_after = len(emp_list)
        assert len_after - len_before == 1

        # Проверка созданного сотрудника
        result_api = emp.get_employee_by_id(id_new_emp)

        assert result_api["id"] == id_new_emp
        assert result_api["firstName"] == dict_creds_emp["first_name"]
        assert result_api["lastName"] == dict_creds_emp["last_name"]
        assert result_api["isActive"] is True
        assert result_api["middleName"] == dict_creds_emp["middle_name"]
        assert result_api["avatar_url"] == dict_creds_emp["url"]
        assert result_api["phone"] == str(dict_creds_emp["phone"])
        assert result_api["birthdate"] == dict_creds_emp["birthdate"]

        # Проверка, что последний ID сотрудника равен созданному
        assert id_new_emp == id_emp_create

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative. Создание сотрудника без авторизации")
    def test_create_employee_without_auth_token(self):
        """
        Проверяет создание сотрудника без авторизации.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Проверка, что у компании нет сотрудников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        len_before = len(emp_list_f)
        assert len(emp_list_f) == 0

        # Попытка создания сотрудника без авторизации
        new_emp = emp.create_employee_without_auth_token(company_id, dict_creds_emp)
        assert new_emp["statusCode"] == 401
        assert new_emp["message"] == 'Unauthorized'

        # Проверка, что сотрудник не был создан
        emp_list_a = db_emp.get_list_emps_by_id_company(company_id)
        len_after = len(emp_list_a)
        assert len_after - len_before == 0

        # Удаление компании
        db_com.delete_company(company_id)

    @allure.story("negative. Создание сотрудника без тела запроса")
    def test_create_employee_without_body(self):
        """
        Проверяет создание сотрудника без тела запроса.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Проверка, что у компании нет сотрудников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        assert len(emp_list_f) == 0

        # Попытка создания сотрудника без тела запроса
        new_emp = emp.create_employee_without_body()
        assert new_emp["statusCode"] == 500
        assert new_emp["message"] == 'Internal server error'

        # Удаление компании
        db_com.delete_company(company_id)

    @allure.story("редактирование сотрудника")
    def test_patch_employee(self):
        """
        Проверяет редактирование сотрудника.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Создание нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # Редактирование информации о сотруднике
        db_emp.patch_employee(id_new_emp, is_active, dict_creds_emp)
        result_db = db_emp.get_emp_by_id(id_new_emp)

        # Проверка ключей ответа
        assert result_db[0][0] == id_new_emp
        result_api = emp.get_employee_by_id(id_new_emp)

        assert result_db[0][1] == result_api.get('isActive')
        assert result_db[0][8] == result_api.get('email')
        assert result_db[0][10] == result_api.get('avatar_url')
        assert result_db[0][6] == result_api.get('middleName')
        assert result_db[0][11] == result_api.get('companyId')

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative. Редактирование сотрудника без авторизации")
    def test_patch_employee_without_auth_token(self):
        """
        Проверяет редактирование сотрудника без авторизации.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Создание нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # Попытка редактирования сотрудника без авторизации
        result = emp.change_info_employee_without_auth_token(id_new_emp, api_creds_emp)
        assert result["statusCode"] == 401
        assert result["message"] == 'Unauthorized'

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative. Редактирование сотрудника без ID")
    def test_patch_employee_without_id(self):
        """
        Проверяет редактирование сотрудника без передачи ID.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Создание нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)

        # Попытка редактирования сотрудника без ID
        result = emp.change_info_employee_without_id(api_creds_emp)
        assert result["statusCode"] == 404
        assert result["error"] == 'Not Found'

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @pytest.mark.xfail(reason="без тела запроса возвращается информация по пользователю")
    @allure.story("negative. Редактирование сотрудника без тела запроса")
    def test_patch_employee_without_body(self):
        """
        Проверяет редактирование сотрудника без тела запроса.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Создание нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # Попытка редактирования сотрудника без тела запроса
        result = emp.change_info_employee_without_body(id_new_emp)
        assert result["statusCode"] == 404
        assert result["error"] == 'Not Found'

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @pytest.mark.xfail(reason="ФР: 500, ОР: 404")
    @allure.story("negative. Редактирование сотрудника с неправильным ID")
    def test_patch_employee_wrong_id(self):
        """
        Проверяет редактирование сотрудника с неправильным ID.
        """
        # Создание новой компании
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # Создание нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # Использование неправильного ID для редактирования
        wrong_emp_id = id_new_emp + 1000
        result = emp.change_info_employee_wrong_id(wrong_emp_id)
        assert result["statusCode"] == 404
        assert result["message"] == 'Not Found'

        # Удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)
