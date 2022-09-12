from datetime import datetime
from flask import Flask, render_template, request
from model import Model as modelo

class Routes:
    def __init__(self):
        self.modelo = modelo()
        self.app = Flask(__name__)

        @self.app.route("/", methods=["POST", "GET"])
        def inserir():
            resultado_comando=''
            if request.method=='POST':
                nome=request.form['inputNome']
                telefone=request.form['inputTelefone']
                endereco=request.form['inputEndereco']
                data_nascimento_inserida=request.form['inputDataNascimento']

                resultado_comando=self.modelo.inserir(nome, telefone, endereco, data_nascimento_inserida)

            return  render_template("index.html", tituloIndex="Inserir", resultado=resultado_comando)

        @self.app.route("/consulta", methods=['POST', 'GET'])
        def consultar():
            codigo = 0
            if request.method=='POST':
                codigo=request.form['inputCodigo']
                resultado_comando=self.modelo.consultar(codigo)
            
            return render_template('index.html', resultadoConsulta=resultado_comando)
