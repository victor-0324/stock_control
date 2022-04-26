from src.database.config import DBConnectionHendler
from src.database.models import Equipamentos


class EquipamentosQuerys:
    """Create a new user"""

    @classmethod
    def novo(cls, modelo, data):
        """someting"""
        with DBConnectionHendler() as db_connection:
            try:
                criar_novo_equipamento = Equipamentos(
                    modelo=modelo.upper(), estado="Estoque", data=data
                )
                db_connection.session.add(criar_novo_equipamento)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    # """ Create a new user """
    # @classmethod
    # def retirar_equipamento(cls, name, data):
    #     """ someting """
    #     with DBConnectionHendler() as db_connection:
    #         try:

    #             cliente = Equipamentos(modelo=name.upper(), estado=1, data=data, equipamento='Retirado')

    #             db_connection.session.add(cliente)
    #             db_connection.session.commit()
    #         except:
    #             db_connection.session.rollback()
    #             raise
    #         finally:
    #             db_connection.session.close()

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

    # """ Create a new user """
    # @classmethod
    # def ver_equipamento_id(cls, equipamento_id):
    #     """ someting """
    #     with DBConnectionHendler() as db_connection:
    #         try:
    #             return db_connection.session.query(Equipamentos).filter_by(id=equipamento_id).first()

    #         except:
    #             db_connection.session.rollback()
    #             raise
    #         finally:
    #             db_connection.session.close()

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
