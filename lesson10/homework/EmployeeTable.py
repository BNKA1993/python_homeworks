from sqlalchemy import create_engine
from sqlalchemy.sql import text
from faker import Faker
import allure


@allure.epic("HW9")
@allure.story("BD.employee")
class EmployeeTable:
    __scripts = {
        "select by id": text("select * from employee where id =:id_to_select"),
        "select list emp by id company": text("select * from employee where company_id =:company_id order by id"),
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "select_by_name": text("select * from company where name = 'Company Empoyees 8'"),
        "get max id": "select MAX(id) from employee",
        "insert new": text(
            "insert into employee(first_name, last_name, company_id, is_active, phone, email, middle_name, birthdate, avatar_url) "
            "values (:first_name, :last_name, :company_id, :is_active, :phone, :email, :middle_name, :birthdate, :url)"
        ),
        "update by id": text(
            "update employee set first_name=:first_name, last_name=:last_name, email=:email, middle_name=:middle_name, "
            "is_active=:is_active, phone=:phone, birthdate=:birthdate, avatar_url=:url where id=:id_emp"
        )
    }

    def __init__(self, connection_string: str) -> None:
        """
        Инициализирует соединение с базой данных.

        :param connection_string: Строка подключения к базе данных.
        """
        self.__db = create_engine(connection_string)

    @allure.step("db.получить сотрудника по id")
    def get_emp_by_id(self, emp_id: int) -> list:
        """
        Находит сотрудника по ID.

        :param emp_id: ID сотрудника.
        :return: Список записей с информацией о сотруднике.
        """
        query = self.__db.execute(self.__scripts["select by id"], id_to_select=emp_id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("db.получить список сотрудников по id компании")
    def get_list_emps_by_id_company(self, com_id: int) -> list:
        """
        Находит всех сотрудников компании и возвращает список словарей с информацией о сотрудниках.

        :param com_id: ID компании.
        :return: Список записей с информацией о сотрудниках.
        """
        query = self.__db.execute(self.__scripts["select list emp by id company"], company_id=com_id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("db.получить список id сотрудников по id компании")
    def get_list_id_emps_by_id_company(self, com_id: int) -> list:
        """
        Находит всех сотрудников компании и возвращает список их ID.

        :param com_id: ID компании.
        :return: Список ID сотрудников.
        """
        list_id_emp = []
        id_emp = self.get_list_emps_by_id_company(com_id)
        for emp in id_emp:
            list_id_emp.append(emp[0])
        return list_id_emp

    @allure.step("db.получить max id сотрудника")
    def get_emp_max_id(self) -> int:
        """
        Находит наибольшее значение ID сотрудника и возвращает его.

        :return: Наибольшее значение ID сотрудника.
        """
        query = self.__db.execute(self.__scripts["get max id"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        max_id_emp = query.fetchall()[0][0]
        return max_id_emp

    @allure.step("db.создать нового сотрудника компании")
    def create_employee(self, com_id: int, is_active: bool, dict_creds_emp: dict) -> None:
        """
        Создает нового сотрудника компании с указанными значениями ключей.

        :param com_id: ID компании.
        :param is_active: Статус активности сотрудника.
        :param dict_creds_emp: Словарь с данными сотрудника (first_name, last_name, phone, url, birthdate, email, middle_name).
        """
        query = self.__db.execute(self.__scripts["insert new"],
                                  company_id=com_id,
                                  first_name=dict_creds_emp["first_name"],
                                  last_name=dict_creds_emp["last_name"],
                                  is_active=is_active,
                                  phone=dict_creds_emp["phone"],
                                  url=dict_creds_emp["url"],
                                  birthdate=dict_creds_emp["birthdate"],
                                  email=dict_creds_emp["email"],
                                  middle_name=dict_creds_emp["middle_name"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("db.создать несколько ({num_emp}) новых сотрудников компании")
    def create_employees_mult(self, com_id: int, num_emp: int, is_active: bool) -> None:
        """
        Создает заданное количество сотрудников компании с генерируемыми значениями ключей.

        :param com_id: ID компании.
        :param num_emp: Количество сотрудников для создания.
        :param is_active: Статус активности сотрудников.
        """
        fake = Faker("ru_RU")
        for _ in range(num_emp):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            middle_name = fake.first_name_male()
            phone = fake.random_number(digits=11, fix_len=True)
            birthdate = '2005-04-26'
            url = fake.url()
            max_id = self.get_emp_max_id() + 1
            self.__db.execute(self.__scripts["insert new"], id=max_id,
                              company_id=com_id, first_name=first_name,
                              last_name=last_name, is_active=is_active,
                              phone=phone, url=url, birthdate=birthdate,
                              email=email, middle_name=middle_name)

    @allure.step("db.удалить сотрудника по id")
    def delete(self, emp_id: int) -> None:
        """
        Удаляет сотрудника по ID.

        :param emp_id: ID сотрудника.
        """
        query = self.__db.execute(self.__scripts["delete by id"], id_to_delete=emp_id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("db.удалить список сотрудников по id")
    def delete_list_emps(self, emp_ids: list) -> None:
        """
        Удаляет сотрудников по списку их ID.

        :param emp_ids: Список ID сотрудников для удаления.
        """
        for emp_id in emp_ids:
            query = self.__db.execute(self.__scripts["delete by id"], id_to_delete=emp_id)
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("db.удалить список сотрудников по id компании")
    def delete_list_emps_by_company_id(self, company_id: int) -> None:
        """
        Удаляет сотрудников компании по ID компании. Сначала получает список ID сотрудников по ID компании,
        затем удаляет сотрудников по полученным ID.

        :param company_id: ID компании.
        """
        list_id_emp = self.get_list_id_emps_by_id_company(company_id)
        for emp_id in list_id_emp:
            query = self.__db.execute(self.__scripts["delete by id"], id_to_delete=emp_id)
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("db.обновить данные сотрудника")
    def patch_employee(self, id_emp: int, is_active: bool, dict_creds_emp: dict) -> None:
        """
        Обновляет данные сотрудника по ID.

        :param id_emp: ID сотрудника.
        :param is_active: Новый статус активности сотрудника.
        :param dict_creds_emp: Словарь с новыми данными сотрудника (first_name, last_name, phone, url, birthdate, email, middle_name).
        """
        query = self.__db.execute(self.__scripts["update by id"],
                                  id_emp=id_emp,
                                  first_name=dict_creds_emp["first_name"],
                                  last_name=dict_creds_emp["last_name"],
                                  is_active=is_active,
                                  phone=dict_creds_emp["phone"],
                                  url=dict_creds_emp["url"],
                                  birthdate=dict_creds_emp["birthdate"],
                                  email=dict_creds_emp["email"],
                                  middle_name=dict_creds_emp["middle_name"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("db.получить компании")
    def get_companies(self) -> list:
        """
        Получает список компаний по заданному запросу.

        :return: Список записей с информацией о компаниях.
        """
        return self.__db.execute(self.__scripts["select_by_name"]).fetchall()
