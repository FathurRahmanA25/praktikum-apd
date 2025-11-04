from data import inventory
from display import tampilkan_semua_alat, tampilkan_hasil_pencarian


def tambah_alat(nama: str, kategori: str, jumlah: int, harga: float):
    if nama in inventory:
        print("Alat ini sudah ada di inventory.")
    else:
        inventory[nama] = {"kategori": kategori, "jumlah": jumlah, "harga": harga}
        print(f"Alat '{nama}' berhasil ditambahkan!")

def cari_alat(keyword: str):
    hasil = {n: d for n, d in inventory.items() if keyword.lower() in n.lower()}
    tampilkan_hasil_pencarian(hasil)

def ubah_data_alat():
    if not inventory:
        print("Belum ada data untuk diubah.")
        return

    tampilkan_semua_alat()
    nama_alat = input("\nMasukkan nama alat yang ingin diubah: ")

    if nama_alat not in inventory:
        print("Alat tidak ditemukan.")
        return

    data = inventory[nama_alat]

    nama_baru = input("Nama baru (kosongkan jika tidak diubah): ").strip()
    kategori_baru = input("Kategori baru (kosongkan jika tidak diubah): ").strip()
    jumlah_baru = input("Jumlah baru (kosongkan jika tidak diubah): ").strip()
    harga_baru = input("Harga baru (kosongkan jika tidak diubah): ").strip()

    if nama_baru:
        inventory[nama_baru] = inventory.pop(nama_alat)
        nama_alat = nama_baru
        data = inventory[nama_alat]  

    if kategori_baru:
        data["kategori"] = kategori_baru
    if jumlah_baru:
        try:
            data["jumlah"] = int(jumlah_baru)
        except ValueError:
            print("Jumlah harus berupa angka!")
    if harga_baru:
        try:
            data["harga"] = float(harga_baru)
        except ValueError:
            print("Harga harus berupa angka!")

    print("Data alat berhasil diperbarui!")

def hapus_alat():
    if not inventory:
        print("Belum ada data untuk dihapus.")
        return

    tampilkan_semua_alat()
    nama_hapus = input("\nMasukkan nama alat yang ingin dihapus: ").strip()

    if nama_hapus in inventory:
        del inventory[nama_hapus]
        print(f"Alat '{nama_hapus}' telah dihapus.")
    else:
        print("Nama alat tidak ditemukan.")