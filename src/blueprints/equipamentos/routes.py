""" Aplicação de Controle de estoque """

from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import EquipamentosQuerys
from datetime import datetime
import os

equipamentos_app = Blueprint("equipamentos_app", __name__, url_prefix="/equipamentos")


@equipamentos_app.route("/", methods=["GET"])
def mostrar():
    """Mostra todos os equipamentos"""
    today = datetime.now().strftime("%d/%m/%Y")
    equipamentos = EquipamentosQuerys().mostrar()
    total = len(equipamentos)
    print(total)
    # image = os.listdir('./src/static/media/equipamentos/')
    return render_template(
        "/pages/equipamento/mostrar.html",
        equipamentos=equipamentos,
        total=total,
        today=today,
    )


@equipamentos_app.route("/novo", methods=["GET", "POST"])
def novo():
    """Cria um novo equipamento no sistema"""
    if request.method == "POST":
        mensagem = request.form.get("name")
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        EquipamentosQuerys.novo(mensagem, date_time)
        return redirect(url_for("equipamentos_app.mostrar"))
    return render_template("/pages/equipamento/novo.html")


@equipamentos_app.route("/editar/<int:id_equipamento>", methods=["GET", "POST"])
def editar(id_equipamento):
    """Edita as caracteristicas de um equipamento"""
    return render_template("/pages/equipamento/editar.html")


@equipamentos_app.route("/deletar/<int:id_equipamento>", methods=["GET", "POST"])
def deletar(id_equipamento):
    """Deleta um equipamento"""
    print(id_equipamento)
    EquipamentosQuerys.deletar(id_equipamento)
    return redirect(url_for("equipamentos_app.mostrar"))
    # return render_template('equipamentos.html')
