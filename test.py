import os
import unittest
from dotenv import load_dotenv
from sqlalchemywrapper.engine import SQLAlchemyEngineWrapper

load_dotenv()


class TestSQLAlchemyEngineWrapper(unittest.TestCase):
    DB_HOST = os.getenv("DB_HOST")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    SSL_CA_FILEPATH = os.getenv("SSL_CA_FILEPATH")
    MYSQLCLIENT_SELECT_QUERY = os.getenv("MYSQLCLIENT_SELECT_QUERY")

    TEST_CONNECTION_STR = "sqlite:///test.db"

    def test_sqlite_full(self):
        try:
            engine_sqlite = SQLAlchemyEngineWrapper.create_engine_from_connection_str(
                connection_string=self.TEST_CONNECTION_STR)
            sqlite_wrapper = SQLAlchemyEngineWrapper(engine=engine_sqlite)


            # TEST CREATE TABLE
            sqlite_wrapper.modify('''
            CREATE TABLE person (
                id INTEGER,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
            );
            ''')

            # TEST INSERT
            sqlite_wrapper.modify('''
            INSERT INTO person (first_name, last_name)
            VALUES ("Patrick", "Star");
            ''')

            # TEST SELECT AFTER INSERT
            print(
                sqlite_wrapper.select('''
                        SELECT * FROM person;
                ''', include_column_names=True)
            )

            # TEST DELETE
            sqlite_wrapper.modify('''
            DELETE FROM person WHERE first_name = "Patrick" and last_name = "Star";
            ''')

            # TEST SELECT AFTER DELETE
            print(
                sqlite_wrapper.select('''
                        SELECT * FROM person;
                ''')
            )

            # TEST DROP TABLE
            sqlite_wrapper.modify('''
            DROP TABLE person;
            ''')

            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)


    def test_mysqlclient_select(self):
        try:
            engine_mysqlclient = SQLAlchemyEngineWrapper.create_mysqlclient_engine(db_host=self.DB_HOST,
                                                                                   db_name=self.DB_NAME,
                                                                                   db_username=self.DB_USERNAME,
                                                                                   db_password=self.DB_PASSWORD,
                                                                                   ssl_ca_filepath=self.SSL_CA_FILEPATH)
            mysqlclient_wrapper = SQLAlchemyEngineWrapper(engine=engine_mysqlclient)


            res = mysqlclient_wrapper.select(self.MYSQLCLIENT_SELECT_QUERY)
            print(res)
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)

