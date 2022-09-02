"""
Problem 9 - Special Pythagorean Triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product a*b*c.
"""


for i in range(100, 500):
    for j in range(100, 500):
        for k in range(100, 999):
            if (i ** 2 + j ** 2) == k ** 2 and i + j + k == 1000 and k > j > i:
                print("i :", i, "j :", j, "k :", k)
                print(i * j * k)

