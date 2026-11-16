import lugat

sozlar = {}

lugat.soz_qosh(sozlar, "apple", "olma")
lugat.soz_qosh(sozlar, "book", "kitob")
lugat.soz_qosh(sozlar, "car", "mashina")
lugat.soz_qosh(sozlar, "dog", "it")
lugat.soz_qosh(sozlar, "sun", "quyosh")

print("Tarjima:", lugat.soz_qidir(sozlar, "apple"))
print("\nBarcha lug'at:")
lugat.lugatni_kor(sozlar)
