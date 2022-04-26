from sqlalchemy import Column, String, Integer, Boolean
from src.database import Base


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    data = Column(String(80))
    estado = Column(String(80))
    equipamento = Column(String(80))

    def __rep__(self):
        return f"{self.nome} {self.estado}{self.data}{self.equipamento}"
