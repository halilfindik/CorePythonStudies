print("""
**************************************
ATM MAKİNESİNE HOŞGELDİNİZ

İşlemler

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için Q'ya basınız...
**************************************
""")

bakiye = 1000

while True:
    işlem = input("İşlemi Seçiniz...: ")

    if (işlem == "q"):
        print("Yine bekleriz...")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} TL'dir.".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("Miktarı giriniz...:"))
        bakiye += miktar
    elif (işlem == "3"):
        miktar = int(input("Miktarı giriniz...:"))
        if (bakiye - miktar < 0):
            print("Daha düşük bir miktar giriniz!..")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem!...")