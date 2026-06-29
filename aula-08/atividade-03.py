from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return "Seja muito bem-vindo à nossa API de testes!"

@app.route("/data")
def mostrar_data():
    
    hoje = date.today()
    
    data_formatada = hoje.strftime("%d/%m/%Y")  #data no brasil!!!!!!!!
    
    return f"A data de hoje é: {data_formatada}"

if __name__ == "__main__":
    app.run(debug=True)