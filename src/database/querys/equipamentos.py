from src.database.config import DBConnectionHendler, db_connector
from src.database.models import Equipamentos


class EquipamentosQuerys:
    """Create a new user"""

    @classmethod
    def novo(cls, modelo, data):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                criar_novo_equipamento = Equipamentos(
                    modelo=modelo.upper(), estado="Estoque",cliente="Nenhum", data=data
                )
                db_connection.session.add(criar_novo_equipamento)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def mostrar(cls):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Equipamentos).all()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def deletar(cls, equipamento_id):
        """Deletando um equipamento"""
        with DBConnectionHendler() as db_connection:
            try:
                equipamento = (
                    db_connection.session.query(Equipamentos)
                    .filter_by(id=equipamento_id)
                    .first()
                )
                db_connection.session.delete(equipamento)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    @db_connector
    def update_trocar(cls, connection, arg1, arg2):
        """ someting """
        query = (connection.session.query(Equipamentos)
        .filter_by(modelo=arg1)
        .first()
        )

        query.estado = "Estoque"
        query.cliente = "Nenhum"
        query.data = arg2
        connection.session.commit()

    @classmethod
    @db_connector
    def update(cls, connection, arg1, arg2, arg3):
        """Atualiza o nome de um exemplo"""

        query = (
            connection.session.query(Equipamentos)
            .filter_by(modelo=arg1)
            .first()
        )
        
        query.estado = "Usando"
        query.cliente = arg2
        query.data = arg3
        connection.session.commit()

    @classmethod
    @db_connector
    def update_retirar(cls, connection, arg1, arg3):
        """Atualiza o nome de um exemplo"""

        query = (
            connection.session.query(Equipamentos)
            .filter_by(modelo=arg1)
            .first()
        )
        
        query.estado = "Estoque"
        query.cliente = "Nenhum"
        query.data = arg3
        connection.session.commit()