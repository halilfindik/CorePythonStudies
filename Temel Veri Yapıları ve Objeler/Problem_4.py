"""
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""

print("Merhaba\nBen Kullanıcı Kayıt Asistanınızım\nLütfen Aşağıdaki Bilgileri Giriniz.")

Ad = input("İsim Giriniz: ")
Soyad = input("Soyad Giriniz: ")
Telefon = int(input("Telefon No Giriniz : "))

print("\nAdı\t\t\tSoyadı\t\t\tTelefonu\n------------------------------------")
print("{}\t\t{}\t\t\t{}".format(Ad,Soyad,Telefon))
