print(12 // 10)
print(12 % 10)
sayi = int(input("Sayı Giriniz :"))

birler = 0
ters = 0

while True:
    if sayi % 10 < 1:
        print("Sayı'nın Tersi :", ters)
        break
    else:
        birler = sayi % 10
        ters = ters * 10 + birler
        sayi = sayi // 10


