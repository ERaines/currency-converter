import requests


def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Throws an error if the response is 4xx or 5xx
        data = response.json()

        result = data.get("result")
        if result is None:
            raise ValueError("Error fetching conversion rate.")

        return result

    except resquests.exceptions.RequestsException as e:
        print("Error connecting to the API", e)
        return None
