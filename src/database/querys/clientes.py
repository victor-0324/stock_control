from src.database.config import DBConnectionHendler
from src.database.models import Cliente


class CriarCliente:
    """ Create a new user """
    @classmethod
    def criar_cliente(cls, nome, data):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                cliente = Cliente(nome=nome.upper(), estado=0, data=data,)
                
                db_connection.session.add(cliente)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

# class RetirarCliente:
#     """ Create a new user """
#     @classmethod
#     def retirar_cliente(cls):
#         """ someting """
#         with DBConnectionHendler() as db_connection:
#             try:
#                 cliente = Cliente(estado=1)
                
#                 db_connection.session.add(cliente)
#                 db_connection.session.commit()
#             except:
#                 db_connection.session.rollback()
#                 raise
#             finally:
#                 db_connection.session.close()

class VerCliente:
    """ Create a new user """
    @classmethod
    def ver_cliente(cls):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Cliente).all()
        
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()



class VerClienteId:
    """ Create a new user """
    @classmethod
    def ver_cliente_id(cls, cliente_id):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(Cliente).filter_by(id=cliente_id).first()
        
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


class DeletarCliente:
    """ Create a new user """
    @classmethod
    def deletar(cls, cliente_id):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                cliente = db_connection.session.query(Cliente).filter_by(id=cliente_id).first()
                db_connection.session.delete(cliente)
                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
