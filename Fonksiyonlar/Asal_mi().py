"""
Asal Sayılar Bulma
"""


def asal_mi(x):
    if x == 1:
        return False
    elif x == 2:
        return True

    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


while True:
    sayi = input("Sayı Giriniz:")

    if sayi == "q":
        break
    else:
        sayi = int(sayi)

        if asal_mi(sayi):
            print(sayi, "asal bir sayıdır.")
        else:
            print(sayi, "asal bir sayı değildir.")
