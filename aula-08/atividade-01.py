from flask import Flask

app = Flask(__name__)

@app.route("/")
def meu_nome():
    return "Gal Costa"
    
if __name__ == "__main__":
    app.run(debug=True)