print("=== List Produk Toko Jaya Online ===")
print("1. Sabun mandi  - Rp20.000")
print("2. Shampoo      - Rp10.000")
print("3. Odol         - Rp17.000")
print("4. Sikat gigi   - Rp8.000")

member = input("Apakah Anda member? (yes/no): ")

# Data login member
username_akun = "fathur"
password_akun = "023"

# Harga produk
harga_produk = {
    "1": 20000,
    "2": 10000,
    "3": 17000,
    "4": 8000
}

if member.lower() == "yes":
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    login = True if username == username_akun and password == password_akun else False
    
    if login:
        print("Login berhasil! Silakan belanja.")
        
        pilihan = input("Pilih produk (1/2/3/4): ")
        if pilihan in harga_produk:
            jumlah = int(input("Jumlah: "))
            harga = harga_produk[pilihan]
            total = harga * jumlah
            diskon = total * 0.15
            bayar = total - diskon
            
            print(f"\nHarga sebelum diskon : Rp{total:,}")
            print(f"Diskon 15%           : Rp{diskon:,}")
            print(f"Total yang harus dibayar : Rp{bayar:,}")
        else:
            print("Produk tidak tersedia.")
    else:
        print("Login gagal! Program selesai.")

else:
    print("Anda bukan member, langsung ke menu belanja.")
    
    pilihan = input("Pilih produk (1/2/3/4): ")
    if pilihan in harga_produk:
        jumlah = int(input("Jumlah: "))
        harga = harga_produk[pilihan]
        total = harga * jumlah
        
        print(f"\nTotal harga belanja: Rp{total:,}")
    else:
        print("Produk tidak tersedia.")
