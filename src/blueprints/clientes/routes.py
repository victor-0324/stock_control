from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import CriarCliente, VerCliente, VerClienteId, DeletarCliente
from datetime import datetime
import os

clientes_app = Blueprint(
    'clientes_app',
    __name__,
    url_prefix = '/cliente' 
)



@clientes_app.route("/", methods=["GET"])
def mostrar_cliente():
    today = datetime.now().strftime("%d/%m/%Y")
    clientes = VerCliente.ver_cliente()
    total = len(clientes)
    print(type(clientes))
    return render_template("/pages/cliente/mostrar.html",clientes=clientes,total=total,today=today)


@clientes_app.route("/novo", methods=["GET","POST"])
def novo():
    if request.method == "POST":
        nome = request.form['name']
        data = request.files['data']
        
        CriarCliente.criar_cliente(nome.upper(), data)
        return redirect(url_for('clientes_app.mostrar_cliente'))
    return render_template("/pages/cliente/novo.html")
    

@clientes_app.route("/editar/<int:id_cliente>", methods=["GET","POST"])
def editar(id_cliente):
    cliente = VerClienteId.ver_cliente_id(id_cliente)
    image = os.path.join('/media/equipamentos/', cliente.nome +'.jpeg')
    return render_template('/pages/cliente/editar.html',cliente=cliente,image=image)


@clientes_app.route("/deletar/<int:id_cliente>", methods=["GET","POST"])
def deletar(id_cliente):

    DeletarCliente.deletar(id_cliente)
    return redirect(url_for('clientes_app.mostrar_cliente'))



    