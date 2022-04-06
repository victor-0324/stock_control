""" Models """

import sqlalchemy 
from src.database import Base

# class Retiradas(Base):
#       __tablename__ = 'clientes_ret'
#       id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)      
#       name = sqlalchemy.Column(sqlalchemy.String(length=200),nullable=False)
#       # image = sqlalchemy.Column(sqlalchemy.LargeBinary())
      

#       def __init__(self, name):
#         self.name = name
#         # self.image = image

#       def __repr__(self):
#         return f' {self.name.upper()}'

# class Estalacao(Base):
#       __tablename__ = 'clientes_inst'
#       id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
#       name = sqlalchemy.Column(sqlalchemy.String(length=200))
      
#       def __init__(self, name):
#         self.name = name
        
      
#       def __repr__(self):
#         return f'{self.name}'

class InstRet(Base):
    __tablename__ = 'inst_ret_used'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    instalacao_usado = sqlalchemy.Column(sqlalchemy.String(length=200))
    retirada_usado = sqlalchemy.Column(sqlalchemy.String(length=200))

    # image = image_attachment ( 'UserPicture' ) 

 

    # def __init__(self, instalacao_usado, Retirada_usado):
    #     self.instalacao_usado = instalacao_usado
    #     self.Retirada_usado = Retirada_usado
    #     # self.image = image

    def __repr__(self):
        return f'{self.instalacao_usado.upper()} (usado em) {self.Retirada_usado.upper()}'

# class Trocas(Base):
#     __tablename__ = 'trocas'
#     id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
#     id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
#     recebido = sqlalchemy.Column(sqlalchemy.String(length=100))
#     retirado = sqlalchemy.Column(sqlalchemy.String(length=100))
#   # image = image_attachment ( 'UserPicture' ) 

 
#   def __init__(self, recebido, retirado):
#       self.recebido = recebido
#       self.retirado = retirado
#       # self.image = image

#   def __repr__(self):
#       return f'{self.recebido.upper()} (usado em) {self.retirado.upper()}'


