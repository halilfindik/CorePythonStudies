"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""

print("""**************************
Geometrik Şekil Hesaplama
**************************""")

sekil = input("Üçgen mi dörtgen mi?")

if sekil == "dörtgen":
    print("Dört kenarı giriniz...")
    d1 = input("1.Kenar uzunluğunu giriniz...")
    d2 = input("2.Kenar uzunluğunu giriniz...")
    d3 = input("3.Kenar uzunluğunu giriniz...")
    d4 = input("4.Kenar uzunluğunu giriniz...")
    


elif sekil == "üçgen":
    print("Üç kenarı giriniz...")
    u1 = input("1.Kenar uzunluğunu giriniz...")
    u2 = input("2.Kenar uzunluğunu giriniz...")
    u3 = input("3.Kenar uzunluğunu giriniz...")