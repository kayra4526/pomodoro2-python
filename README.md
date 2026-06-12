# ✈️ Terminal Havayolları Odaklanma Sayacı (Gamified Pomodoro Timer)

Sıkıcı geri sayım sayaçlarından sıkıldınız mı? Odaklanmayı oyunlaştıran (gamification) bu Python projesi ile Pomodoro seanslarınızı bir uçak yolculuğuna dönüştürün! Terminalinizde kalkış yapan bir uçağın hedefine doğru ilerleyişini canlı olarak izlerken, çalışmaya olan motivasyonunuzu zirveye taşıyın.

## 🚀 Özellikler

* **Canlı Uçuş Animasyonu:** Terminalde `\r` kullanılarak oluşturulan dinamik ilerleme çubuğunda (progress bar), uçağın (`✈️`) hedefine doğru saniye saniye süzülmesini izleyin.
* **Gerçekçi Rotalar:** Kalkış noktası Ankara olmak üzere, İstanbul, Roma, Tokyo gibi şehirlere ortalama uçuş süreleriyle otomatik odaklanma seansları başlatın.
* **Özel Uçuş Planlama:** "Kendi Rotanı Oluştur" seçeneği ile istediğiniz şehre, kendi belirlediğiniz sürede (örn: 25 dakika) özel Pomodoro uçuşları düzenleyin.
* **Yüzde ve Zaman Takibi:** Uçuşun yüzde kaçının tamamlandığını ve hedefe (molaya) ne kadar süre kaldığını anlık olarak görün.

## 🛠️ Kurulum ve Kullanım

Bu proje hiçbir dış kütüphaneye (library) ihtiyaç duymaz, tamamen Python'un standart modülleri (`time` ve `sys`) kullanılarak geliştirilmiştir.

1. Projeyi bilgisayarınıza indirin (clone).
2. Terminali veya komut satırını açın.
3. Proje dizinine gidin ve uçağı havalandırın:
   ```bash
   python main.py

   Menüden gitmek istediğiniz rotayı seçin ve arkanıza yaslanıp odaklanmaya başlayın!

    Terminal Çıktısı
   ☁️ TERMINAL HAVAYOLLARI ODAKLANMA UÇUŞU ☁️
========================================

🛫 Ankara - Roma uçuşumuz başlamak üzeredir.
Lütfen kemerlerinizi bağlayın ve odaklanma moduna geçin...

[==============✈️               ] %50 | ⏳ Kalan Yolculuk: 70:00
   
