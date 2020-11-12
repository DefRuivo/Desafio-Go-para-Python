import requests
import json
from timeit import default_timer as timer


# https://digimon-api.vercel.app/api/digimon/
# https://digimon-api.vercel.app/api/digimon/name/

### Puxa lista de nomes da API

def requests_digimon():
    api_digimon_raw = requests.get('https://digimon-api.vercel.app/api/digimon/')
    api_digimon = api_digimon_raw.json()
    return api_digimon

### Cria um arquivo TXT para inserir os nomes

def criar_txt(api):      
    with open('digimon.txt', 'w') as arquivo:
        for name in api:
            arquivo.write(name['name']+'\n')

### Olha se o TXT existe, se der erro, cria um arquivo

def info_digimon():
    try:
        with open('digimon.txt', 'r'):
            pass
    except FileNotFoundError:
        criar_txt(requests_digimon())


### O desafio de fato:

def pegar_nomes():
    try:
        with open('digimon.txt', 'r') as arquivo:
            linhas = []
            for linha in arquivo.readlines():
                linhas.append(linha.replace('\n', ''))
            return linhas
    except:
        pass


def inicial():
    info_digimon() ### Envio da lista de Nomes da API pro TXT

    antes = timer()

    for numero, nome in enumerate(pegar_nomes()):
        conteudo = requests.get(f'https://digimon-api.vercel.app/api/digimon/name/{nome}')

    depois = timer()

    print(f' Duração: {depois - antes}')

inicial()