def kilometrdan_metrga(km):
    return km * 1000

def metr_dan_santimetrga(metr):
    return metr * 100

def kilogrammdan_gramga(kg):
    return kg * 1000

if __name__ == "__main__":
    print("Kilometrdan metrga (5 km):", kilometrdan_metrga(5))
    print("Metrdan santimetrga (3 m):", metr_dan_santimetrga(3))
    print("Kilogrammdan grammga (2 kg):", kilogrammdan_gramga(2))
