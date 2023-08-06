
import requests

def consultar_dni(api_token, numero_dni):
    url = f"https://api.apis.net.pe/v2/reniec/dni?numero={numero_dni}"
    headers = {
        "Referer": "https://apis.net.pe/consulta-dni-api",
        "Authorization": f"Bearer {api_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al realizar la consulta. Código de estado:", response.status_code)
        return None

# Coloca tu token y el número de DNI a consultar
TOKEN = "apis-token-5140.0DFWA-3vI4IC854uxjcAEjh2q-A12rQ-"
numero_dni_consultar = "42388604"

resultado = consultar_dni(TOKEN, numero_dni_consultar)
if resultado:
    print("Resultado:")
    print(resultado)
