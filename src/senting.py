# pylint: disable=too-few-public-methods
""" Configurações para o projeto
Para passar determinadas variaveis e constantes para o sistemas
esteremos utilizando objetos com diferentes propriedades para
cada ambiente. Para setar esse ambiente va para
"""

import os

# Constantes de Diretorios do Programa
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
FONT_PATH = os.path.join(PROJECT_PATH, "")
IMAGE_PATH = os.path.join(PROJECT_PATH, "media/")
OPERACOES_PATH = os.path.join(IMAGE_PATH, "operacoes/")
