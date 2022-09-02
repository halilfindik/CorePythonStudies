print("""********************************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
*********************************
""")

a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))

islem = input("İşlemi Giriniz: ")

if islem == "1":
    print("{} ile {}'nin toplamı {}'dir.".format(a,b,a+b))

elif islem == "2":
    print("{} ile {}'nin farkı {}'dir.".format(a,b,a-b))

elif islem == "3":
    print("{} ile {}'nin çarpımı {}'dir.".format(a,b,a * b))

elif islem == "4":
    print("{} ile {}'nin bölümü {}'dir.".format(a,b,a/b))

else:
    print("Geçersiz işlem!...")