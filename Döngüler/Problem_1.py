"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""

print("""
************************************************
        Mükemmel Sayı Sorgulama Programı
************************************************""")
print("""(Sonlandırmak için q'ya basınız...)
""")

while True:

    toplam = 0
    sayi = input("Bir sayı giriniz (1'den büyük):")

    if sayi == "q":

        print("Program sonlandırılıyor...")
        break

    sayi = int(sayi)

    if sayi < 2:
        print("Lütfen 1'den büyük bir sayı giriniz...")
        continue

    else:
        for i in range(1,sayi):
            if (sayi%i) == 0:
                toplam += i
        if toplam == sayi:
            print("Girdiğiniz", sayi, "sayısı mükemmel bir sayıdır.")
        else:
            print("Girdiğiniz", sayi, "sayısı mükemmel bir sayı değildir.")
