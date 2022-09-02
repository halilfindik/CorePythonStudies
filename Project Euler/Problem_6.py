"""
Problem 6 - Sum Square Difference

The sum of the squares of the first ten natural numbers is,
12+22+...+102=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

a = range(1,101)
toplam1 = sum(i ** 2 for i in a)
toplam2 = sum(i for i in a) ** 2

fark = toplam1 - toplam2

print(fark)
