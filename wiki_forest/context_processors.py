import requests


def user_info(request):
    return {
        'user_type': request.session.get('user_type'),
        'user_name': request.session.get('user_name'),
        'user_email': request.session.get('user_email'),
        'user_phone': request.session.get('user_phone'),
        'user_country': request.session.get('user_country'),
        'user_id' : request.session.get('user_id'),
    }
    
    
def valor_dolar(request):
    try:
        response = requests.get('https://cl.dolarapi.com/v1/cotizaciones/usd', timeout=5)
        if response.status_code == 200:
            data = response.json()
            valor_dolar = data['compra']
            return {
                'valor_dolar': valor_dolar
            }
        else:
            return {
                'valor_dolar': None
            }
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el valor del dólar: {e}")
        return {
            'valor_dolar': None
        }


import requests

def valor_criptomonedas(request):
    try:
        response = requests.get('https://api.coinlore.net/api/ticker/?id=90,80', timeout=5)
        if response.status_code == 200:
            data = response.json()
            valor_bitcoin = None
            valor_ethereum = None

            for moneda in data:
                if moneda['id'] == '90':  # Bitcoin
                    valor_bitcoin = float(moneda['price_usd'])
                elif moneda['id'] == '80':  # Ethereum
                    valor_ethereum = float(moneda['price_usd'])

            return {
                'valor_bitcoin': valor_bitcoin,
                'valor_ethereum': valor_ethereum
            }
        else:
            return {
                'valor_bitcoin': None,
                'valor_ethereum': None
            }
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los valores de las criptomonedas: {e}")
        return {
            'valor_bitcoin': None,
            'valor_ethereum': None
        }