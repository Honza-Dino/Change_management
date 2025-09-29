import pytest
from DPH.dph import vypocitej_cenu_s_dph


@pytest.mark.parametrize("vstup, ocekavany_vystup", [
    ("100", 121.00),
    ("1000.50", 1210.61),
    ("1", 1.21),
    ("55000", 66550.00),
    ("10.00", 12.10)
])
def test_spravny_vypocet_dph(vstup, ocekavany_vystup):
    skutecny_vysledek = vypocitej_cenu_s_dph(vstup)
    assert skutecny_vysledek == ocekavany_vystup
