"""
Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
Problem için şu siteye bakabilirsiniz;
http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
"""


def ebob(a, b):

    i = 1
    ebob_no = 1

    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            ebob_no = i
        i += 1
    return ebob_no


x = int(input("Sayı 1 :"))
y = int(input("Sayı 2 :"))

if ebob(x, y) < 2:
    print("EBOB'u bulunamamaktadır..")
else:
    print("EBOB :", ebob(x, y))
