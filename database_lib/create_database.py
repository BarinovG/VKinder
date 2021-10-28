import psycopg2
from database_lib.template_db import create_commands
from psycopg2 import OperationalError
import re
from settings import db_name


class SqlDataBase:
    def __init__(self, sql_db_name):
        self.line = sql_db_name
        new_data_list = self._data_name()
        self.db_name = new_data_list[4]
        self.db_user = new_data_list[1]
        self.db_password = new_data_list[2]
        self.db_port = new_data_list[3]
        self.connection = self._create_connection()

    def _data_name(self):
        ref = r"([a-zA-Z_]*)://([a-zA-Z_]*):([0-9]*)@localhost:([0-9]*)/([a-zA-Z_]*)"
        return re.findall(ref, self.line)[0]

    def _create_connection(self):
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                port=self.db_port,
            )
            print("Есть подключение к бд")
        except OperationalError as e:
            print(f"Ошибка подключения '{e}'")
        return self.connection

    def execute_query(self, query):
        self.connection.autocommit = True
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except OperationalError as e:
            print(e)

    def create_tables(self, command_list):
        for query in command_list:
            self.execute_query(query=query)


def create_db(link_bd):
    sq1 = SqlDataBase(link_bd)
    sq1.create_tables(create_commands)



