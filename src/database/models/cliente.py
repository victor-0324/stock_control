from sqlalchemy import Column, String, Integer, Boolean
from src.database import Base 

class Cliente(Base):
    __tablename__ = 'clientes'
    id =  Column(Integer,primary_key=True)
    nome = Column(String(80),nullable=False)
    estado = Column(Boolean)

    def __rep__(self):
        return f'{self.nome}: {self.estado}'
