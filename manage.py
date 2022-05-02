from src import init_app

app = init_app()


# iniciar o Servidor
if __name__ == "__main__":
    app.run(debug=True)
