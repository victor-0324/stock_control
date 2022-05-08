# pylint: disable=unused-argument, no-member, arguments-differ, no-value-for-parameter, unreachable

"""Rotas de Operações"""

import os
from flask import Blueprint, request, render_template, url_for, redirect
from src.database.models import operacoes
from src.database.querys import OperacoesQuerys, ClientesQuerys, EquipamentosQuerys
from datetime import datetime
from src.settings import IMAGE_PATH, OPERACOES_PATH


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
    """Nova Operação"""
    operacao = OperacoesQuerys.get_by_id(os_id)
    print(operacao)
    return render_template("/pages/operacoes/detalhes.html", operacao=operacao)

@operacoes_app.route("/deletar/<os_id>", methods=["GET", "POST"])
def deletar(os_id):
    """Nova Operação"""
    OperacoesQuerys.deletar(os_id)
    return redirect(url_for("operacoes_app.mostrar"))
    

@operacoes_app.route("/instalar", methods=["GET", "POST"])
def instalar():
    """Realiza a instalação de um equipamento"""
    if request.method == "POST":
        cliente = request.form.get("cliente")
        equipamento = request.form.get("equipamento")
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        imagem = request.files.get("imagem")
        OperacoesQuerys.instalar(cliente, equipamento, date_time)

        operacao = OperacoesQuerys.mostrar()[-1]
        
        imagem.save(
            os.path.join(OPERACOES_PATH, f"{operacao.id}.jpg")
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
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        imagem = request.files.get("imagem")

        OperacoesQuerys.trocar(cliente, equipamento_trocado, date_time, observacao)
        operacao = OperacoesQuerys.mostrar()[-1]
        
        imagem.save(
            os.path.join(OPERACOES_PATH, f"{operacao.id}.jpg")
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
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        imagem = request.files.get("imagem")
        OperacoesQuerys.retirar(cliente, equipamento, date_time)
       
        operacao = OperacoesQuerys.mostrar()[-1]
        
        imagem.save(
            os.path.join(OPERACOES_PATH, f"{operacao.id}.jpg")
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
        return redirect(url_for("operacoes_app.instalar"))
    return render_template("/pages/equipamento/novo.html")