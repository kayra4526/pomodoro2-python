import time
import sys

# Kalkış: Ankara (Ortalama uçuş süreleri - dakika)
UCUS_ROTALARI = {
    "İstanbul": 45,
    "İzmir": 50,
    "Antalya": 55,
    "Roma": 140,
    "Londra": 250,
    "Tokyo": 660 # Hardcore odaklanma!
}

def ucus_sayaci(hedef, dakika):
    toplam_saniye = dakika * 60
    
    print(f"\n🛫 Ankara - {hedef} uçuşumuz başlamak üzeredir.")
    print("Lütfen kemerlerinizi bağlayın ve odaklanma moduna geçin...\n")
    time.sleep(2)
    
    for gecen_saniye in range(toplam_saniye + 1):
        kalan_saniye = toplam_saniye - gecen_saniye
        dk, sn = divmod(kalan_saniye, 60)
        zaman_formati = f"{dk:02d}:{sn:02d}"
        
        # İlerleme Çubuğu (Progress Bar) Hesaplama
        # 30 karakterlik bir gökyüzü (çubuk) yapıyoruz
        cubuk_uzunlugu = 30
        ilerleme_orani = gecen_saniye / toplam_saniye if toplam_saniye > 0 else 1
        ilerleme_miktari = int(cubuk_uzunlugu * ilerleme_orani)
        
        # Çubuğu çiz (Örn: [======✈️             ])
        tamamlanan = "=" * ilerleme_miktari
        kalan = " " * (cubuk_uzunlugu - ilerleme_miktari - 1)
        
        # Uçak simgesi hep ilerleyen ucun ucunda olacak
        if gecen_saniye == toplam_saniye:
            bar = f"[{'=' * cubuk_uzunlugu}🛬]"
        else:
            bar = f"[{tamamlanan}✈️{kalan}]"
            
        yuzde = int(ilerleme_orani * 100)
        
        # Terminale yazdır
        sys.stdout.write(f"\r{bar} %{yuzde:02d} | ⏳ Kalan Yolculuk: {zaman_formati}")
        sys.stdout.flush()
        
        if gecen_saniye < toplam_saniye:
            time.sleep(1)
            
    print(f"\n\n🛬 Ding Dong! Sayın yolcumuz, {hedef} havalimanına iniş yaptık.")
    print("Mükemmel bir odaklanma seansıydı, tebrikler! 🎉\a")

def main():
    while True:
        print("\n" + "*"*40)
        print("☁️ TERMINAL HAVAYOLLARI ODAKLANMA UÇUŞU ☁️")
        print("*"*40)
        
        print("\nPopüler Rotalar (Ankara Çıkışlı):")
        for sehir, sure in UCUS_ROTALARI.items():
            print(f"- {sehir} ({sure} dk)")
            
        print("\n1. Listeden bir şehre uç")
        print("2. Kendi rotanı ve süreni oluştur (Özel Uçuş)")
        print("3. Uçaktan İn (Çıkış)")
        
        secim = input("\nSeçiminiz (1/2/3): ")
        
        if secim == '1':
            hedef = input("Gitmek istediğiniz şehri yazın: ").capitalize()
            if hedef in UCUS_ROTALARI:
                ucus_sayaci(hedef, UCUS_ROTALARI[hedef])
            else:
                print("❌ Bu rota sistemde yok. Lütfen listedeki gibi yazın veya 'Özel Uçuş' seçin.")
                
        elif secim == '2':
            hedef = input("Hedef şehrin adı: ").capitalize()
            try:
                sure = int(input(f"Ankara'dan {hedef}'a uçuş kaç dakika sürecek?: "))
                ucus_sayaci(hedef, sure)
            except ValueError:
                print("❌ Lütfen süre için sadece sayı girin!")
                
        elif secim == '3':
            print("Terminal Havayollarını tercih ettiğiniz için teşekkür ederiz. İyi günler! 👋")
            break
        else:
            print("❌ Geçersiz kapı numarası, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()