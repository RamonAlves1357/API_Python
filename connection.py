from mysql import connector

def criar_conexao(host, user, senha, banco):
    mydb = connector.connect(
        host=host, 
        user=user, 
        password=senha, 
        database=banco
    )
    
    return mydb

def fechar_conexao(con):
    return con.close()