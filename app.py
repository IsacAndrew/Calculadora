from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "calculadora_isac"

@app.route("/", methods=["GET", "POST"])

def rota():
    ultima_interacao = 0

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

        #Defini o primeiro numero da session e o segundo numero da session
        if numero_variavel is not None:
            if "primeiro_numero_session" not in session:
                session["primeiro_numero_session"] = numero_variavel
                ultima_interacao = session["primeiro_numero_session"]
            else:
                session["segundo_numero_session"] = numero_variavel
                ultima_interacao = session["segundo_numero_session"]
        
        #Atribui a session á variavel do python
        if operacao_variavel is not None:
            session["operacao_session"] = operacao_variavel
            ultima_interacao = session["operacao_session"]
            if ultima_interacao == "subtracao":
                ultima_interacao = "-"
            elif ultima_interacao == "multiplicacao":
                ultima_interacao = "X"
            else:
                ultima_interacao = "+"

        if acao_variavel is not None:
            session["acao_session"] = acao_variavel
            ultima_interacao = session["acao_session"]

        #Atribui a variavel ao valor da session naquela session, na session 
        #sequinte o valor muda
        primeiro_numero = session.get("primeiro_numero_session")
        segundo_numero = session.get("segundo_numero_session")
        operacao_variavel = session.get("operacao_session")

        #Temporário enquanto o visor não funciona,
        #só p ver se os valores estão indo certo
        print(session.get("primeiro_numero_session"))
        print(session.get("operacao_session"))
        print(session.get("segundo_numero_session"))
        print(f"Ultima interação = {ultima_interacao}")

        if ultima_interacao == "limpar":
            ultima_interacao = 0

    return render_template("index.html", visor = ultima_interacao)

# print("-=-"*10, "Calculadora", "-=-"*10)

# num_01 = int(input("Digite o seu primeiro número: "))
# num_02 = int(input("Digite o seu segundo número: "))

# print("-=-"*20)

# while True:

#      operacao = input("1 - Adição,\n"
#                       "2 - Subtração,\n"
#                       "3 - Multiplicação\n"
#                       "Selecione a operação: ")

#      if operacao != "1" and operacao != "2" and operacao != "3":
#          print("\033c", end="")  
#          print(f"Primeiro número selecionado: {num_01}\n"
#                f"Segundo número selecionado:  {num_02}\n") 
#          print("Selecione apenas as opções exibidas: 1, 2 ou 3")
#          continue
#      else:
#         break

# print("-=-"*20)

# if operacao == "1":

#     resultado = (num_01 + num_02)
#     print(f"A soma de {num_01} + {num_02} é igual a {resultado}")

# elif operacao == "2":

#     resultado = (num_01 - num_02)
#     print(f"A subtração de {num_01} - {num_02} é igual a {resultado}")

# else:

#     resultado = (num_01 * num_02)
#     print(f"A multiplicação de {num_01} * {num_02} é igual a {resultado}")

if __name__=="__main__":
    app.run()
