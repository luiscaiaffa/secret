from app import app
from sanic.response import json
from pycpfcnpj import cpfcnpj


@app.route('/<cpf>')
async def base_a(request, cpf):
    result = await app.mongo['test'].basea.find_one({'cpf': cpf})
    if not cpf or not cpfcnpj.validate(cpf) or not result:
        return json({'Error': f'CPF {cpf} does not exist or invalid'}, 400, headers={'Content-type': 'application/json'})
    return json(result, 200)


@app.listener('after_server_start')
async def notify_server_started(app, loop):
    doc = {
        "_id": 1,
        "nome": "Teste A",
        "cpf": "97512625189",
        "dividas": [
            {
                "_id": 1,
                "tipo": "tipo 1",
                "nome": "Divida exemplo"
            },
            {
                "_id": 2,
                "tipo": "tipo 2",
                "nome": "Divida exemplo"
            }
        ],
        "endereço": [
            {
                "estado": "RJ",
                "cidade": "Rio de Janeiro",
                "rua": "Rua Alegrete",
                "numero": 101,
                "cep": "0000000"
            }
        ]
    }
    await app.mongo['test']["basea"].save(doc)
