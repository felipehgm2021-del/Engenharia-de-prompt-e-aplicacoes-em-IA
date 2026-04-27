import requests

# URL COM ERRO (viacepx não existe) para a estratégia de IA
url_com_erro = "https://viacepx.com.br/ws/01001000/json/"

print("Tentando conectar na API...")

try:
    response = requests.get(url_com_erro)
    dados = response.json()
    print(dados)
except Exception as e:
    print(f"\n[ERRO DETECTADO]: {e}")
    print("Aguardando correção da IA...")
