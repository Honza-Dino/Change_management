import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("MAPY_API_KEY")

if not API_KEY:
    raise ValueError("API klíč 'MAPY_API_KEY' není nastaven v souboru .env.")


URL = "https://api.mapy.cz/v1/geocode"

def najdi_mesto(mesto: str):
    params = {
        "query": mesto,
        "apikey": API_KEY # Používáme klíč načtený z paměti
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


