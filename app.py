from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "calculadora_isac"

@app.route("/", methods=["GET", "POST"])

def rota():
    ultima_interacao = 0

    if request.method == "POST":

        acao_variavel = request.form.get("acao_html")
      
        if acao_variavel == "limpar":
            session.clear()

        operacao_variavel = request.form.get("operacao_html")
        numero_variavel = request.form.get("numero_html")

        if numero_variavel is not None:
            if "primeiro_numero_session" not in session:
                session["primeiro_numero_session"] = numero_variavel
                ultima_interacao = session["primeiro_numero_session"]
            else:
                session["segundo_numero_session"] = numero_variavel
                ultima_interacao = session["segundo_numero_session"]
        
        if operacao_variavel is not None:
            session["operacao_session"] = operacao_variavel
            ultima_interacao = session["operacao_session"]

        if acao_variavel is not None:
            session["acao_session"] = acao_variavel
            ultima_interacao = session["acao_session"]

        primeiro_numero = session.get("primeiro_numero_session")
        segundo_numero = session.get("segundo_numero_session")
        operacao_variavel = session.get("operacao_session")

        if ultima_interacao == "limpar":
            ultima_interacao = 0

        if acao_variavel == "resultado":
            if primeiro_numero is not None and segundo_numero is not None:
                primeiro_numero = int(primeiro_numero)
                segundo_numero = int(segundo_numero)

        if acao_variavel == "resultado":
            if operacao_variavel == "-":
                resultado = (primeiro_numero) - (segundo_numero)
            elif operacao_variavel == "+":
                resultado = (primeiro_numero) + (segundo_numero)
            elif operacao_variavel == "X":
                resultado = (primeiro_numero) * (segundo_numero)
            elif operacao_variavel == "÷":
                resultado = (primeiro_numero) / (segundo_numero)
            ultima_interacao = resultado

    return render_template("index.html", visor = ultima_interacao)

if __name__=="__main__":
    app.run()
