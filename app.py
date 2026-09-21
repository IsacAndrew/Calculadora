from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def rota():
    if request.method == "POST":

        numero = request.form.get("numero")
        operacao = request.form.get("operacao")
        acao = request.form.get("acao")/quit

    return render_template("index.html")

print("-=-"*10, "Calculadora", "-=-"*10)

num_01 = int(input("Digite o seu primeiro número: "))
num_02 = int(input("Digite o seu segundo número: "))

print("-=-"*20)

while True:

     operacao = input("1 - Adição,\n"
                      "2 - Subtração,\n"
                      "3 - Multiplicação\n"
                      "Selecione a operação: ")

     if operacao != "1" and operacao != "2" and operacao != "3":
         print("\033c", end="")  
         print(f"Primeiro número selecionado: {num_01}\n"
               f"Segundo número selecionado:  {num_02}\n") 
         print("Selecione apenas as opções exibidas: 1, 2 ou 3")
         continue
     else:
        break

print("-=-"*20)

if operacao == "1":

    resultado = (num_01 + num_02)
    print(f"A soma de {num_01} + {num_02} é igual a {resultado}")

elif operacao == "2":

    resultado = (num_01 - num_02)
    print(f"A subtração de {num_01} - {num_02} é igual a {resultado}")

else:

    resultado = (num_01 * num_02)
    print(f"A multiplicação de {num_01} * {num_02} é igual a {resultado}")

if __name__=="__main__":
    app.run()