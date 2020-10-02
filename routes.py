from flask import Flask, request
from dataBase import insertUser

app = Flask("Minha API Python")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"Mensagem": "Olá Mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUser():
    body = request.get_json()
    if ("nome" not in body) or ("email" not in body) or ("senha" not in body):
        return geraResponse(400, "Os paramentros são obrigatorios")

    user = insertUser(body["nome"], body["email"], body["senha"])
    return geraResponse(200, "Usuario criado", "user", user)

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem
    
    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response

app.run()