from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Hola desde EC2</h1>"

@app.route("/pagina_registro")
def pagina_registro():
    return render_template("registro.html")

if __name__ == '__main__':
    host = "0.0.0.0"
    port = "80"
    app.run(host, port)
