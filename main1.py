import parol

uzunlik = int(input("Parol uzunligini kiriting: "))
yangi_parol = parol.parol_yarat(uzunlik)
print(f"Yaratilgan parol: {yangi_parol}")
print(f"Tekshiruv natijasi: {parol.parol_tekshir(yangi_parol)}")
