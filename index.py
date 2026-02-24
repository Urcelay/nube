from flask import Flask

# crea una aplicación Flask
app = Flask(__name__)

# ruta principal
@app.route("/")
def hello():
    return "¡Lilian rá a ver a Shakira!"

if __name__ == "__main__":
    # se ejecuta en localhost:5000 por defecto
    app.run()
