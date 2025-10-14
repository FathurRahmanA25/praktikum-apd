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

inventory = []

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
        kategori = input("Kategori (contoh: cat, semen, kayu, besi): ")
        jumlah = int(input("Jumlah stok: "))
        harga = float(input("Harga per unit: "))

        alat = {
            "nama": nama,
            "kategori": kategori,
            "jumlah": jumlah,
            "harga": harga
        }
        inventory.append(alat)
        print(f"Alat '{nama}' berhasil ditambahkan!")

    elif pilihan == "2":
        print("\n--- Daftar Semua Alat ---")
        if not inventory:
            print("Belum ada alat yang terdaftar.")
        else:
            print(f"{'No':<4}{'Nama':<20}{'Kategori':<15}{'Jumlah':<10}{'Harga':<10}")
            for i, alat in enumerate(inventory, start=1):
                print(f"{i:<4}{alat['nama']:<20}{alat['kategori']:<15}{alat['jumlah']:<10}{alat['harga']:<10.2f}")

    elif pilihan == "3":
        print("\n--- Cari Alat ---")
        keyword = input("Masukkan nama alat yang dicari: ").lower()
        hasil = [a for a in inventory if keyword in a['nama'].lower()]

        if hasil:
            print(f"\nDitemukan {len(hasil)} hasil:")
            for a in hasil:
                print(f"- {a['nama']} ({a['kategori']}), stok: {a['jumlah']}, harga: Rp{a['harga']:.2f}")
        else:
            print("Alat tidak ditemukan.")

    elif pilihan == "4":
        if not inventory:
            print("Belum ada data untuk diubah.")
        else:
            print("\n--- Daftar Semua Alat ---")
            print(f"{'No':<4}{'Nama':<20}{'Kategori':<15}{'Jumlah':<10}{'Harga':<10}")
            for i, alat in enumerate(inventory, start=1):
                print(f"{i:<4}{alat['nama']:<20}{alat['kategori']:<15}{alat['jumlah']:<10}{alat['harga']:<10.2f}")

            try:
                index = int(input("\nMasukkan nomor alat yang ingin diubah: ")) - 1
                if index < 0 or index >= len(inventory):
                    print("Nomor tidak valid.")
                else:
                    alat = inventory[index]
                    print(f"Mengubah data '{alat['nama']}'")

                    nama_baru = input("Nama baru (biarkan kosong jika tidak diubah): ")
                    kategori_baru = input("Kategori baru (biarkan kosong jika tidak diubah): ")
                    jumlah_baru = input("Jumlah baru (biarkan kosong jika tidak diubah): ")
                    harga_baru = input("Harga baru (biarkan kosong jika tidak diubah): ")

                    if nama_baru:
                        alat['nama'] = nama_baru
                    if kategori_baru:
                        alat['kategori'] = kategori_baru
                    if jumlah_baru:
                        alat['jumlah'] = int(jumlah_baru)
                    if harga_baru:
                        alat['harga'] = float(harga_baru)

                    print("Data alat berhasil diperbarui!")
            except ValueError:
                print("Input tidak valid.")

    elif pilihan == "5":
        if not inventory:
            print("Belum ada data untuk dihapus.")
        else:
            print("\n--- Daftar Semua Alat ---")
            print(f"{'No':<4}{'Nama':<20}{'Kategori':<15}{'Jumlah':<10}{'Harga':<10}")
            for i, alat in enumerate(inventory, start=1):
                print(f"{i:<4}{alat['nama']:<20}{alat['kategori']:<15}{alat['jumlah']:<10}{alat['harga']:<10.2f}")

            try:
                index = int(input("\nMasukkan nomor alat yang ingin dihapus: ")) - 1
                if index < 0 or index >= len(inventory):
                    print("Nomor tidak valid.")
                else:
                    alat = inventory.pop(index)
                    print(f"Alat '{alat['nama']}' telah dihapus.")
            except ValueError:
                print("Input tidak valid.")

    elif pilihan == "6":
        print(f"Terima kasih, {username}! Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
