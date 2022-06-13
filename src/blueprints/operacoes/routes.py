# pylint: disable=unused-argument, no-member, arguments-differ, no-value-for-parameter, unreachable

"""Rotas de Operações"""

import os
from flask import Blueprint, request, render_template, url_for, redirect
from src.database.models import operacoes
from src.database.querys import OperacoesQuerys, ClientesQuerys, EquipamentosQuerys
from datetime import datetime
from src.settings import IMAGE_PATH

operacoes_app = Blueprint("operacoes_app", __name__, url_prefix="/operacoes")

@operacoes_app.route("/", methods=["GET"])
def mostrar():
    """Mostra todas as operações"""
    operacoes = OperacoesQuerys.mostrar().all()[::-1]
    return render_template("/pages/operacoes/mostrar.html", operacoes=operacoes)

@operacoes_app.route("/novo", methods=["GET", "POST"])
def novo():
    """Nova Operação"""
    return render_template("/pages/operacoes/opcoes.html")

@operacoes_app.route("/detalhes/<os_id>", methods=["GET", "POST"])
def detalhes(os_id):
    """ Detalhes de uma operação """
    operacao = OperacoesQuerys.get_by_id(os_id)
    print(type(operacao))
    return render_template("/pages/operacoes/detalhes.html", operacao=operacao)

@operacoes_app.route("/deletar/<os_id>", methods=["GET", "POST"])
def deletar(os_id):
    """ Deletar uma operação """
    OperacoesQuerys.deletar(os_id)
    return redirect(url_for("operacoes_app.mostrar"))

@operacoes_app.route("/instalar", methods=["GET", "POST"])
def instalar():
    """ Realiza a instalação de um equipamento """
    if request.method == "POST":
        cliente = request.form.get("cliente")
        equipamento = request.form.get("equipamento")
        observacao = request.form.get("obs")
        date_time = datetime.now().strftime("%d/%m/%Y  %H:%M")
        OperacoesQuerys.instalar(cliente, equipamento, date_time, observacao)

        imagem = request.files.get("imagem")
        operacao = OperacoesQuerys.mostrar()[-1]
        imagem.save(
            os.path.join(IMAGE_PATH, f"{operacao.id}.jpg")
        ) 
        
        ClientesQuerys.update(cliente, equipamento, date_time)
        EquipamentosQuerys.update(equipamento, cliente, date_time)
        return redirect(url_for("operacoes_app.mostrar"))
        
    clientes = [
        cliente.nome
        for cliente in ClientesQuerys.mostrar()
        if cliente.equipamento == "Nenhum"
    ]

    equipamentos = [
        equipamento.modelo
        for equipamento in EquipamentosQuerys.mostrar()
        if equipamento.estado == "Estoque"
    ]
    
    return render_template(
        "/pages/operacoes/instalar.html",
        clientes_disponiveis=clientes,
        equipamentos_disponiveis=equipamentos,
    )

@operacoes_app.route("/trocar", methods=["GET", "POST"])
def trocar():
    """Realiza a troca de um equipamento"""
    if request.method == "POST":

        observacao = request.form.get("obs")
        cliente = request.form.get("cliente")
        equipamento = request.form.get("equipamento")
        equipamento_trocado = request.form.get("equipamentoss")
        date_time = datetime.now().strftime("%d/%m/%Y  %H:%M")
        imagem = request.files.get("imagem")

        OperacoesQuerys.trocar(cliente, equipamento_trocado, date_time, observacao)
        operacao = OperacoesQuerys.mostrar()[-1]
        
        imagem.save(
            os.path.join(IMAGE_PATH, f"{operacao.id}.jpg")
        ) 
        

        ClientesQuerys.update(cliente, equipamento_trocado, date_time)
        EquipamentosQuerys.update_trocar(equipamento, date_time)
        EquipamentosQuerys.update(equipamento_trocado, cliente, date_time)
        return redirect(url_for("operacoes_app.mostrar"))
        

    clientes = [
        cliente.nome
        for cliente in ClientesQuerys.mostrar()
        if cliente.equipamento != "Nenhum"
    ]
    equipamentos = [
        equipamento.modelo
        for equipamento in EquipamentosQuerys.mostrar()
        if equipamento.estado == "Usando"
    ]
    equipamentoss = [
        equipamento.modelo
        for equipamento in EquipamentosQuerys.mostrar()
        if equipamento.estado == "Estoque"
    ]
    
    return render_template(
        "/pages/operacoes/trocar.html",
        clientes_disponiveis=clientes,
        equipamentos_disponiveis=equipamentos,
        equipamentos_para_trocar=equipamentoss,
    )

@operacoes_app.route("/retirar", methods=["GET", "POST"])
def retirar():
    """Faz a retirada de um equipamento"""
    if request.method == "POST":
       
        cliente = request.form.get("cliente")
        equipamento = request.form.get("equipamento")
        observacao = request.form.get("obs")
        date_time = datetime.now().strftime("%d/%m/%Y  %H:%M")
        imagem = request.files.get("imagem")
        OperacoesQuerys.retirar(cliente, equipamento, date_time, observacao)
       
        operacao = OperacoesQuerys.mostrar()[-1]
        
        imagem.save(
            os.path.join(IMAGE_PATH, f"{operacao.id}.jpg")
        )  
        
        ClientesQuerys.update_retirar(cliente, date_time)
        EquipamentosQuerys.update_retirar(equipamento,  date_time)
        return redirect(url_for("operacoes_app.mostrar"))
        

    clientes = [
        cliente.nome
        for cliente in ClientesQuerys.mostrar()
        if cliente.equipamento != "Nenhum"
    ]
    equipamentos = [
        equipamento.modelo
        for equipamento in EquipamentosQuerys.mostrar()
        if equipamento.estado == "Usando"
    ]
    
    return render_template(
        "/pages/operacoes/retirar.html",
        clientes_disponiveis=clientes,
        equipamentos_disponiveis=equipamentos,
    )

@operacoes_app.route("/instalar/novo/cliente", methods=["GET", "POST"])
def instalar_novo_cliente():
    """Cria um novo cliente"""
    if request.method == "POST":
        nome = request.form["name"]
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        ClientesQuerys.criar_cliente(nome.upper(), date_time)
        return redirect(url_for("operacoes_app.instalar"))

    return render_template("/pages/cliente/novo.html")

@operacoes_app.route("/add_novo", methods=["GET", "POST"])
def add_novo():
    """Cria um novo cliente"""
    if request.method == "POST":
        nome = request.form["name"]
        mac = request.form['name1']
        date_time = datetime.now().strftime("%d/%m/%Y")
        ClientesQuerys.add_cliente(nome.upper(), mac.upper(), date_time)
        EquipamentosQuerys.add_novo(mac.upper(), nome.upper(), date_time)
        OperacoesQuerys.add_novo(mac.upper(), nome.upper(), date_time)
        return redirect(url_for("operacoes_app.novo"))

    return render_template("/pages/cliente/add_novo.html")
@operacoes_app.route("/instalar/novo/equipamento", methods=["GET", "POST"])
def instalar_novo_equipamento():
    """Cria um novo equipamento no sistema"""
    if request.method == "POST":
        mensagem = request.form.get("name")
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        EquipamentosQuerys.novo(mensagem, date_time)
        return redirect(url_for("operacoes_app.instalar"))
    return render_template("/pages/equipamento/novo.html")