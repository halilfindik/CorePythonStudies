"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
"""

print("""(Sonlandırmak için q'ya basınız...)
""")

toplam = 0

while True:

    sayi = input("Bir Sayı Giriniz...:")
    if sayi == "q":
        print("Sayıların Toplamı :",int(toplam))
        print("Program sonlandırılıyor...")
        break
    if int(sayi) < 1:
        print("Lütfen 0'dan büyük bir sayı giriniz...")

    else:
        toplam += int(sayi)

