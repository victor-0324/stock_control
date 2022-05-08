# pylint: disable=unused-argument, no-member, arguments-differ, undefined-variable

from typing import List
from src.database.config import DBConnectionHendler, db_connector
from src.database.models import Cliente


class ClientesQuerys:
    """Create a new user"""

    @classmethod
    @db_connector
    def criar_cliente(cls,connection, nome, data):
        """someting"""
        
        cliente = Cliente(
            nome=nome.upper(), 
            estado="Esperando", 
            data=data, 
            equipamento="Nenhum"
        )

        connection.session.add(cliente)
        connection.session.commit()
          
    @classmethod
    @db_connector
    def mostrar(cls, connection) -> List:
        """Retorna uma lista de todos os clientes"""
        cliente = connection.session.query(Cliente).all()
        return cliente

    @classmethod
    def ver_cliente_id(cls, cliente_id):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                return (
                    db_connection.session.query(Cliente)
                    .filter_by(id=cliente_id)
                    .first()
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    @db_connector
    def deletar(cls, connection, arg1):
        """someting"""

        cliente = (
            connection.session.query(Cliente)
            .filter_by(id=arg1)
            .first()
        )
        connection.session.delete(cliente)
        connection.session.commit()

    @classmethod
    @db_connector
    def update(cls, connection, arg1, arg2, arg3):
        """Atualiza o nome de um exemplo"""
        query = (
            connection.session.query(Cliente)
            .filter_by(nome=arg1)
            .first()
        )
        
        query.estado = "Ativo"
        query.data = arg3
        query.equipamento = arg2
        connection.session.commit()
        
    @classmethod
    @db_connector
    def update_retirar(cls, connection, arg1, arg3):
        """Atualiza o nome de um exemplo"""

        query = (
            connection.session.query(Cliente)
            .filter_by(nome=arg1)
            .first()
        )

        query.estado = "Retirado"
        query.data = arg3
        query.equipamento = "Nenhum"
        connection.session.commit()
        
        
        