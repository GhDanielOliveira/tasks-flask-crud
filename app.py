from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello word!"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)

    """CODIGOS DE STATUS DE RESPOSTAS HTTP"""
    """
    Respostas informativas ( 100 - 199)
    Respostas bem-sucedidas ( 200 - 299)
    Mensagem de redirecionamento ( 300 - 399)
    Respostas de erro do cliente ( 400 - 499)
    Respostas de erro do servidor ( 500 - 599)
    """
