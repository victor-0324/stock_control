# pylint: disable=unused-argument, no-member, arguments-differ, no-value-for-parameter, unreachable,  disable=unused-import, pylint(import-error)

""" Aplicação de Controle de estoque """

from flask import Blueprint, request, render_template, url_for, redirect
from src.database.querys import EquipamentosQuerys, ClientesQuerys, OperacoesQuerys


initial_app = Blueprint("initial_app", __name__, url_prefix="/")


# Tela Iniciarl
@initial_app.route("/", methods=["GET", "POST"])
def mostrar():
    equipamentos = EquipamentosQuerys().mostrar().all()[::-1]
    total = len(equipamentos)
    clientes = ClientesQuerys.mostrar().all()[::-1]
    total_clientes = len(clientes)
    operacoes = OperacoesQuerys.mostrar().all()[::-1]
    total_operacoes = len(operacoes)
    # if not g.user:
    #     # abort(403)

    #     return redirect(url_for("auth_app.login"))
    return render_template(
        "/pages/initial/index.html",
        total=total,
        total_clientes=total_clientes,
        total_operacoes=total_operacoes,
    )
