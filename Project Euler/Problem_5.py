"""
Problem 5 - Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

asallar = []

for i in range(2, 21):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        asallar.append(i)

print(asallar)

carpim = 1

for i in range(2, 11):
    for j in asallar:
        i += 1

i = 0
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sayi = 2

while False:
    if sayi % liste[i] == 0:
        i += 1
    sayi += 2
    break


print("En Küçük Bölen :", sayi)
