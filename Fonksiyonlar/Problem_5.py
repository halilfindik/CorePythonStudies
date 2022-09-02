"""
Problem 5

1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
"""


def pisagor():
    liste = list()

    i = 1

    while i <= 100:
        j = 1
        while j <= 100:
            psg = (i ** 2 + j ** 2) ** (1 / 2)
            if psg * 10 % 10 == 0:
                liste.append((i, j))
            j += 1
        i += 1
    return liste


print(pisagor())
