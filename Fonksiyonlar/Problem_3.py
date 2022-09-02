"""
Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
Problem için şu siteye bakabilirsiniz;
http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
"""


def ekok(a, b):

    i = 1
    ekok_no = []

    while i <= a*b:
        if i % a == 0 and i % b == 0:
            ekok_no.append(i)
        i += 1
    return ekok_no[0]


x = int(input("Sayı 1 :"))
y = int(input("Sayı 2 :"))

print("EKOK :", ekok(x, y))
