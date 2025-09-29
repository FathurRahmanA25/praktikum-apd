print("=== list Produk Toko jaya online ===")
print("1. sabun mandi      - Rp20.000")
print("2. shampoo    - Rp10.000")
print("3. odol       - Rp17.000")
print("4. sikat gigi       - Rp8.000")

member = input("Apakah Anda member? (yes/no): ")

username = "fathur"
password = "023"

if member == "yes":
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    login = True if username == "fathur" and password == "023" else False
    
    if login:
        print("Login berhasil! Silakan belanja.")
        
        pilihan = input("Pilih produk (1/2/3): ")
        jumlah = int(input("Jumlah: "))
        
        harga = 20000 if pilihan == "1" else (5000 if pilihan == "2" else 100000)
        total = harga * jumlah
        diskon = total * 0.15
        bayar = total - diskon
        
        print(f"\nHarga sebelum diskon : Rp{total:,}")
        print(f"Diskon 15%           : Rp{diskon:,}")
        print(f"Total yang harus dibayar : Rp{bayar:,}")
    else:
        print("Login gagal! Program selesai.")

else:
    print("Anda bukan member, langsung ke menu belanja.")
    
    pilihan = input("Pilih produk (1/2/3): ")
    jumlah = int(input("Jumlah: "))
    
    harga = 20000 if pilihan == "1" else (5000 if pilihan == "2" else 100000)
    total = harga * jumlah
    
    print(f"\nTotal harga belanja: Rp{total:,}")