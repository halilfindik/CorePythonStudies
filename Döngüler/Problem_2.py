"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

print("""
***********************************************
        Armstrong Sayısı Bulma Programı
***********************************************
""")
print("""(Sonlandırmak için q'ya basınız...)
""")

while True:

    toplam = 0
    sayi = input("Bir Sayı Giriniz...:")

    if sayi == "q":

        print("Program sonlandırılıyor...")
        break
    if int(sayi) < 0:
        print("Lütfen 0 ya da daha büyük bir sayı giriniz...")
        continue

    else:
        basamak = len(sayi)
        int_sayi = int(sayi)

        for i in sayi:
            toplam += int(i) ** basamak
        if toplam == int_sayi:
            print("Girdiğiniz", int_sayi, "sayısı Armstrong sayısıdır.")
        else:
            print("Girdiğiniz", int_sayi, "sayısı Armstrong sayısı değildir.")