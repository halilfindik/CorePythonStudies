"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve
sürücünün toplam ne kadar ödemesi gerektiğini hesaplayın.
"""

birim_yakit = float(input("Aracınız km başı kaç TL benzin tüketmektedir? :"))
yol = float(input("Aracınızla kaç km yol yaptınız? :"))

harcama = yol * birim_yakit

print("Aracınız {} km yol boyunca {} TL yakıt tüketmiştir.".format(yol,harcama))
