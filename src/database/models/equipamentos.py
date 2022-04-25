from sqlalchemy import Column, String, Integer
from src.database import Base


class Equipamentos(Base):
    __tablename__ = "equipamentos"
    id = Column(Integer, primary_key=True)
    modelo = Column(String(80), nullable=False)
    data = Column(String(80))
    estado = Column(String(80))

    def __rep__(self):
        return f"{self.modelo}{self.estado}{self.historico}{self.data}"
