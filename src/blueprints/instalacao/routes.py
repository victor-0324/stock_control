from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import CriarCliente, CriarEquipamentos
from datetime import datetime
import os

instalacao_app = Blueprint(
    'instalacao_app',
    __name__,
    url_prefix = '/instalacao' 
)

@instalacao_app.route("/novo", methods=["GET", "POST"])
def mostrar_instalacao():

    if request.method == "POST":
        nome = request.form.get('name')
        name = request.form.get('nameeqp')
        image = request.files.get('image')
        image.save('./src/static/media/equipamentos/'+ nome +'.jpeg')
        data = request.form.get('data')
       
        CriarCliente.criar_cliente(nome, data)
        CriarEquipamentos.criar_equipamento(name, data)

        # image = os.listdir('./src/static/media/equipamentos/')
        return redirect(url_for('clientes_app.mostrar_cliente'))
    return render_template("/pages/instalacao/novo.html")

