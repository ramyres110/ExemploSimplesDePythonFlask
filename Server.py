#!\bin\python3

'''
Exemplo de servidor simples utilizando flask
'''
from dotenv import load_dotenv
from os import getenv
from flask import Flask, request, abort

dados = [
    {
        "id": 1,
        "nome": "Bob",
        "sexo": "M",
        "ativo": True
    },
    {
        "id": 2,
        "nome": "Alice",
        "sexo": "F",
        "ativo": False
    }
]

def proximo_id():
    max_id = dados[0]["id"]
    for usuario in dados:
        if max_id < usuario["id"]:
            max_id = usuario["id"]
    return max_id + 1;

def usuario_index_por_id(id):
    for index, usuario in enumerate(dados):
        if id == usuario["id"]:
            return index
    return None

PORT = int(getenv('PORT'))
print("Servidor escutando na porta {}".format(PORT))

app = Flask(__name__)

@app.get("/")
def index():
    return {}

# Verbo GET
# Lista todos os usuarios
@app.get("/api/v1/usuario")
def lista_usuarios():
    return dados # Resposta, Status Code

# Verbo GET
# Retorna usuário por id
@app.get("/api/v1/usuario/<int:id>")
def obter_usuario_por_id(id):
    indice = usuario_index_por_id(id)
    if indice != None:
        return dados[indice], 200 # Resposta, Status Code
    abort(404)

# Verbo POST
# Adiciona usuário
@app.post("/api/v1/usuario")
def adiciona_usuario():
    usuario = request.get_json() # JSON no corpo da requisição
    print(type(usuario))
    usuario["id"] = proximo_id()    
    dados.append(usuario) # salva usuário
    return usuario, 201 # Resposta, Status Code

# Verbo PUT
# Altera dados de um usuário
@app.put("/api/v1/usuario/<int:id>")
def altera_usuario(id):
    indice = usuario_index_por_id(id)
    if indice != None:
        usuario = request.get_json()
        usuario["id"] = id
        dados[indice] = usuario
        return usuario, 202 # Resposta, Status Code
    abort(404)

# Verbo DELET
# Exclui usuário por id
@app.delete("/api/v1/usuario/<int:id>")
def exclui_usuario(id):
    indice = usuario_index_por_id(id)
    if indice != None:
        dados.pop(indice)
        return {}, 202 # Resposta, Status Code
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return '', 404
