"""Rotas de Operações"""


from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import OperacoesQuerys, ClientesQuerys, EquipamentosQuerys
from datetime import datetime

operacoes_app = Blueprint("operacoes_app", __name__, url_prefix="/operacoes")


@operacoes_app.route("/", methods=["GET"])
def mostrar():
    """Mostra todas as operações"""
    operacoes = OperacoesQuerys.mostrar()
    return render_template("/pages/operacoes/mostrar.html")


@operacoes_app.route("/novo", methods=["GET", "POST"])
def novo():
    """Nova Operação"""
    operacoes = OperacoesQuerys.mostrar()
    return render_template("/pages/operacoes/opcoes.html")


@operacoes_app.route("/instalar", methods=["GET", "POST"])
def instalar():
    """Realiza a instalação de um equipamento"""
    if request.method == "POST":
        ...

    clientes = [
        cliente.nome
        for cliente in ClientesQuerys.mostrar()
        if cliente.equipamento == "Nenhum"
    ]
    equipamentos = [
        equipamento.modelo
        for equipamento in EquipamentosQuerys.mostrar()
        if equipamento.estado == "estoque"
    ]
    print(clientes)

    return render_template(
        "/pages/operacoes/instalar.html",
        clientes_disponiveis=clientes,
        equipamentos_disponiveis=equipamentos,
    )


@operacoes_app.route("/instalar/novo/cliente", methods=["GET", "POST"])
def instalar_novo_cliente():
    """Cria um novo cliente"""
    if request.method == "POST":
        nome = request.form["name"]
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        ClientesQuerys.criar_cliente(nome.upper(), date_time)
        return redirect(url_for("operacoes_app.instalar"))
    return render_template("/pages/cliente/novo.html")


@operacoes_app.route("/instalar/novo/equipamento", methods=["GET", "POST"])
def instalar_novo_equipamento():
    """Cria um novo equipamento no sistema"""
    if request.method == "POST":
        mensagem = request.form.get("name")
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        EquipamentosQuerys.novo(mensagem, date_time)
        return redirect(url_for("equipamentos_app.mostrar"))
    return render_template("/pages/equipamento/novo.html")


@operacoes_app.route("/trocar", methods=["GET", "POST"])
def trocar():
    """Realiza a troca de um equipamento"""
    if request.method == "POST":
        ...

    return render_template("/pages/operacoes/trocar.html")


@operacoes_app.route("/retirar", methods=["GET", "POST"])
def retirar():
    """Faz a retirada de um equipamento"""
    if request.method == "POST":
        ...

    return render_template("/pages/operacoes/retirar.html")
