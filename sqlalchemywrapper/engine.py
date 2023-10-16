from sqlalchemy import Engine, create_engine
from sqlalchemy import exc
from sqlalchemy import text


class SQLAlchemyEngineWrapper:
    engine = None

    def __init__(self, engine: Engine):
        self.engine = engine

    def select(self, stmt: str, include_column_names: bool = False):
        with self.engine.connect() as connection:

            try:
                rtn = []
                result = connection.execute(text(stmt))

                if include_column_names:
                    rtn.append(tuple(result.keys()))
                rtn += [row for row in result]
                return rtn
            except Exception as e:
                raise e

    # Applies for INSERT, UPDATE, DELETE operations
    def modify(self, stmt: str):
        with self.engine.connect() as connection:
            try:
                connection.execute(text(stmt))
                connection.commit()
            except exc.SQLAlchemyError as e:
                connection.rollback()
                raise e
            except Exception as e:
                connection.rollback()
                raise e

    def modify_bulk(self, stmt_list: list):
        with self.engine.connect() as connection:
            try:
                for stmt in stmt_list:
                    connection.execute(text(stmt))

                connection.commit()
            except exc.SQLAlchemyError as e:
                connection.rollback()
                raise e
            except Exception as e:
                connection.rollback()
                raise e

    @classmethod
    def create_engine_from_connection_str(cls, connection_string, echo=True):
        try:
            return create_engine(connection_string, echo=echo)
        except Exception as e:
            raise e

    @classmethod
    def create_mysqlclient_connection_string(cls, db_host, db_name, db_username, db_password):
        try:
            return 'mysql+mysqldb://{}:{}@{}/{}'.format(db_username, db_password, db_host, db_name)
        except Exception as e:
            raise e

    @classmethod
    def create_mysqlclient_engine(cls, db_host, db_name, db_username, db_password, ssl_ca_filepath=None):
        try:
            connection_str = cls.create_mysqlclient_connection_string(db_host=db_host,
                                                                      db_name=db_name,
                                                                      db_username=db_username,
                                                                      db_password=db_password)

            if ssl_ca_filepath is not None:
                engine = create_engine(connection_str,
                                       connect_args={
                                           'ssl': {
                                               "ca": ssl_ca_filepath
                                           }
                                       }
                )
            else:
                engine = create_engine(connection_str)

            return engine
        except Exception as e:
            raise e
