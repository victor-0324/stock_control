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
    def add_novo(cls, connection, modelo, nome, data):
        """someting"""
        criar_novo_equipamento = Operacoes(
            equipamento=modelo, 
            operacao="Instalação",
            data_hora=data,
            cliente=nome,
            observacao="Instalação feita manualmente pelo tecnico antes do app"
           
        )
        connection.session.add(criar_novo_equipamento)
        connection.session.commit()

    @classmethod
    @db_connector
    def instalar(cls, connection, cliente, equipamento, data_hora, observacao):
        """ Operação de instalação """
       
        operacao = Operacoes(cliente=cliente,
                            equipamento=equipamento,
                            data_hora=data_hora,
                            observacao=observacao,
                            operacao="Instalação")
        connection.session.add(operacao)
        connection.session.commit() 
    
    @classmethod
    @db_connector
    def retirar(cls, connection, cliente, equipamento, data_hora,observacao):
        """ Fazer operação de retirada """
       
        operacao = Operacoes(cliente=cliente,
                            equipamento=equipamento,
                            data_hora=data_hora,
                            observacao=observacao,
                            operacao="Retirada")
        connection.session.add(operacao)
        connection.session.commit() 
        
    @classmethod
    @db_connector
    def trocar(cls, connection, cliente, equipamento_trocado, data_hora, observacao):
        """ Operação de trocar o equipamento """
       
        operacao = Operacoes(cliente=cliente,
                            equipamento=equipamento_trocado,
                            data_hora=data_hora,
                            observacao=observacao,
                            operacao="Troca")
        connection.session.add(operacao)
        connection.session.commit()  

    @classmethod
    @db_connector
    def deletar(cls, connection, arg1):
        """Deletar uma operação"""
        operacoes = connection.session.query(Operacoes).filter_by(id=arg1).first()
        connection.session.delete(operacoes)
        connection.session.commit()
          
    @classmethod
    @db_connector
    def get_by_id(cls, connection, arg1):
        """Pesquisa um exemplo pelo id"""
        return connection.session.query(Operacoes).filter_by(id=arg1)
    
    