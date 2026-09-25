from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "calculadora_isac"

@app.route("/", methods=["GET", "POST"])

def rota():
    ultima_interacao = 0
    resultado = None

    if request.method == "POST":

        #Lê dados enviados pelo botão no HTML
        acao_variavel = request.form.get("acao_html")
      
        #Limpa sessão, melhor deixar aqui em cima pq lá em baixo o usuário teria
        # que clicar duas vezes pois no primeiro clique ele iria definir a variavel
        # da session e só no segundo clique ira limpar de fato.
        if acao_variavel == "limpar":
            session.clear()

        #Lê dados enviados pelo botão no HTML
        operacao_variavel = request.form.get("operacao_html")
        numero_variavel = request.form.get("numero_html")

        #Define o primeiro e segundo número da session
        if numero_variavel is not None:
            if "primeiro_numero_session" not in session:
                session["primeiro_numero_session"] = numero_variavel
                ultima_interacao = session["primeiro_numero_session"]
            else:
                session["segundo_numero_session"] = numero_variavel
                ultima_interacao = session["segundo_numero_session"]
        
        #Atribui a variavél do python a sua respectiva session
        if operacao_variavel is not None:
            session["operacao_session"] = operacao_variavel
            ultima_interacao = session["operacao_session"]

        if acao_variavel is not None:
            session["acao_session"] = acao_variavel
            ultima_interacao = session["acao_session"]

        #Atribui a variavel ao valor da session naquela session, na session 
        # seguinte o valor muda
        primeiro_numero = session.get("primeiro_numero_session")
        segundo_numero = session.get("segundo_numero_session")
        operacao_variavel = session.get("operacao_session")

        #Tratamento para limpar o ultimo digito do usuário, seja 1, +, 7, -, 4...
        if ultima_interacao == "limpar":
            ultima_interacao = 0

        #Transforma o primeiro e segundo numero em inteiro. Calculadora AINDA não funciona com número não inteiro 
        if acao_variavel == "resultado":
            primeiro_numero = int(primeiro_numero)
            segundo_numero = int(segundo_numero)        

        #Calculo da calculadora (O cerebro de tudo)
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
      
            print(f"Primeiro dig.  :{primeiro_numero}")
            print(f"Operação sel.  :{operacao_variavel}")
            print(f"Segundo dig.   :{segundo_numero}")
            print(f"Resultado Fin. :{resultado}")


    return render_template("index.html", visor = ultima_interacao)

if __name__=="__main__":
    app.run()
