# pylint: disable:E1101

""" User Querys"""

from src.database.config import DBConnectionHendler
from src.database.models.User import User

class CheckName:
    """ A Consult if name alredy exits """
    @classmethod
    def check_name(cls, name):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(User).filter_by(name=name).first()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
                

class CheckUsers:
    """ A Consult if name alredy exits """
    @classmethod
    def check_Users(cls):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(User).all()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

class CreateUsers:
    """ Create a new user """
    @classmethod
    def create_User(cls, name):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                new_user = User(name=name)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


class GetId:
    """ A Consult if name alredy exits """
    @classmethod
    def get_id(cls, name):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                return db_connection.session.query(User).filter_by(name=name).first()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()


class DeleteUser:
    """ Delete a User """
    @classmethod
    def delete_User(names, name):
        """ someting """
        with DBConnectionHendler() as db_connection:
            try:
                User = db_connection.session.query(User).filter_by(name=name).first()
                db_connection.session.delete(User)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()