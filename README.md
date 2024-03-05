# Servidor Exemplo em Flask
Servidor de exemplo utilizando Flask.

## Dicas

* Utilize o VSCode
* Instale no VSCode as extenções:
    - Python - Microsoft
    - Markdown Preview Github Styling - Matt Bierner
    - REST Client - Huachao Mao
    - indent-rainbow - oderwat
* Utilize o REST Client para executar o arquivo `Requests.rest`

## Get Started

1. Utilize o venv

```
python -m venv .
```

2. Instale as dependências

```
pip install -r requirements.txt
```

3. Execute

```
flask --app Server run --debug
```

## API

### Rotas

Host: localhost
Port: 8081
Path: /api/v1/

### Recursos

#### /usuario

`localhost:8081/api/v1/usuario`

- GET: Lista todos os usuários
- GET /id: Usuário por id
- POST: Adiciona usuário
- PUT /id: Altera usuário
- DELETE /id: Exclui usuário


