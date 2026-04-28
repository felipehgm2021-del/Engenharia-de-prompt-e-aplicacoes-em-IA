import requests

url = "https://viacep.com.br/ws/01001000/json/"

print("Tentando conectar na API...")

try:
    response = requests.get(url)
    dados = response.json()
    print(f"Rua: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
except Exception as e:
    print(f"\n[ERRO DETECTADO]: {e}")