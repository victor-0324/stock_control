from typing import List
from src.database.config import DBConnectionHendler, db_connector
from src.database.models import Operacoes


class OperacoesQuerys:
    """Create a new user"""

    @classmethod
    @db_connector
    def mostrar(connection, arg1, arg2=None) -> List:
        con = connection.session.query(Operacoes)
        return con

    @classmethod
    @db_connector
    def instalar(connection, arg1, arg2=None):
        """Pesquisa um exemplo pelo id"""
        print(arg2)
        operacao = Operacoes(cliente=arg2[0],
                            equipamento=arg2[1],
                            data_hora=arg2[2],
                            operacao="Instalação")
        connection.session.add(operacao)
        connection.session.commit()
        

    @classmethod
    @db_connector
    def get_by_id(connection, arg1, arg2=None):
        """Pesquisa um exemplo pelo id"""
        return connection.session.query(Operacoes).filter_by(id=arg2)