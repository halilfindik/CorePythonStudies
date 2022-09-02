print("""
************************
Kullanıcı Grişi Programı
************************
""")

sys_kullanıcı_adı = "hfindik"

sys_parolar = "12345"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı: ")
    parola = input("Parola :")
    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parolar):
        print("Kullanıcı Adı Hatalı!....")
        giriş_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parolar):
        print("Parola Hatalı!....")
        giriş_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parolar):
        print("Kullanıcı Adı ve Parola Hatalı!....")
        giriş_hakkı -= 1
    else:
        print("Sisteme Başarı ile giriş yapıldı...")
        break
    if (giriş_hakkı==0):
        print("Giriş hakkınız bitti")
        break