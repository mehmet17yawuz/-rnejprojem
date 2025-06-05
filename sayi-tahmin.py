import random

print("Sayı Tahmin Oyununa Hoşgeldin!")

sayi = random.randint(1, 100)
tahmin = None
tahmin_sayisi = 0

while tahmin != sayi:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin et: "))
    tahmin_sayisi += 1
    if tahmin < sayi:
        print("Daha büyük bir sayı dene.")
    elif tahmin > sayi:
        print("Daha küçük bir sayı dene.")
    else:
        print(f"Tebrikler! {tahmin_sayisi} denemede doğru tahmin ettin.")
