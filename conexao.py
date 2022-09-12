import mysql.connector

class Conexao:
    def __init__(self):
        pass

    def conectar(self):
        try:
            db_connection = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="bancoFlask") #localhost
            return db_connection
        except Exception as error:
            print(error)