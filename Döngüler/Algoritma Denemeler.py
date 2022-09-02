sayi = int(input("Sayı Giriniz :"))

sayac = 0
n = 1

while True:
    if sayi / n < 1:
        print("sayı", sayac, "basamaklıdır.")
        break
    else:
        sayac = sayac + 1
        n = n * 10
