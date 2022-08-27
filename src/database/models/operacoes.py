from sqlalchemy import Column, String, Integer
from src.database import Base


class Operacoes(Base):
    __tablename__ = "operacoes"
    id = Column(Integer, primary_key=True)
    operacao = Column(String(80), nullable=False)
    data_hora = Column(String(80))
    drop = Column(String(200))
    observacao = Column(String(200))
    cliente = Column(String(80))
    equipamento = Column(String(80))
 
    def __rep__(self):
        return f"{self.operacao}, {self.data_hora}, {self.cliente}, {self.equipameto}, {self.drop}"
