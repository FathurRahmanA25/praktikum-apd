import os
os.system("cls  || clear")

users = {
    "admin": "1234",
    "kasir": "0000",
    "manager": "abcd"
}

print("=== SISTEM LOGIN ===")
login_berhasil = False
percobaan = 0

while not login_berhasil and percobaan < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        print(f"\nSelamat datang, {username}!")
        login_berhasil = True
    else:
        print("Username atau password salah!")
        percobaan += 1

if not login_berhasil:
    print("\nTerlalu banyak percobaan. Program berhenti.")
    exit()

inventory = {}

os.system("cls  || clear")
while True:
    print("\n=== MENU MANAJEMEN INVENTORY ALAT BANGUNAN ===")
    print("1. Tambah Alat")
    print("2. Lihat Semua Alat")
    print("3. Cari Alat")
    print("4. Ubah Data Alat")
    print("5. Hapus Alat")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        print("\n--- Tambah Alat Baru ---")
        nama = input("Nama alat: ")

        if nama in inventory:
            print("Alat ini sudah ada di inventory.")
        else:
            kategori = input("Kategori (contoh: cat, semen, kayu, besi): ")
            jumlah = int(input("Jumlah stok: "))
            harga = float(input("Harga per unit: "))

            inventory[nama] = {
                "kategori": kategori,
                "jumlah": jumlah,
                "harga": harga
            }
            print(f"Alat '{nama}' berhasil ditambahkan!")

    elif pilihan == "2":
        print("\n--- Daftar Semua Alat ---")
        if not inventory:
            print("Belum ada alat yang terdaftar.")
        else:
            print(f"{'No':<4}{'Nama':<20}{'Kategori':<15}{'Jumlah':<10}{'Harga':<10}")
            no = 1
            for nama, data in inventory.items():
                print(f"{no:<4}{nama:<20}{data['kategori']:<15}{data['jumlah']:<10}{data['harga']:<10.2f}")
                no += 1

    elif pilihan == "3":
        print("\n--- Cari Alat ---")
        keyword = input("Masukkan nama alat yang dicari: ").lower()
        hasil = {n: d for n, d in inventory.items() if keyword in n.lower()}

        if hasil:
            print(f"\nDitemukan {len(hasil)} hasil:")
            for nama, data in hasil.items():
                print(f"- {nama} ({data['kategori']}), stok: {data['jumlah']}, harga: Rp{data['harga']:.2f}")
        else:
            print("Alat tidak ditemukan.")

    elif pilihan == "4":
        if not inventory:
            print("Belum ada data untuk diubah.")
        else:
            print("\n--- Daftar Semua Alat ---")
            no = 1
            for nama, data in inventory.items():
                print(f"{no}. {nama} ({data['kategori']}) - stok: {data['jumlah']}, harga: Rp{data['harga']:.2f}")
                no += 1

            nama_alat = input("\nMasukkan nama alat yang ingin diubah: ")
            if nama_alat not in inventory:
                print("Alat tidak ditemukan.")
            else:
                data = inventory[nama_alat]
                print(f"Mengubah data '{nama_alat}'")

                nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
                kategori_baru = input("Kategori baru (kosongkan jika tidak diubah): ")
                jumlah_baru = input("Jumlah baru (kosongkan jika tidak diubah): ")
                harga_baru = input("Harga baru (kosongkan jika tidak diubah): ")

                if nama_baru:
                    inventory[nama_baru] = inventory.pop(nama_alat)
                    nama_alat = nama_baru
                if kategori_baru:
                    inventory[nama_alat]['kategori'] = kategori_baru
                if jumlah_baru:
                    inventory[nama_alat]['jumlah'] = int(jumlah_baru)
                if harga_baru:
                    inventory[nama_alat]['harga'] = float(harga_baru)

                print("Data alat berhasil diperbarui!")

    elif pilihan == "5":
        if not inventory:
            print("Belum ada data untuk dihapus.")
        else:
            print("\n--- Daftar Semua Alat ---")
            no = 1
            for nama, data in inventory.items():
                print(f"{no}. {nama} ({data['kategori']}) - stok: {data['jumlah']}, harga: Rp{data['harga']:.2f}")
                no += 1

            nama_hapus = input("\nMasukkan nama alat yang ingin dihapus: ")
            if nama_hapus in inventory:
                del inventory[nama_hapus]
                print(f"Alat '{nama_hapus}' telah dihapus.")
            else:
                print("Nama alat tidak ditemukan.")

    elif pilihan == "6":
        print(f"Terima kasih, {username}! Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
