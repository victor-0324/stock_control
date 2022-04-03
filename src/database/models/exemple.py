""" Models for Motorists"""

from sqlalchemy import String, Column

from src.database import Base


class User(Base):
    """ User Table """
    __tablename__ = 'User'
    name = Column(String(80), nullable=False, unique=True)


    def __rep__(self):
        """True, as all users are active."""
        return f"Usr [name={self.name}]"
