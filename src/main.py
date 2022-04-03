""" Metodo de fabrica """

from flask import Flask


def init_app():
    """ Contruindo o app """
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static')
    
    # Configuração do app
    app.secret_key = 'vitorvitoriaeyaramariaauvesdacosta'
    
    with app.app_context():

        # Aplicativo de autenticação
        from .blueprints import auth_app
        app.register_blueprint(auth_app)

        return app
