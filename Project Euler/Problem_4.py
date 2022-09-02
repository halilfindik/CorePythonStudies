"""
Problem 4 - Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrom = []

for i in range(100, 1000):
    for j in range(100, 1000):
        carpim = i * j
        carpim_str = str(carpim)
        carpim_liste = list(carpim_str)
        carpim_liste_ters = carpim_liste[::-1]
        if carpim_liste == carpim_liste_ters:
            palindrom.append(carpim)
            print("i :", i, "j :", j, "Palindrom :", carpim)


print("Largest 3-Digit Palindrom :", max(palindrom))
