"""
ullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.
"""

vize1 = int(input("1. Vize Notunuzu giriniz...: "))
vize2 = int(input("2. Vize Notunuzu giriniz...: "))
final = int(input("Final Notunuzu giriniz...: "))

n = vize1 * 0.3 + vize2 * 0.3 + final * 0.4

print(n)

if vize1 > 100 or vize2 > 100 or final > 100:
    print("Hatalı Not Girişi")
elif vize1 < 0 or vize2 < 0 or final < 0:
    print("Hatalı Not Girişi")


elif n >= 90 and n < 100:
    print("Notunuz AA'dır.")
elif n >= 85 and n < 90:
    print("Notunuz BA'dır.")
elif n >= 80 and n < 85:
    print("Notunuz BB'dir.")
elif n >= 75 and n < 80:
    print("Notunuz CB'dir.")
elif n >= 70 and n < 75:
    print("Notunuz CC'dir.")
elif n >= 65 and n < 70:
    print("Notunuz DC'dir.")
elif n >= 60 and n < 65:
    print("Notunuz DD'dir.")
elif n >= 55 and n < 100:
    print("Notunuz FD'dir.")
elif n >= 0 and n < 55:
    print("Notunuz FF'dir.")

else:
    print("Hatalı not girişi...")