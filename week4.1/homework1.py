maas = float(input("Lütfen maaşınızı giriniz: "))

if maas <= 10000:
    kesinti = maas * 0.05
elif maas <= 25000:
    kesinti = maas * 0.10
elif maas <= 45000:
    kesinti = maas * 0.25
else:
    kesinti = maas * 0.30

yeni_maas = maas - kesinti
print(f"Yeni maaşınız: {yeni_maas}")
