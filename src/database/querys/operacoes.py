# pylint: disable=unused-argument, no-member, arguments-differ


""" User Querys """

from typing import List
from src.database.config import DBConnectionHendler, db_connector
from src.database.models import Operacoes


class OperacoesQuerys:
    """ Aqui estão as consultas no banco de dados e CRUDs """

    @classmethod
    @db_connector
    def mostrar(cls, connection) -> List:
        con = connection.session.query(Operacoes)
        return con

    @classmethod
    @db_connector
    def instalar(cls, connection, cliente, equipamento, data_hora):
        """Pesquisa um exemplo pelo id"""
       
        operacao = Operacoes(cliente=cliente,
                            equipamento=equipamento,
                            data_hora=data_hora,
                            operacao="Instalação")
        connection.session.add(operacao)
        connection.session.commit() 
    
    @classmethod
    @db_connector
    def deletar(cls, connection, arg1):
        """Pesquisa um exemplo pelo id"""
        operacoes = connection.session.query(Operacoes).filter_by(id=arg1).first()
        connection.session.delete(operacoes)
        connection.session.commit()
          
    @classmethod
    @db_connector
    def get_by_id(cls, connection, arg1):
        """Pesquisa um exemplo pelo id"""
        return connection.session.query(Operacoes).filter_by(id=arg1)
    