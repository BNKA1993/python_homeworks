from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.engine.base import Connection
from typing import List, Tuple, Any

class CompanyTable:
    """
    Класс для работы с таблицей компаний в базе данных.
    """

    __scripts = {
        "select": "select * from company where deleted_at is Null",
        "select only active": "select * from company where is_active = true and deleted_at is Null",
        "delete by id": text("delete from company where id =:id_to_delete"),
        "insert new": text("insert into company(\"name\") values (:new_name)"),
        "get max id": "select MAX(\"id\") from company",
        "select by id": text("select * from company where id =:select_id")
    }

    def __init__(self, connection_string: str):
        """
        Инициализирует подключение к базе данных.

        :param connection_string: Строка подключения к базе данных.
        """
        self.__db = create_engine(connection_string)

    def get_companies(self) -> List[Tuple[Any, ...]]:
        """
        Получает все компании из таблицы.

        :return: Список кортежей, представляющих все записи в таблице компании.
        """
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_active_companies(self) -> List[Tuple[Any, ...]]:
        """
        Получает все активные компании из таблицы.

        :return: Список кортежей, представляющих активные записи в таблице компании.
        """
        return self.__db.execute(self.__scripts["select only active"]).fetchall()

    def delete_company(self, com_id: int) -> None:
        """
        Удаляет компанию из таблицы по идентификатору.

        :param com_id: Идентификатор компании для удаления.
        """
        self.__db.execute(self.__scripts["delete by id"], id_to_delete=com_id)

    def create_company(self, name: str) -> None:
        """
        Создает новую компанию в таблице.

        :param name: Название новой компании.
        """
        self.__db.execute(self.__scripts["insert new"], new_name=name)

    def get_max_id(self) -> int:
        """
        Получает максимальный идентификатор компании в таблице.

        :return: Максимальный идентификатор компании.
        """
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    def get_company_by_id(self, com_id: int) -> List[Tuple[Any, ...]]:
        """
        Получает информацию о компании по идентификатору.

        :param com_id: Идентификатор компании.
        :return: Список кортежей, представляющих запись компании по идентификатору.
        """
        return self.__db.execute(self.__scripts["select by id"], select_id=com_id).fetchall()
