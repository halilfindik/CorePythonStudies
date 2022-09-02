def okunusu(a):
    birler = {1: "BİR", 2: "İKİ", 3: "ÜÇ", 4: "DÖRT", 5: "BEŞ", 6: "ALTI", 7: "YEDİ", 8: "SEKİZ", 9: "DOKUZ", 0: ""}
    onlar = {1: "ON", 2: "YİRMİ", 3: "OTUZ", 4: "KIRK", 5: "ELLİ", 6: "ALTMIŞ", 7: "YETMİŞ", 8: "SEKSEN", 9: "DOKSAN",
             0: ""}
    yuzler = {1: "YÜZ", 2: "İKİYÜZ", 3: "ÜÇYÜZ", 4: "DÖRTYÜZ", 5: "BEŞYÜZ", 6: "ALTIYÜZ", 7: "YEDİYÜZ", 8: "SEKİZYÜZ",
              9: "DOKUZYÜZ", 0: ""}
    binler = {1: "BİN", 2: "İKİBİN", 3: "ÜÇBİN", 4: "DÖRTBİN", 5: "BEŞBİN", 6: "ALTUBİN", 7: "YEDİBİN", 8: "SEKİZBİN",
              9: "DOKUZBİN", 0: ""}
    onbinler = {1: "ONBİN", 2: "YİRMİ", 3: "OTUZ", 4: "KIRK", 5: "ELLİ", 6: "ALTMIŞ", 7: "YETMİŞ", 8: "SEKSEN",
                9: "DOKSAN", 0: ""}
    yuzbinler = {1: "ON", 2: "YİRMİ", 3: "OTUZ", 4: "KIRK", 5: "ELLİ", 6: "ALTMIŞ", 7: "YETMİŞ", 8: "SEKSEN",
                 9: "DOKSAN", 0: ""}
    milyonlar = {1: "ON", 2: "YİRMİ", 3: "OTUZ", 4: "KIRK", 5: "ELLİ", 6: "ALTMIŞ", 7: "YETMİŞ", 8: "SEKSEN",
                 9: "DOKSAN", 0: ""}
    onmilyonlar = {1: "ON", 2: "YİRMİ", 3: "OTUZ", 4: "KIRK", 5: "ELLİ", 6: "ALTMIŞ", 7: "YETMİŞ", 8: "SEKSEN",
                   9: "DOKSAN", 0: ""}
    yuzmilyonlar = {1: "ON", 2: "YİRMİ", 3: "OTUZ", 4: "KIRK", 5: "ELLİ", 6: "ALTMIŞ", 7: "YETMİŞ", 8: "SEKSEN",
                    9: "DOKSAN", 0: ""}
    milyarlar = {1: "ON", 2: "YİRMİ", 3: "OTUZ", 4: "KIRK", 5: "ELLİ", 6: "ALTMIŞ", 7: "YETMİŞ", 8: "SEKSEN",
                 9: "DOKSAN"}

    t1 = int(a) % 10
    t2 = int(a) // 10
    t3 = int(a) // 100
    t4 = int(a) // 1000
    t5 = int(a) // 10000
    t6 = int(a) // 100000
    t7 = int(a) // 1000000
    t8 = int(a) // 10000000
    t9 = int(a) // 100000000
    t10 = int(a) // 1000000000

    return onbinler[t5] + binler[t4] + yuzler[t3] + onlar[t2] + birler[t1]


x = input("Bir sayı giriniz :")

print("OKUNUŞU :", okunusu(x))
