import requests


def LoginRouter(rota, valor):
    # pega o ID do roteador inserido
    request = requests.get(rota+valor)
    a = request.json()
    id = a[0]["id"]

    # compara a ID do roteador com a tabela roteador_id em roteadorLogin, se for igual, retorna em forma de lista as possiveis senhas
    request_final = requests.get('http://20.172.148.56:8080/roteadorLogin/')
    b = request_final.json()
    list_senhas = []
    for c in b:
        id_final = c["roteador_id"]
        if id == id_final:
            list_senhas.append({"user": c["usuario"], "senha": c["senha"]})


LoginRouter('http://20.172.148.56:8080', f'/roteador/?search=ws5200')
