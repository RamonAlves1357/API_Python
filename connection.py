import mysql.connector

def criar_conexao(host, user, senha, banco):
    return mysql.connector.connect(host=host, user=user, password=senha, database=banco)

def fechar_conexao(con):
    return con.close()