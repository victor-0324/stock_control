from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import OperacoesQuerys
from datetime import datetime
import os

operacoes_app = Blueprint(
    'operacoes_app',
    __name__,
    url_prefix = '/operacoes' 
)


@operacoes_app.route("/", methods=["GET"])
def mostrar():
    operacoes = OperacoesQuerys.mostrar()
    return render_template("/pages/operacoes/mostrar.html")


@operacoes_app.route("/novo", methods=["GET", "POST"])
def novo():
    operacoes = OperacoesQuerys.mostrar()
    return render_template("/pages/operacoes/opcoes.html")

@operacoes_app.route("/instalar", methods=["GET", "POST"])
def instalar():
    if request.method == "POST":
        ...
    
    return render_template("/pages/operacoes/instalar.html")

@operacoes_app.route("/trocar", methods=["GET", "POST"])
def trocar():
    if request.method == "POST":
        ...
    
    return render_template("/pages/operacoes/trocar.html")

@operacoes_app.route("/retirar", methods=["GET", "POST"])
def retirar():
    if request.method == "POST":
        ...
    
    return render_template("/pages/operacoes/retirar.html")