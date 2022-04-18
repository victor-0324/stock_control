from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import CriarCliente, VerCliente, VerClienteId, DeletarCliente, RetirarCliente, RetirarEquipamento
from datetime import datetime
import os

retirar_app = Blueprint(
    'retirar_app',
    __name__,
    url_prefix = '/retirar' 
)

@retirar_app.route("/", methods=["GET","POST"])
def retirar():
    today = datetime.now().strftime("%d/%m/%Y")
    clientes = VerCliente.ver_cliente()
    total = len(clientes) 
    if request.method == "POST":
        pesquisa = request.form.get('pesquisa')
        for p in clientes:
            if pesquisa.upper() == p.nome:
                pesquisa = p
                
                print(type(pesquisa))
                return render_template("/pages/retiradas/retirado.html",pesquisa=pesquisa)
           
    return render_template("/pages/retiradas/mostrar.html",clientes=clientes,total=total,today=today)


            
# @retirar_app.route("/retirado/<string:pesquisa>", methods=["GET","POST"])
# def retirado(pesquisa): 
#     if request.method == "GET":
#         today = datetime.now().strftime("%d/%m/%Y")
#         clientes = VerCliente.ver_cliente()
#         total = len(clientes) 
#         pesquisado = RetirarCliente.retirar_cliente(pesquisa[3],pesquisa[1]) 

#         print(pesquisa)
#         return render_template("/pages/cliente/mostrar.html",pesquisa =pesquisado)
#     return render_template("/pages/retiradas/mostrar.html",clientes=clientes,total=total,today=today)



@retirar_app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    
    if request.method == "POST":
        nome = request.form.get('name')
        image = request.files.get('image')
        name = request.form.get('nameeqp')
        data = request.form.get('data')
        image.save('./src/static/media/equipamentos/'+ nome.upper() +'.jpeg')
        RetirarCliente.retirar_cliente(nome, data)
        RetirarEquipamento.retirar_equipamento(name, data)
        # image = os.listdir('./src/static/media/equipamentos/')
        return redirect(url_for('clientes_app.mostrar_cliente'))
    return render_template("/pages/retiradas/retirar.html")
 

    