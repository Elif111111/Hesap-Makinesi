import math

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Hata: Sıfıra bölme tanımsız."

def karekok(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Hata: Negatif bir sayının karekökü alınamaz."

def us_alma(x, y):
    return x ** y

def mod_alma(x, y):
    return x % y

def hesap_makinesi():
    print("=== Gelişmiş Hesap Makinesi ===")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    print("5. Karekök (√)")
    print("6. Üs Alma (^)")
    print("7. Mod Alma (%)")
    print("8. Çıkış")

    while True:
        try:
            secim = input("\nBir işlem seçin (1/2/3/4/5/6/7/8): ")

            if secim == '8':  # Çıkış seçeneği
                print("Hesap makinesi kapatılıyor...")
                break

            if secim in ['1', '2', '3', '4', '6', '7']:  # İki sayıyla yapılan işlemler
                sayi1 = float(input("Birinci sayıyı girin: "))
                sayi2 = float(input("İkinci sayıyı girin: "))

                if secim == '1':
                    print(f"Sonuç: {sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")
                elif secim == '2':
                    print(f"Sonuç: {sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")
                elif secim == '3':
                    print(f"Sonuç: {sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")
                elif secim == '4':
                    print(f"Sonuç: {sayi1} / {sayi2} = {bolme(sayi1, sayi2)}")
                elif secim == '6':
                    print(f"Sonuç: {sayi1} ^ {sayi2} = {us_alma(sayi1, sayi2)}")
                elif secim == '7':
                    print(f"Sonuç: {sayi1} % {sayi2} = {mod_alma(sayi1, sayi2)}")

            elif secim == '5':  # Tek sayıyla yapılan karekök işlemi
                sayi = float(input("Karekökü alınacak sayıyı girin: "))
                print(f"Sonuç: √{sayi} = {karekok(sayi)}")

            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.")

        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu: {e}")

# Hesap makinesini çalıştır
hesap_makinesi()
