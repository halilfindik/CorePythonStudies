"""
Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

asallar = []

for i in range(2, 50000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        asallar.append(i)


a = 600851475143
b = 13195

i = 2
liste = [1]

while i <= b / i:
    x = b % i
    y = b % liste[-1]
    print("i :", i, "x :", x, "y :", y)
    if x == 0 and y == 0:
        liste.append(i)
        print(liste)
        print("")
    i += 1

print(liste)

liste_ters = liste[::-1]

print(liste_ters)

aralik = range(2, (liste[-1] + 1))

print(*aralik)

liste3 = []

for i in aralik:
    for j in liste_ters:
        if j % i == 0:
            liste3.append(j)
            print(liste3)

