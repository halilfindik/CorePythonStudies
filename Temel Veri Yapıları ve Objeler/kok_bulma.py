"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı hesaplama : b ** 2 - 4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)

"""
print("a*x^2 + b*x + c şeklindeki formüle ilişkin aşağıdaki değerleri giriniz..")
a = float(input("a değerini girin:"))
b = float(input("b değerini girin:"))
c = float(input("c değerini girin:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

print("Birinci.Kök: {}\nİkinci Kök: {}".format(x1,x2))
