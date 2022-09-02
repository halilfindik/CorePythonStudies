"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
"""

print("""Beden Kitle Endesinizi tespit etmek için lütfen verileri giriniz...
**********************************************************************
""")
kilo = float(input("Kilonuzu Giriniz (kg)...: "))
boy = float(input("Boyunuzu giriniz (m)... : "))

bmi = kilo / boy ** 2

if bmi < 18.5 and bmi>0:
    print("Zayıf")

elif bmi>=18.5 and bmi<25:
    print("Normal")

elif bmi>=25 and bmi<30:
    print("Fazla Kilolu")

elif bmi>=30:
    print("Obez")

else:
    print("Hatalı değer girdiniz...")