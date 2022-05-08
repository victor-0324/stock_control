from src.database.config import DBConnectionHendler, db_connector
from src.database.models import Equipamentos


class EquipamentosQuerys:
    """Create a new user"""

    @classmethod
    @db_connector
    def novo(cls, connection, modelo, data):
        """someting"""
        criar_novo_equipamento = Equipamentos(
            modelo=modelo.upper(), 
            estado="Estoque",
            cliente="Nenhum", 
            data=data
        )
        connection.session.add(criar_novo_equipamento)
        connection.session.commit()
            
    @classmethod
    @db_connector
    def mostrar(cls, connection):
        """ Retorna o estoque """
        mostrar = connection.session.query(Equipamentos).all()
        return mostrar

    @classmethod
    @db_connector
    def deletar(cls, connection, equipamento_id):
        """Deletando um equipamento"""
        
        equipamento = (
            connection.session.query(Equipamentos)
            .filter_by(id=equipamento_id)
            .first()
        )
        connection.session.delete(equipamento)
        connection.session.commit()
            

    @classmethod
    @db_connector
    def update_trocar(cls, connection, arg1, arg2):
        """ someting """
        query = (connection.session.query(Equipamentos)
        .filter_by(modelo=arg1)
        .first()
        )

        query.estado = "Estoque"
        query.cliente = "Nenhum"
        query.data = arg2
        connection.session.commit()

    @classmethod
    @db_connector
    def update(cls, connection, arg1, arg2, arg3):
        """Atualiza o nome de um exemplo"""

        query = (
            connection.session.query(Equipamentos)
            .filter_by(modelo=arg1)
            .first()
        )
        
        query.estado = "Usando"
        query.cliente = arg2
        query.data = arg3
        connection.session.commit()

    @classmethod
    @db_connector
    def update_retirar(cls, connection, arg1, arg3):
        """Atualiza o nome de um exemplo"""

        query = (
            connection.session.query(Equipamentos)
            .filter_by(modelo=arg1)
            .first()
        )
        
        query.estado = "Estoque"
        query.cliente = "Nenhum"
        query.data = arg3
        connection.session.commit()