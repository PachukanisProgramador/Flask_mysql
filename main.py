from flask import Flask, render_template, request
from model import Model

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def inserir():
    resultado_comando=''
    modelo = Model()
    if request.method=='POST':
        nome=request.form['inputNome']
        telefone=request.form['inputTelefone']
        endereco=request.form['inputEndereco']
        data_nascimento_inserida=request.form['inputDataNascimento']

        resultado_comando=modelo.inserir(nome, telefone, endereco, data_nascimento_inserida)

    return  render_template("index.html", tituloIndex="Inserir", resultado=resultado_comando)

@app.route("/consulta", methods=['POST', 'GET'])
def consultar():
    codigo = 0
    modelo = Model()
    if request.method=='POST':
        codigo=request.form['inputCodigo']
        resultado_comando=modelo.consultar(codigo)
            
    return render_template('index.html', resultadoConsulta=resultado_comando)

if __name__ == "__main__":
    app.run(debug=True, port=5000)