from datetime import datetime
from time import strftime
from conexao import Conexao

class Model:
    def __init__(self):
        self.db_connection = Conexao().conectar()
        self.cur = self.db_connection.cursor(buffered=True)

    def inserir(self, nome, telefone, endereco, data_nascimento):
        try:
            comando = f"INSERT INTO person(codigo, nome, telefone, endereco, data_nascimento) VALUES('','{nome}','{telefone}','{endereco}','{data_nascimento}')"
            self.cur.execute(comando)
            self.db_connection.commit()

            return f"{self.cur.rowcount} linha(s) afetada(s)!"
        except Exception as error:
            print(error)

    def consultar(self, codigoConsulta):
        try:
            comando=f"SELECT * FROM person WHERE codigo='{codigoConsulta}'"
            self.cur.execute(comando)
            self.db_connection.commit()

            msg= ''
            for (codigo, nome, telefone, endereco, data_nascimento) in self.cur:
                msg = msg + f"Código: {codigo}\nNome: {nome}\nTelefone: {telefone}\nEndereço: {endereco}\nData de nascimento: {str(datetime.strftime(data_nascimento, '%d/%m/%Y'))}"
            return msg
        except Exception as error:
            return error