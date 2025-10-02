import requests

API_KEY = "XFF10pwXd6fSYk0c4tBX-yYpYmiZ1p_gYHOB0F3C6p8"
URL = "https://api.mapy.cz/v1/geocode"

def najdi_mesto(mesto: str):
    params = {
        "query": mesto,
        "apikey": API_KEY
    }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()

        if data.get("items"):
            prvni = data["items"][0]


            nazev = (
                prvni.get("name")
                or prvni.get("title")
                or prvni.get("formatted")
                or prvni.get("label")
                or "Neznámý název"
            )

            return {
                "nazev": nazev,
                "souradnice": prvni.get("position")
            }
        else:
            return None
    else:
        raise Exception(f"Chyba API: {response.status_code} - {response.text}")


