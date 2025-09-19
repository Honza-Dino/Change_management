import smtplib
from email.message import EmailMessage


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
    # Sem později vložím modul smtplib pro reálné odeslání


def ziskej_vstup():
    jmeno = input("Zadejte jméno: ")
    prijmeni = input("Zadejte příjmení: ")
    mesto = input("Zadejte město cílové destinace: ")
    stat = input("Zadejte stát cílové destinace: ")
    doprava = input("Zadejte druh dopravy: ")
    hotel = input("Zadejte název hotelu: ")
    cena = input("Zadejte odhadovanou cenu: ")

    return Zmena(jmeno, prijmeni, mesto, stat, doprava, hotel, cena)


def schvalovaci_proces(zmena):
    # 1. Schválení vedoucím
    email_vedouciho = "vedouci@firma.cz"
    predmet_vedouci = "Nový požadavek na změnové řízení"
    text_vedouci = f"Prosím o schválení požadavku od {zmena.jmeno} {zmena.prijmeni} na cestu do {zmena.mesto}, {zmena.stat}."
    odesli_email(email_vedouciho, predmet_vedouci, text_vedouci)

    # Simulační část - zde by se čekalo na reálnou odpověď
    odpoved = input("Vedoucí schválil? (ano/ne): ")
    if odpoved.lower() == "ano":
        zmena.schvaleni_vedouci = True
        print("Schváleno vedoucím. Pokračuji k řediteli.")
    else:
        print("Požadavek zamítnut vedoucím.")
        return

    # 2. Schválení ředitelem
    email_reditel = "reditel@firma.cz"
    predmet_reditel = "Schválený požadavek na změnové řízení"
    text_reditel = f"Požadavek od {zmena.jmeno} {zmena.prijmeni} byl schválen vedoucím. Prosím o vaše schválení."
    odesli_email(email_reditel, predmet_reditel, text_reditel)

    odpoved = input("Ředitel schválil? (ano/ne): ")
    if odpoved.lower() == "ano":
        zmena.schvaleni_reditel = True
        print("Schváleno ředitelem. Pokračuji k jednateli.")
    else:
        print("Požadavek zamítnut ředitelem.")
        return

    # 3. Schválení jednatelem
    email_jednatel = "jednatel@firma.cz"
    predmet_jednatel = "Konečné schválení požadavku"
    text_jednatel = f"Požadavek od {zmena.jmeno} {zmena.prijmeni} byl schválen vedoucím i ředitelem. Prosím o konečné schválení."
    odesli_email(email_jednatel, predmet_jednatel, text_jednatel)

    odpoved = input("Jednatel schválil? (ano/ne): ")
    if odpoved.lower() == "ano":
        zmena.schvaleni_jednatel = True
        print("Požadavek byl schválen jednatelem. Kompletní schválení!")
    else:
        print("Požadavek zamítnut jednatelem.")


# Spuštění programu
if __name__ == "__main__":
    nova_zmena = ziskej_vstup()
    schvalovaci_proces(nova_zmena)