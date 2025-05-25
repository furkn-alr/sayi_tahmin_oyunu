import random

def sayi_tahmin_oyunu():                   #giriş yapılır
    isim = input("Merhaba, isminizi girin. ")
    print("Hoşgeldin" , isim, "oyuna başlıyoruz." )

    while True:
        print("\nZorluk seviyesi seçin. ")  #zorluk seviyesi seçilir
        print("1 - Kolay Seviye (1,10)")
        print("2 - Orta Seviye (1,100)")
        print("3 - Zor Seviye (1,1000)")

        seviye = input("Seviye (1/2/3): ")
        if seviye == "1":
            alt_sinir = 1
            ust_sinir = 10
        elif seviye == "2":
            alt_sinir = 1
            ust_sinir = 100
        elif seviye == "3":
            alt_sinir = 1
            ust_sinir = 1000
        else:
            print("Geçersiz seviye seçimi, Orta Seviye (1,100) olarak ayarlanıyor.")
            alt_sinir = 1
            ust_sinir = 100


        gizli_sayi = random.randint(alt_sinir, ust_sinir)    #rastgele sayı tutulur
        tahmin_sayisi = 0
        tahminler = []
        print(alt_sinir ,"ile" ,ust_sinir ,"arasında bir sayı tuttum, tahmin etmeye çalış.")

        while True:                         #tahmin yapılır
            try:
                tahmin = int(input("Tahmininiz: "))
                tahminler.append(tahmin)     #tahminlerin listesi oluşturulur
                tahmin_sayisi += 1

                if tahmin < gizli_sayi:
                    print("Daha büyük bir sayı giriniz.")
                elif tahmin > gizli_sayi:
                    print("Daha küçük bir sayı giriniz. ")
                else:
                    print("Bravo! " , tahmin_sayisi ,  "tahminde doğru sayıyı buldun!")
                    break

            except ValueError:              #error kontrolü
                print("Geçerli bir sayı giriniz. ")

                #yeniden oynama
        yeniden =input("Yeniden oynamak ister misiniz? evet/hayır ").lower()
        if yeniden != "evet" :
            print("İşte tahminlerin: " ,tahminler)
            print("Oyun sona erdi",isim,"." ,"Güle Güle!")
            break

sayi_tahmin_oyunu()