import os
os.system("cls")

username_akun = "fathur"
password_akun = "023"

print("=== Selamat datang di Toko Jaya Online ===")
member = input("Apakah Anda member? (y/n): ").strip().lower()
login = False

produk = {
    "1": ("Sabun mandi", 20000),
    "2": ("Shampoo", 10000),
    "3": ("Odol", 17000),
    "4": ("Sikat gigi", 8000)
}

while True:  
    if member == "y":
        kesempatan = 3
        while kesempatan > 0:
            username = input("Masukkan username: ").strip()
            password = input("Masukkan password: ").strip()

            if username == "" or password == "":
                print("Username dan password tidak boleh kosong!")
                continue

            if username == username_akun and password == password_akun:
                print("Login berhasil! Anda akan mendapatkan diskon 15%.")
                login = True
                break
            else:
                kesempatan -= 1
                print(f"Login salah! Sisa percobaan: {kesempatan}")

        if not login:
            print("Anda gagal login 3 kali, sistem menganggap Anda Non-Member.")
    elif member != "n":
        print("Input tidak valid, sistem menganggap Anda Non-Member.")

    keranjang = ""
    total = 0
    
    while True:
        print("\n=== Menu Belanja ===")
        for kode, (nama, harga) in produk.items():
            print(f"{kode}. {nama:12} - Rp{harga:,}")
        print("5. Checkout")

        pilihan = input("Pilih produk (1/2/3/4) atau 5 untuk checkout: ").strip()
        if pilihan == "5":
            break
        elif pilihan in produk:
            os.system("cls")
            nama, harga = produk[pilihan]
            subtotal = harga
            total += subtotal
            keranjang += f"{nama:12} Rp{subtotal:,}\n"
            print(f"{nama} berhasil ditambahkan ke keranjang.")
            print(f"Total sementara: Rp{total:,}")
        else:
            print("Pilihan tidak valid!")

    print("=== STRUK BELANJA TOKO JAYA ONLINE ===")
    print(keranjang if keranjang else "Tidak ada produk dibeli.")

    if login:
        diskon = total * 0.15
        bayar = total - diskon
        print(f"\nTotal Sebelum Diskon : Rp{total:,}")
        print(f"Diskon 15%           : Rp{diskon:,}")
        print(f"Total Bayar          : Rp{bayar:,}")
    else:
        print(f"\nTotal Bayar : Rp{total:,}")

    print("===============================")
    print("Terima kasih telah berbelanja di Toko Jaya Online!")

    ulang = input("\nApakah ingin melakukan transaksi baru? (y/n): ").strip().lower()
    os.system("cls")
    print("=== Selamat datang di Toko Jaya Online ===")
    if ulang != "y":
        print("Program selesai. Sampai jumpa!")
        break
