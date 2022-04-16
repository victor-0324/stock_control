from src.database.config import DBConnectionHendler
from src.database.models import Equipamentos


class CriarEquipamentos:
    """ Create a new user """
    @classmethod
    def criar_equipamento(cls, name, data):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                criar_novo_equipamento = Equipamentos(modelo=name.upper(), estado=0, data=data)
                db_connection.session.add(criar_novo_equipamento)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


class VerEquipamentos:
    """ Create a new user """
    @classmethod
    def ver_equipamentos(cls):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Equipamentos).all()
        
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()



class VerEquipamentoId:
    """ Create a new user """
    @classmethod
    def ver_equipamento_id(cls, equipamento_id):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Equipamentos).filter_by(id=equipamento_id).first()
        
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


class DeletarEquipamentos:
    """ Create a new user """
    @classmethod
    def deletar(cls, equipamento_id):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                equipamento = db_connection.session.query(Equipamentos).filter_by(id=equipamento_id).first()
                db_connection.session.delete(equipamento)
                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
