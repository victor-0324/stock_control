from sqlalchemy import Column, String, Integer
from src.database import Base


class Operacoes(Base):
    __tablename__ = "operacoes"
    id = Column(Integer, primary_key=True)
    operacao = Column(String(80), nullable=False)
    data_hora = Column(String(80))
    cliente = Column(String(80))
    equipameto = Column(String(80))
