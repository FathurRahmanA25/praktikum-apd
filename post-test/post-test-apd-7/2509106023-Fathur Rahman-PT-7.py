import os

users = {
    "admin": "1234",
    "kasir": "0000",
    "manager": "abcd"
}
inventory = {}
login_user = ""

def clear_screen():
    """Membersihkan layar terminal"""
    os.system("cls || clear")

def tampilkan_semua_alat():
    """Menampilkan semua data alat"""
    if not inventory:
        print("Belum ada alat yang terdaftar.")
    else:
        print(f"{'No':<4}{'Nama':<20}{'Kategori':<15}{'Jumlah':<10}{'Harga':<10}")
        for i, (nama, data) in enumerate(inventory.items(), start=1):
            print(f"{i:<4}{nama:<20}{data['kategori']:<15}{data['jumlah']:<10}{data['harga']:<10.2f}")

def tambah_alat(nama, kategori, jumlah, harga):
    """Menambah alat baru ke inventory"""
    global inventory
    if nama in inventory:
        print("Alat ini sudah ada di inventory.")
    else:
        inventory[nama] = {"kategori": kategori, "jumlah": jumlah, "harga": harga}
        print(f"Alat '{nama}' berhasil ditambahkan!")

def cari_alat(keyword):
    """Mencari alat berdasarkan nama"""
    hasil = {n: d for n, d in inventory.items() if keyword.lower() in n.lower()}
    if hasil:
        print(f"\nDitemukan {len(hasil)} hasil:")
        for nama, data in hasil.items():
            print(f"- {nama} ({data['kategori']}), stok: {data['jumlah']}, harga: Rp{data['harga']:.2f}")
    else:
        print("Alat tidak ditemukan.")

def ubah_data_alat():
    """Prosedur untuk mengubah data alat"""
    global inventory
    if not inventory:
        print("Belum ada data untuk diubah.")
        return

    tampilkan_semua_alat()
    nama_alat = input("\nMasukkan nama alat yang ingin diubah: ")

    if nama_alat not in inventory:
        print("Alat tidak ditemukan.")
    else:
        data = inventory[nama_alat]
        nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
        kategori_baru = input("Kategori baru (kosongkan jika tidak diubah): ")
        jumlah_baru = input("Jumlah baru (kosongkan jika tidak diubah): ")
        harga_baru = input("Harga baru (kosongkan jika tidak diubah): ")

        if nama_baru:
            inventory[nama_baru] = inventory.pop(nama_alat)
            nama_alat = nama_baru
        if kategori_baru:
            data['kategori'] = kategori_baru
        if jumlah_baru:
            try:
                data['jumlah'] = int(jumlah_baru)
            except ValueError:
                print("Jumlah harus berupa angka!")
        if harga_baru:
            try:
                data['harga'] = float(harga_baru)
            except ValueError:
                print("Harga harus berupa angka!")

        print("Data alat berhasil diperbarui!")

def hapus_alat():
    """Prosedur untuk menghapus alat"""
    global inventory
    if not inventory:
        print("Belum ada data untuk dihapus.")
        return

    tampilkan_semua_alat()
    nama_hapus = input("\nMasukkan nama alat yang ingin dihapus: ")

    if nama_hapus in inventory:
        del inventory[nama_hapus]
        print(f"Alat '{nama_hapus}' telah dihapus.")
    else:
        print("Nama alat tidak ditemukan.")

def menu():
    """Menampilkan menu utama menggunakan rekursi"""
    clear_screen()
    print("\n=== MENU MANAJEMEN INVENTORY ALAT BANGUNAN ===")
    print("1. Tambah Alat")
    print("2. Lihat Semua Alat")
    print("3. Cari Alat")
    print("4. Ubah Data Alat")
    print("5. Hapus Alat")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    try:
        if pilihan == "1":
            print("\n--- Tambah Alat Baru ---")
            nama = input("Nama alat: ")
            kategori = input("Kategori: ")
            try:
                jumlah = int(input("Jumlah stok: "))
                harga = float(input("Harga per unit: "))
                tambah_alat(nama, kategori, jumlah, harga)
            except ValueError:
                print("Input jumlah/harga tidak valid!")

        elif pilihan == "2":
            tampilkan_semua_alat()

        elif pilihan == "3":
            keyword = input("Masukkan nama alat yang dicari: ")
            cari_alat(keyword)

        elif pilihan == "4":
            ubah_data_alat()

        elif pilihan == "5":
            hapus_alat()

        elif pilihan == "6":
            print(f"Terima kasih, {login_user}! Program selesai.")
            return

        else:
            print("Pilihan tidak valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    input("\nTekan Enter untuk kembali ke menu...")
    menu() 

def login():
    global login_user
    print("=== SISTEM LOGIN ===")
    percobaan = 0
    while percobaan < 3:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in users and users[username] == password:
            print(f"\nSelamat datang, {username}!")
            login_user = username
            return True
        else:
            print("Username atau password salah!")
            percobaan += 1
    print("\nTerlalu banyak percobaan. Program berhenti.")
    return False

if login():
    menu()
