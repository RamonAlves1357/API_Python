def insertUser(con, nome, email, senha):
    cursor = con.cursor()
    sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def Listar_Users(con):
    cursor = con.cursor()
    sql = "SELECT id, nome, email FROM usuario"
    cursor.execute(sql)
    for (id, nome, email) in cursor:
        return { "id": id, "nome": nome, "email": email}
    cursor.close()
    