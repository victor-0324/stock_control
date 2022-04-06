""" Configs from database conncetions"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHendler:
    """ Sqlalchemy database connection """

    def __init__(self) -> None:
        self.__connection_string = "mariadb+mariadbconnector://bingo_game:bingogn@127.0.0.1:3306/stock_control"
        self.session = None

    def get_engine(self):
        """ Return connection engine
        :param - None
        :return - engine_connection
        """
        engine = create_engine(
            self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close() # pylint: disable=no-member
