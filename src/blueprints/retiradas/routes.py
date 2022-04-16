from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import CriarCliente, VerCliente, VerClienteId, DeletarCliente
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
            if pesquisa == p.nome:
                pesquisa = p.id, p.nome, p.data, p.estado
                print(type(pesquisa))
                return render_template("/pages/retiradas/retirado.html",pesquisa=pesquisa) 
           
    return render_template("/pages/retiradas/mostrar.html",clientes=clientes,total=total,today=today)

    