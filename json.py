import json

d1 = {
    'Pessoa 1':{
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2':{
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dump(d1, ident=True)
print(d1_json)
