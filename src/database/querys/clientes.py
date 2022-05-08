# pylint: disable=unused-argument, no-member, arguments-differ, undefined-variable

from typing import List
from src.database.config import DBConnectionHendler, db_connector
from src.database.models import Cliente


class ClientesQuerys:
    """Create a new user"""

    @classmethod
    def criar_cliente(cls, nome, data):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                cliente = Cliente(
                    nome=nome.upper(), estado="Esperando", data=data, equipamento="Nenhum"
                )

                db_connection.session.add(cliente)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def mostrar(cls):
        """Retorna uma lista de todos os clientes"""
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Cliente).all()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

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
    def deletar(cls, cliente_id):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                cliente = (
                    db_connection.session.query(Cliente)
                    .filter_by(id=cliente_id)
                    .first()
                )
                db_connection.session.delete(cliente)
                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

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
        
        
        