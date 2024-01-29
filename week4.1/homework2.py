kullanici_adi = input("Kullanıcı adınızı giriniz: ")
sifre = input("Bir şifre oluşturunuz: ")

if len(sifre) >= 6:
    print("Hesabınız oluşturuldu.")
else:
    print("Lütfen altı haneli bir şifre oluşturunuz.")
