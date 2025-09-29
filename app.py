import smtplib
from email.message import EmailMessage
import sys


class Zmena:

    def __init__(self, jmeno, prijmeni, mesto, stat, doprava, hotel, cena):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.mesto = mesto
        self.stat = stat
        self.doprava = doprava
        self.hotel = hotel
        self.cena = cena
        self.schvaleni_vedouci = False
        self.schvaleni_reditel = False
        self.schvaleni_jednatel = False


def odesli_email(prijemce, predmet, text):

    print(f"Odesílám e-mail na adresu: {prijemce}")
    print(f"Předmět: {predmet}")
    print(f"Text zprávy:\n{text}\n")


def vypocitej_cenu_s_dph(cena_str):
    try:
        cena_bez_dph = float(cena_str.strip())
        if cena_bez_dph < 0:
            # Přidáno pro robustnost, i když v zadání nebylo
            raise ValueError("Cena nesmí být záporná.")

        # 21% DPH
        cena_s_dph = cena_bez_dph * 1.21
        return round(cena_s_dph, 2)
    except ValueError:
        raise ValueError("Neplatná hodnota. Zadejte prosím cenu v číslech.")



def ziskej_vstup():

    jmeno = ""
    while not jmeno.strip():
        jmeno = input("Zadejte jméno: ")
        if not jmeno.strip():
            print("Chyba: Jméno nemůže být prázdné. Zadejte prosím platnou hodnotu.")

    prijmeni = ""
    while not prijmeni.strip():
        prijmeni = input("Zadejte příjmení: ")
        if not prijmeni.strip():
            print("Chyba: Příjmení nemůže být prázdné. Zadejte prosím platnou hodnotu.")

    mesto = ""
    while not mesto.strip():
        mesto = input("Zadejte město cílové destinace: ")
        if not mesto.strip():
            print("Chyba: Město nemůže být prázdné.")

    stat = ""
    while not stat.strip():
        stat = input("Zadejte stát cílové destinace: ")
        if not stat.strip():
            print("Chyba: Stát nemůže být prázdný.")

    doprava = ""
    while not doprava.strip():
        doprava = input("Zadejte druh dopravy: ")
        if not doprava.strip():
            print("Chyba: Doprava nemůže být prázdná.")

    hotel = ""
    while not hotel.strip():
        hotel = input("Zadejte název hotelu: ")
        if not hotel.strip():
            print("Chyba: Hotel nemůže být prázdný.")

    cena = None
    while cena is None:
        try:
            cena_str = input("Zadejte odhadovanou cenu bez DPH: ")

            if not cena_str.strip():
                print("Chyba: Cena nemůže být prázdná.")
                continue


            cena_s_dph = vypocitej_cenu_s_dph(cena_str)
            cena = cena_s_dph

            print(f"Cena s DPH: {cena} Kč")

        except ValueError as e:

            print(f"Chyba: {e}")
            print("Neplatná hodnota. Zadejte prosím cenu v číslech.")

    return Zmena(jmeno, prijmeni, mesto, stat, doprava, hotel, cena)


def schvalovaci_proces(zmena):

    # 1. Schválení vedoucím
    email_vedouciho = "vedouci@firma.cz"
    predmet_vedouci = "Nový požadavek na změnové řízení"
    text_vedouci = f"Prosím o schválení požadavku od {zmena.jmeno} {zmena.prijmeni} na cestu do {zmena.mesto}, {zmena.stat}."
    odesli_email(email_vedouciho, predmet_vedouci, text_vedouci)

    while True:
        odpoved = input("Vedoucí schválil? (ano/ne): ").lower().strip()
        if odpoved == "ano":
            zmena.schvaleni_vedouci = True
            print("Schváleno vedoucím. Pokračuji k řediteli.")
            break
        elif odpoved == "ne":
            print("Požadavek zamítnut vedoucím.")
            return
        else:
            print("Neplatná odpověď. Zadejte prosím 'ano' nebo 'ne'.")

    # 2. Schválení ředitelem
    email_reditel = "reditel@firma.cz"
    predmet_reditel = "Schválený požadavek na změnové řízení"
    text_reditel = f"Požadavek od {zmena.jmeno} {zmena.prijmeni} byl schválen vedoucím. Prosím o vaše schválení."
    odesli_email(email_reditel, predmet_reditel, text_reditel)

    while True:
        odpoved = input("Ředitel schválil? (ano/ne): ").lower().strip()
        if odpoved == "ano":
            zmena.schvaleni_reditel = True
            print("Schváleno ředitelem. Pokračuji k jednateli.")
            break
        elif odpoved == "ne":
            print("Požadavek zamítnut ředitelem.")
            return
        else:
            print("Neplatná odpověď. Zadejte prosím 'ano' nebo 'ne'.")

    # 3. Schválení jednatelem
    email_jednatel = "jednatel@firma.cz"
    predmet_jednatel = "Konečné schválení požadavku"
    text_jednatel = f"Požadavek od {zmena.jmeno} {zmena.prijmeni} byl schválen vedoucím i ředitelem. Prosím o konečné schválení."
    odesli_email(email_jednatel, predmet_jednatel, text_jednatel)

    while True:
        odpoved = input("Jednatel schválil? (ano/ne): ").lower().strip()
        if odpoved == "ano":
            zmena.schvaleni_jednatel = True
            print("Požadavek byl schválen jednatelem. Kompletní schválení!")
            break
        elif odpoved == "ne":
            print("Požadavek zamítnut jednatelem.")
            return
        else:
            print("Neplatná odpověď. Zadejte prosím 'ano' nebo 'ne'.")



if __name__ == "__main__":
    try:
        nova_zmena = ziskej_vstup()
        print("\n--- Spouštění schvalovacího procesu ---")
        schvalovaci_proces(nova_zmena)
    except Exception as e:
        print(f"\nDošlo k chybě při spuštění programu: {e}")
