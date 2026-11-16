def soz_qosh(lugat, soz, tarjima):
    lugat[soz.lower()] = tarjima.lower()

def soz_qidir(lugat, soz):
    return lugat.get(soz.lower(), "Bunday so'z topilmadi")

def lugatni_kor(lugat):
    for soz, tarjima in lugat.items():
        print(f"{soz} - {tarjima}")
