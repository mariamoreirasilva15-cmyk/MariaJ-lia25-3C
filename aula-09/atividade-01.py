from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produto")
def obter_produto():
    
    item = {
        "id": 1,
        "nome": "Sega Neon Genesis Evangelion asuka",
        "preco": 388,00
        "disponivel": True
    }
    return jsonify(item)

if __name__ == "__main__":
    app.run(debug=True)