from src.database.config import DBConnectionHendler
from src.database.models import Cliente


class ClientesQuerys:
    """Create a new user"""

    @classmethod
    def criar_cliente(cls, nome, data):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                cliente = Cliente(
                    nome=nome.upper(), estado="Ativo", data=data, equipamento="Nenhum"
                )

                db_connection.session.add(cliente)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def retirar_cliente(cls, nome, data):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:

                cliente = Cliente(
                    nome=nome.upper(), estado=1, data=data, equipamento="Retirado"
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


class DeletarCliente:
    """Create a new user"""

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
