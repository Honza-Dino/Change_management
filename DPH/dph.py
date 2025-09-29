#cena_bez_dph = 100


def vypocitej_cenu_s_dph(cena_bez_dph_str):
    cena_bez_dph = float(cena_bez_dph_str)
    sazba_dph = 0.21
    cena_s_dph = cena_bez_dph * (1 + sazba_dph)
    return round(cena_s_dph, 2)

