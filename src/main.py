""" Metodo de fabrica """

from flask import Flask


def init_app():
    """Contruindo o app"""
    app = Flask(__name__)

    # Configuração do app
    app.secret_key = "vitorvitoriaeyaramariaauvesdacosta"

    # Database
    from .database import DBConnectionHendler
    from .database import Base

    db_connection = DBConnectionHendler()
    engine = db_connection.get_engine()

    with app.app_context(): 

        # Aplicativo de autenticação
        from .blueprints import auth

        app.register_blueprint(auth)

        # Aplicativo inicial
        from .blueprints import initial_app

        app.register_blueprint(initial_app)

        # Aplicativo dos equipamentos
        from .blueprints import equipamentos_app

        app.register_blueprint(equipamentos_app)

        # Aplicativo de configuração dos clientes
        from .blueprints import clientes_app

        app.register_blueprint(clientes_app)

        # Aplicativo de configuração das instalação
        from .blueprints import operacoes_app

        app.register_blueprint(operacoes_app)

        # Criando tabelas que não existem e estão
        # Criando a enginer
        Base.metadata.create_all(engine)

        return app
