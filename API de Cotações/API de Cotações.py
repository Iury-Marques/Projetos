import requests

Url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

try:
    response = requests.get(Url)

    if response.status_code == 200:
        data = response.json()
        usd_brl = data['USDBRL']['bid']
        eur_brl = data['EURBRL']['bid']
        print(f"USD to BRL: {usd_brl}")
        print(f"EUR to BRL: {eur_brl}")

    else:
        print(f"Error: {response.status_code} - {response.reason}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")