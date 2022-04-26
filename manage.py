from src import init_app

app = init_app()


# iniciar Servidor
if __name__ == "__main__":
    app.run(debug=True)
