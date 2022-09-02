"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""

a = int(input("Dik üçgenin eşit kenarlarının uzunluğunu girin: "))

hipotenus = (2 * a**2) ** 0.5

print("Bu dik üçgenin hipotenüsü {}'dir".format(hipotenus))

