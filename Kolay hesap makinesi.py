def hesap_makinesi():
    print("Hesap Makinesi")
    print("Seçenekler:")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    print("5. Çıkış")

    while True:
        try:
            secim = input("\nBir işlem seçin (1/2/3/4/5): ")

            if secim == '5':
                print("Hesap makinesi kapatılıyor...")
                break

            if secim in ['1', '2', '3', '4']:
                sayi1 = float(input("Birinci sayıyı girin: "))
                sayi2 = float(input("İkinci sayıyı girin: "))

                if secim == '1':
                    print(f"Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
                elif secim == '2':
                    print(f"Sonuç: {sayi1} - {sayi2} = {sayi1 - sayi2}")
                elif secim == '3':
                    print(f"Sonuç: {sayi1} * {sayi2} = {sayi1 * sayi2}")
                elif secim == '4':
                    if sayi2 != 0:
                        print(f"Sonuç: {sayi1} / {sayi2} = {sayi1 / sayi2}")
                    else:
                        print("Hata: Bir sayı sıfıra bölünemez.")
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.")
        except ValueError:
            print("Hata: Geçerli bir sayı girin.")

hesap_makinesi()