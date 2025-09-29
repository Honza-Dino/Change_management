import pytest
from

@pytest.mark.parametrize("vstup, ocekavany_vystup", [
    ("100", 121.00),
    ("1000.50", 1210.61),
    ("1", 1.21),
    ("55000", 66550.00),
    ("10.00", 12.10)
])
def test_spravny_vypocet_dph(vstup, ocekavany_vystup):
    # Skutečný výsledek z testované funkce
    skutecny_vysledek = vypocitej_cenu_s_dph

    # Kontrola, zda se výsledek shoduje s očekávaným výstupem
    assert skutecny_vysledek == ocekavany_vystup


def test_vypocet_nula():
    # Test, zda nula vrací nulu
    assert vypocitej_cenu_s_dph("0") == 0.00


def test_vypocet_desetinne_cislo():
    # Test ceny s desetinnou čárkou/tečkou
    # 5.50 * 1.21 = 6.655 -> 6.66
    assert vypocitej_cenu_s_dph("5.50") == 6.66