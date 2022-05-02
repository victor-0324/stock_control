# pylint: disable=unused-argument, no-member, arguments-differ, no-value-for-parameter

""" Autenticação de usuario """

from flask import Blueprint, request, session, render_template, g, redirect, url_for
from .user import User
from src.database.querys import EquipamentosQuerys, ClientesQuerys, OperacoesQuerys

auth_app = Blueprint(
    "auth_app",
    __name__,
)

users = []
users.append(User(id=1, username="Vitor", password="123"))
users.append(User(id=2, username="vitor", password="123"))
users.append(User(id=3, username="Mariano", password="1515"))
users.append(User(id=4, username="mariano", password="1515"))


@auth_app.before_request
def before_request():
    g.user = None

    if "user_id" in session:
        user = [x for x in users if x.id == session["user_id"]][0]
        g.user = user


@auth_app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("user_id", None)

        username = request.form["username"]
        password = request.form["password"]

        user = [x for x in users if x.username == username][0]

        if user and user.password == password:
            session["user_id"] = user.id
            return redirect(url_for("auth_app.index"))

        return redirect(url_for("auth_app.login"))
    return render_template("/pages/auth/login.html")


# Tela Iniciarl
@auth_app.route("/", methods=["GET", "POST"])
def index():
    equipamentos = EquipamentosQuerys().mostrar()
    total = len(equipamentos)
    clientes = ClientesQuerys.mostrar()
    total_clientes = len(clientes)
    operacoes = OperacoesQuerys.mostrar().all()[::-1]
    total_operacoes = len(operacoes)
    if not g.user:
        # abort(403)

        return redirect(url_for("auth_app.login"))
    return render_template("/pages/equipamento/index.html",total=total,total_clientes=total_clientes,total_operacoes=total_operacoes)
