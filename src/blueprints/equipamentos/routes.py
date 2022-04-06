from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import CriarEquipamentos, VerEquipamentos, VerEquipamentoId, DeletarEquipamentos
from datetime import datetime
import os

equipamentos_app = Blueprint(
    'equipamentos_app',
    __name__,
    url_prefix = '/equipamentos' 
)


# Tela de caminho das retiradas das instalções
@equipamentos_app.route("/", methods=["GET"])
def mostrar_equipamentos():
    today = datetime.now().strftime("%d/%m/%Y")
    equipamentos = VerEquipamentos.ver_equipamentos()
    total = len(equipamentos)

    return render_template("/equipamentos.html",equipamento=equipamentos,total=total,today=today)


@equipamentos_app.route("/novo", methods=["GET","POST"])
def novo():
    if request.method == "POST":
        nome = request.form['name']
        image = request.files['image']
        image.save('./src/static/media/equipamentos/'+ nome +'.jpeg')
        CriarEquipamentos.criar_equipamento(nome)
        return redirect(url_for('equipamentos_app.mostrar_equipamentos'))
    return render_template("/novo_equipamento.html")
    

@equipamentos_app.route("/editar/<int:id_equipamento>", methods=["GET","POST"])
def editar(id_equipamento):
    equipamento = VerEquipamentoId.ver_equipamento_id(id_equipamento)
    image = os.path.join('/media/equipamentos/', equipamento.modelo +'.jpeg')
    print(image)
    return render_template('/editar_equipamento.html',equipamento=equipamento,image=image)


@equipamentos_app.route("/deletar/<int:id_equipamento>", methods=["GET","POST"])
def deletar(id_equipamento):
    DeletarEquipamentos.deletar(id_equipamento)

    return redirect(url_for('equipamentos_app.mostrar_equipamentos'))
    # return render_template('equipamentos.html')