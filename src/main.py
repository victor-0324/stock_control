""" Metodo de fabrica """

from flask import Flask


def init_app():
    """ Contruindo o app """
    app = Flask(__name__)
    
    # Configuração do app
    app.secret_key = 'vitorvitoriaeyaramariaauvesdacosta'
    
    with app.app_context():

        # Aplicativo de autenticação
        from .auth import auth_app
        app.register_blueprint(auth_app)

        return app
