import connection

# Criando conexao com o banco de dados
con = connection.criar_conexao("localhost", "root", "", "API_Python")

class User(object):
    # Definindo os tipos dos parametros (Types Annotations)
    def insert(self, nome: str, email: str, senha: str):
        cursor = con.cursor()
        sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
        valores = (nome, email, senha)
        cursor.execute(sql, valores)
        cursor.close()
        con.commit()
        
        # Fechando conexao com o banco de dados
        connection.fechar_conexao(con)

    def lists(self):
        cursor = con.cursor()
        sql = "SELECT id, nome, email FROM usuario"
        cursor.execute(sql)
        
        for (id, nome, email) in cursor:
            user = {
                "id": id, 
                "nome": nome, 
                "email": email
            }
            
            return user
            
        cursor.close()
        
        # Fechando conexao com o banco de dados
        connection.fechar_conexao(con)
        