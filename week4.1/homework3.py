while True:
    kullanici_adi = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Bir şifre oluşturunuz: ")

    if 5 <= len(sifre) <= 10:
        print("Hesabınız oluşturuldu.")
        break
    else:
        print("Lütfen girdiğiniz şifre 5 haneden az 10 haneden fazla olmasın!")
