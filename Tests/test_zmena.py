import pytest
from app import Zmena  # Importujeme pouze třídu Zmena

def test_inicializace_objektu_zmena():

    test_zmena = Zmena(
        jmeno="Anna",
        prijmeni="Krala",
        mesto="Brno",
        stat="Česko",
        doprava="Letadlo",
        hotel="Grand",
        cena=5000.00
    )

    assert test_zmena.jmeno == "Anna"
    assert test_zmena.stat == "Česko"
    assert test_zmena.cena == 5000.00

    assert test_zmena.schvaleni_vedouci is False
    assert test_zmena.schvaleni_reditel is False
    assert test_zmena.schvaleni_jednatel is False
