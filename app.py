from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = "calculadora_isac"

@app.route("/", methods=["GET", "POST"])

def rota():
    if request.method == "POST":

        #Lê dados enviados pelo botão no HTML
        acao_variavel = request.form.get("acao_html")

        #Limpa sessão, melhor deixar aqui em cima pq lá em baixo o usuário teria
        # que clicar duas vezes pois no primeiro clique ele iria 
        if acao_variavel == "limpar":
            session.clear()

        #Lê dados enviados pelo botão no HTML
        operacao_variavel = request.form.get("operacao_html")
        numero_variavel = request.form.get("numero_html")

        #Separa o primeiro numero da session e o segundo numero da session
        if numero_variavel is not None:
            if "primeiro_numero_session" not in session:
                session["primeiro_numero_session"] = numero_variavel
            else:
                session["segundo_numero_session"] = numero_variavel

        #Temporário enquanto o visor não funciona,
        #só p ver se os valores estão indo certo
        print(session.get("primeiro_numero_session"))
        print(session.get("operacao_session"))
        print(session.get("segundo_numero_session"))

        #Atribui a session á variavel do python
        if operacao_variavel is not None:
            session["operacao_session"] = operacao_variavel
        if acao_variavel is not None:
            session["acao_session"] = acao_variavel

        #Atribui a variavel ao valor da session naquela session, na session 
        #sequinte o valor muda

        primeiro_numero = session.get("primeiro_numero_session")
        segundo_numero = session.get("segundo_numero_session")
        operacao_variavel = session.get("operacao_session")

        #Não seria melhor deixar a linha 38 a 40 fora desse IF, pq ai o valor 
        #da session vai existir mesmo se o usuário não clicar em resultado. 
        #Ou tanto faz? Eis a questão

        if acao_variavel == "resultado":
            print("Só p prencher msm")


    return render_template("index.html")

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
