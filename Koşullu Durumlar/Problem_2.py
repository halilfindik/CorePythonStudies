"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""

a = float(input("Birinci Sayıyı Giriniz...: "))
b = float(input("İkinci Sayıyı Giriniz...: "))
c = float(input("Üçüncü Sayıyı Giriniz...: "))

if a > b and a > c:
    print(a)

elif b > a and b > c:
    print(b)

elif c > a and c > b:
    print(c)

else:
    print("Eşit sayı girdiniz...")




print(max(a,b,c))

