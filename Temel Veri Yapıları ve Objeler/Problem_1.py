"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
"""

a = float(input("Lütfen çarpılacak birinci sayıyı giriniz:"))
b = float(input("Lütfen çarpılacak ikinci sayıyı giriniz:"))
c = float(input("Lütfen çarpılacak üçüncü sayıyı giriniz:"))

d = a * b * c

print("Bu sayıların çarpımı {} 'dır.".format(d))
