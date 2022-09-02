"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""

kilo = float(input("Kilonuzu giriniz (kg):"))
boy = float(input("Boyunuzu giriniz (m):"))

bki = kilo / boy**2

print("Beden Kitle Endeksiniz {}'tir.".format(bki))
