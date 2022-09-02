print("""***************************
Kullanıcı Girişi
***************************
""")

sys_kullanici_adi = "mmurat"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adı: ")
parola = input("Parola: ")

if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("Hatalı Parola!...")

elif (kullanici_adi != sys_kullanici_adi and sys_parola == parola):
    print("Hatalı Kullanıcı Adı!...")

elif (kullanici_adi != sys_kullanici_adi and sys_parola != parola):
    print("Kullancı Adı ve Parola Hatalı!...")

else:
    print("Sisteme Başarıyla Giriş Yapıldı...")