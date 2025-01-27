def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Hata: Sıfıra bölme yapılamaz!"

def hesap_makinesi():
    print("\n===== Orta Dereceli Hesap Makinesi =====")
    print("İşlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("0. Çıkış")

    while True:
        try:
            secim = int(input("\nBir işlem seçin (1/2/3/4 veya çıkış için '0'): "))

            if secim == 0:
                print("\nHesap makinesi kapatılıyor. Hoşça kalın!")
                break

            if secim not in [1, 2, 3, 4]:
                print("Hata: Geçersiz seçim. Lütfen 1, 2, 3, 4 veya 0 girin.")
                continue

            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))

            if secim == 1:
                print(f"Sonuç: {sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")
            elif secim == 2:
                print(f"Sonuç: {sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")
            elif secim == 3:
                print(f"Sonuç: {sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")
            elif secim == 4:
                sonuc = bolme(sayi1, sayi2)
                if isinstance(sonuc, str):
                    print(sonuc)
                else:
                    print(f"Sonuç: {sayi1} / {sayi2} = {sonuc}")

        except ValueError:
            print("Hata: Geçerli bir sayı girin.")

# Hesap makinesini başlat
if __name__ == "__main__":
    hesap_makinesi()
