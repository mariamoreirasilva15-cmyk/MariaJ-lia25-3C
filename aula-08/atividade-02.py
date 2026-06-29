from flask import Flask

app = Flask(__name__)

@app.route("/")
def bem_vindo():
    return "Bem-vindo"

@app.route("/curso")
def curso():
    
    return "desenvolvimento de sistemas"

@app.route("/escola")
def escola():
   
    return "ceep"

if __name__ == "__main__":
    app.run(debug=True)