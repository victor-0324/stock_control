""" Metodo de fabrica """

from flask import Flask


def init_app():
    """ Contruindo o app """
    app = Flask(__name__)
    
    # Configuração do app
    app.secret_key = 'vitorvitoriaeyaramariaauvesdacosta'
   
# Database
    from .database import DBConnectionHendler
    from .database import Base

    db_connection = DBConnectionHendler()
    engine = db_connection.get_engine()

    with app.app_context():

        # Aplicativo de autenticação
        from .blueprints import auth_app
        app.register_blueprint(auth_app)

        # Aplicativo de instalção com equipamentos de retiradas
        from .blueprints import equipamentos_app
        app.register_blueprint(equipamentos_app)


        from .blueprints import clientes_app
        app.register_blueprint(clientes_app)

        # Criando a enginer
        Base.metadata.create_all(engine)

        return app

