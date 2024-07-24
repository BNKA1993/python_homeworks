import requests
import allure
from typing import Dict, List, Union

class EmployeeApi:
    """
    Класс для взаимодействия с API сотрудников компании.
    """

    user = 'bloom'
    password = 'fire-fairy'

    def __init__(self, url: str):
        """
        Инициализирует API сотрудников с заданным URL.

        :param url: Базовый URL для API.
        """
        self.url = url

    @allure.step("api.получить токен авторизации")
    def get_token(self, user: str = user, password: str = password) -> str:
        """
        Получает токен для авторизации.

        :param user: Имя пользователя для авторизации.
        :param password: Пароль для авторизации.
        :return: Токен авторизации.
        """
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("api.создать нового сотрудника компании")
    def create_employee(
            self, company_id: int, first_name: str, last_name: str,
            email: str, isActive: bool, id: int = 1,
            middle_name: str = '', url: str = '', phone: str = '',
            birthdate: str = '2005-05-03T11:19:37.153Z') -> Dict[str, Union[int, str]]:
        """
        Создает нового сотрудника компании.

        :param company_id: Идентификатор компании.
        :param first_name: Имя сотрудника.
        :param last_name: Фамилия сотрудника.
        :param email: Email сотрудника.
        :param isActive: Активен ли сотрудник.
        :param id: Идентификатор сотрудника.
        :param middle_name: Отчество сотрудника.
        :param url: URL сотрудника.
        :param phone: Телефон сотрудника.
        :param birthdate: Дата рождения сотрудника.
        :return: Ответ от сервера в формате словаря.
        """
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName': last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.post(self.url + '/employee', headers=my_headers, json=creds)
        return resp.json()

    @allure.step("api.создать несколько - {num_emp} новых сотрудников компании")
    def create_list_employee_get_list_id(
            self, num_emp: int, company_id: int, first_name: str, last_name: str,
            email: str, isActive: bool, id: int = 1,
            middle_name: str = '', url: str = '', phone: str = '',
            birthdate: str = '2005-05-03T11:19:37.153Z') -> List[int]:
        """
        Создает несколько сотрудников компании и возвращает их идентификаторы.

        :param num_emp: Количество сотрудников для создания.
        :param company_id: Идентификатор компании.
        :param first_name: Имя сотрудников.
        :param last_name: Фамилия сотрудников.
        :param email: Email сотрудников.
        :param isActive: Активны ли сотрудники.
        :param id: Идентификатор сотрудников.
        :param middle_name: Отчество сотрудников.
        :param url: URL сотрудников.
        :param phone: Телефон сотрудников.
        :param birthdate: Дата рождения сотрудников.
        :return: Список идентификаторов созданных сотрудников.
        """
        list_new_emp = []
        list_new_emp_id = []
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName': last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {
            "x-client-token": self.get_token()
        }
        for _ in range(num_emp):
            resp = requests.post(self.url + '/employee', headers=my_headers, json=creds)
            resp_json = resp.json()
            list_new_emp.append(resp_json)

        list_new_emp_id = [emp["id"] for emp in list_new_emp]
        return list_new_emp_id

    @allure.step("api.создать сотрудника без токена авторизации")
    def create_employee_without_auth_token(
            self, company_id: int, dict_creds_emp: Dict[str, Union[int, str]]) -> Dict[str, Any]:
        """
        Создает сотрудника компании без токена авторизации.

        :param company_id: Идентификатор компании.
        :param dict_creds_emp: Словарь с данными сотрудника.
        :return: Ответ от сервера в формате словаря.
        """
        resp = requests.post(self.url + '/employee', json=dict_creds_emp)
        return resp.json()

    @allure.step("api.создать сотрудника без тела запроса")
    def create_employee_without_body(self) -> Dict[str, Any]:
        """
        Создает сотрудника компании без тела запроса.

        :return: Ответ от сервера в формате словаря.
        """
        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.post(self.url + '/employee', headers=my_headers)
        return resp.json()

    @allure.step("api.получить список сотрудников по параметру - {params}")
    def get_list_employee(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Возвращает список сотрудников по заданным параметрам.

        :param params: Параметры запроса.
        :return: Список сотрудников в формате словарей.
        """
        resp = requests.get(self.url + '/employee', params=params)
        return resp.json()

    @allure.step("api.получить сотрудника по id")
    def get_employee_by_id(self, emp_id: int) -> Dict[str, Any]:
        """
        Получает информацию о сотруднике по идентификатору.

        :param emp_id: Идентификатор сотрудника.
        :return: Словарь с информацией о сотруднике.
        """
        resp = requests.get(self.url + '/employee/' + str(emp_id))
        return resp.json()

    @allure.step("api.получить сотрудника по id без id")
    def get_employee_by_id_without_id(self) -> Dict[str, Any]:
        """
        Получает информацию о сотруднике без указания идентификатора.

        :return: Ответ от сервера в формате словаря.
        """
        resp = requests.get(self.url + '/employee/')
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике - {cred}")
    def change_info_employee(
            self, emp_id: int, api_creds_emp: Dict[str, Any]) -> Dict[str, Any]:
        """
        Изменяет информацию о сотруднике по идентификатору.

        :param emp_id: Идентификатор сотрудника.
        :param api_creds_emp: Словарь с данными для обновления.
        :return: Ответ от сервера в формате словаря.
        """
        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.patch(self.url + '/employee/' + str(emp_id), headers=my_headers, json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без токена авторизации")
    def change_info_employee_without_auth_token(
            self, emp_id: int, api_creds_emp: Dict[str, Any]) -> Dict[str, Any]:
        """
        Изменяет информацию о сотруднике без токена авторизации.

        :param emp_id: Идентификатор сотрудника.
        :param api_creds_emp: Словарь с данными для обновления.
        :return: Ответ от сервера в формате словаря.
        """
        resp = requests.patch(self.url + '/employee/' + str(emp_id), json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без id")
    def change_info_employee_without_id(
            self, api_creds_emp: Dict[str, Any]) -> Dict[str, Any]:
        """
        Изменяет информацию о сотруднике без указания идентификатора.

        :param api_creds_emp: Словарь с данными для обновления.
        :return: Ответ от сервера в формате словаря.
        """
        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.patch(self.url + '/employee/', headers=my_headers, json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без тела запроса")
    def change_info_employee_without_body(
            self, emp_id: int) -> Dict[str, Any]:
        """
        Изменяет информацию о сотруднике без тела запроса.

        :param emp_id: Идентификатор сотрудника.
        :return: Ответ от сервера в формате словаря.
        """
        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.patch(self.url + '/employee/' + str(emp_id), headers=my_headers)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике с несущест. id")
    def change_info_employee_wrong_id(
            self, emp_id: int) -> Dict[str, Any]:
        """
        Изменяет информацию о сотруднике с несуществующим идентификатором.

        :param emp_id: Идентификатор сотрудника.
        :return: Ответ от сервера в формате словаря.
        """
        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.patch(self.url + '/employee/' + str(emp_id), headers=my_headers)
        return resp.json()
