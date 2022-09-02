"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

a = int(input("Birinci sayıyı girin : "))
b = int(input("İkinci sayıyı girin : "))

[a,b] = [b,a]

print(a,b)