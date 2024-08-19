import random

SECENEKLER = ["Tas", "Kagit", "Makas", "Ates", "Su"]  

def oyun_kurallari():
    kurallar = """
    Klasik tas, kagit, makas oyununa ates ve su karakterlerini ekleyerek oyunu daha eglenceli hale getirdim.
    Kurallar:
    - Tas: Makasi kirar ve Atesi yener. Ama Kagit ve Suya yenilir.
    - Kagit: Tasi sarar ve Suyu yener. Ama Makas ve Atese yenilir.
    - Makas: Kagidi keser ve Atesi yener. Ama Tas ve Suya yenilir.
    - Su: Tasi asindirir ve Makasi paslandirir. Ama Kagit ve Atese yenilir.
    - Ates: Kagidi yakar ve Suyu buharlastirir. Ama Tas ve Makasa yenilir.

    Ilk iki turu kazanan oyunu kazanir. Eger oyundan cikmak isterseniz 'exit' yazarak cikabilirsiniz."""
    print(kurallar)  

def oyuncu_secimi_al():
    while True: # Oyuncunun gecersiz girdi girmesini engellemek icin dongu kullandim.
        secim = input("Bir karakter seçiniz (Tas, Kagit, Makas, Ates, Su, Exit): ").capitalize()
        if secim in SECENEKLER + ["Exit"]: 
            return secim
        print("Geçersiz giriş! Lütfen geçerli bir seçenek giriniz.")

def karakter_karsilastir(oyuncu_secimi, bilgisayar_secimi):
    if oyuncu_secimi == bilgisayar_secimi:
        return "Berabere"
    elif oyuncu_secimi == "Tas": 
        if bilgisayar_secimi == "Makas" or bilgisayar_secimi == "Ates":
            return "Oyuncu"
        else:
            return "Bilgisayar"

    elif oyuncu_secimi == "Kagit":
        if bilgisayar_secimi == "Tas" or bilgisayar_secimi == "Su":
            return "Oyuncu"
        else:
            return "Bilgisayar"
                
    elif oyuncu_secimi == "Makas":
        if bilgisayar_secimi == "Kagit" or bilgisayar_secimi == "Ates":
            return "Oyuncu"
        else:
            return "Bilgisayar"

    elif oyuncu_secimi == "Su":
        if bilgisayar_secimi == "Tas" or bilgisayar_secimi == "Makas":
            return "Oyuncu"
        else:
            return "Bilgisayar"

    elif oyuncu_secimi == "Ates":
        if bilgisayar_secimi == "Kagit" or bilgisayar_secimi == "Su":
            return "Oyuncu"
        else:
            return "Bilgisayar"

def oyuncu_devam_cevabi():
    while True:  # Gecersiz bir girdi yapimasini engellemek icin dongu kurdum.
        cevap = input("Oyunu tekrar oynamak ister misin? (Evet, Hayir): ").capitalize()
        if cevap in ["Evet", "Hayir"]:  # Oyuncu cevabi "Evet" veya "Hayir" ise donguden cikiliyor.
            return cevap
        print("Gecersiz bir giris yaptiniz! Lutfen 'Evet' veya 'Hayir' yaziniz.\n") 

def tas_kagit_makas_MUHAMMED_COSGUN(): 
    oyun_kurallari()
    oyuncu_skoru, bilgisayar_skoru, oyun, round = 0, 0, 1, 1                                                                                               
    while True:
        print("\n#########################################\n")
        print(f"#### Oyun: {oyun}, Round: {round} : ####\n")

        oyuncu_secimi = oyuncu_secimi_al()
        if oyuncu_secimi == "Exit":  # Oyuncu "Exit" girerse oyundan cikilir.
            print("Oyuncu oyundan cikmak istiyor :((")
            print("Oyundan Cikis Yapildi!!")
            break

        bilgisayar_secimi = random.choice(SECENEKLER)  # Bilgisayara random bir sekilde secenekler listesinden karakter sectirdim.
        print(f"Bilgisayar Secimi: {bilgisayar_secimi}")
        
        kazanan = karakter_karsilastir(oyuncu_secimi, bilgisayar_secimi)    
        if kazanan == "Berabere":
            print("Tur berabere bitti :)")
        elif kazanan == "Oyuncu":
            print("Turu oyuncu kazandi :)")
            oyuncu_skoru += 1
        elif kazanan == "Bilgisayar":
            print("Turu bilgisayar kazandi :(")
            bilgisayar_skoru += 1
            
        # Her roundun sonunda oyuncu ve bilgisayarin skorlari yazdirilir.
        print(f"Oyuncu = {oyuncu_skoru}, Bilgisayar = {bilgisayar_skoru}")           
        round +=1  # Roundu guncellenir.

        if oyuncu_skoru == 2 or bilgisayar_skoru == 2:  # Oyuncu veya Bilgisayar skoru 2 ise oyun biter.
            if oyuncu_skoru == 2:
                print("Oyunu Oyuncu kazandi :)")
            else:
                print("Oyunu Bilgisayar kazandi :(")
                
            oyuncu_cevabi = oyuncu_devam_cevabi()
            if oyuncu_cevabi == "Hayir":  # Oyuncu "hayir" girer ise oyun biter.
                print("Oyuncu oyuna devam etmek istemiyor :((")
                print("Oyundan Cikis Yapildi!!")
                break
                
            print("Oyuncu oyuna devam etmek istiyor. Bakalim bilgisayar devam etmek isteyecek mi :)")
            bilgisayar_cevabi = random.choice(["Evet", "Hayir"])  # Bilgisayar random bir sekilde "Evet" veya "Hayir" dan birini secer.
            if bilgisayar_cevabi == "Hayir":
                print("Bilgisayar oyuna devam etmek istemiyor :((")  # Bilgisayarin random secimi "Hayir" olursa oyun biter.
                print("Oyundan Cikis Yapildi!!")
                break
                
            print("Bilgisayar da oyuna devam etmek istiyor. Oyun devam ediyoorrr :))")
            oyun += 1  # Oyun sayisi guncellendi ve her yeni oyunda oyun sayisi 1 artiriliyor.
            round = 1   # Round sayisi yeni oyuna gecilecegi icin 1 yapildi.
            oyuncu_skoru = 0  # Yeni oyuna gecilecegi icin skorlar 0'landi.
            bilgisayar_skoru = 0  #Yeni oyuna gecilecegi icin skorlar 0'landi.
                

tas_kagit_makas_MUHAMMED_COSGUN()
