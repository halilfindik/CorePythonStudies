"""
Problem 4

Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi
"""


def okunus(a):

    birler = {1: "BİR", 2: "İKİ", 3: "ÜÇ", 4: "DÖRT", 5: "BEŞ", 6: "ALTI", 7: "YEDİ", 8: "SEKİZ", 9: "DOKUZ", 0: ""}
    onlar = {1: "ON", 2: "YİRMİ", 3: "OTUZ", 4: "KIRK", 5: "ELLİ", 6: "ALTMIŞ", 7: "YETMİŞ", 8: "SEKSEN", 9: "DOKSAN"}

    t1 = int(a) // 10
    t2 = int(a) % 10

    return onlar[t1] + birler[t2]


x = input("İki basamaklı bir sayı giriniz :")

print("OKUNUŞU :", okunus(x))

