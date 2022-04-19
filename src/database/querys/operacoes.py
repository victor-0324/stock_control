from src.database.config import DBConnectionHendler
from src.database.models import Operacoes


class OperacoesQuerys:
    """ Create a new user """
    @classmethod
    def mostrar(cls):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Operacoes).all
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def novo(cls):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Operacoes).all
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
                
