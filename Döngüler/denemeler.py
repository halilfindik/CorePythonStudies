

liste1 = [*range(1,101)]

liste2 = [i*3 for i in liste1 if (i%2) == 0 if i % 5 == 1]

print(liste2)