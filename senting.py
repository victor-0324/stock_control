# Salvando  a imagem na pagina img
UPLOAD_FOLDER = os.path.join(os.getcwd(),'static/img/instalacao/')
UPLOAD_FOLDE = os.path.join(os.getcwd(),'static/img/inst_ret/')
UPLOAD_FOLDERS = os.path.join(os.getcwd(),'static/img/retiradas/')
UPLOAD_FOLDERSS = os.path.join(os.getcwd(),'static/img/trocas/')


# criando a inginer do banco de dados
engine = sqlalchemy.create_engine(
  "mariadb+mariadbconnector://bingo_game:bingogn@127.0.0.1:3306/stock_control")

# declerando a base do banco de dados
Base = declarative_base()

# # Salvando  a imagem na pagina img
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}