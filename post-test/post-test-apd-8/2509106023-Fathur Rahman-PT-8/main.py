from auth import login
from data import login_user
from inventory import tambah_alat, cari_alat, ubah_data_alat, hapus_alat
from display import tampilkan_semua_alat
from utils import clear_screen, input_int, input_float
def menu():
    while True:
        clear_screen()
        print("\n=== MENU MANAJEMEN INVENTORY ALAT BANGUNAN ===")
        print("1. Tambah Alat")
        print("2. Lihat Semua Alat")
        print("3. Cari Alat")
        print("4. Ubah Data Alat")
        print("5. Hapus Alat")
        print("6. Keluar")

        pilihan = input("\nPilih menu (1-6): ").strip()

        if pilihan == "1": 
            print("\n--- Tambah Alat Baru ---")
            nama = input("Nama alat: ").strip()
            kategori = input("Kategori: ").strip()
            if not nama or not kategori:
                print("Nama dan kategori tidak boleh kosong!")
                input("\nTekan Enter untuk kembali...")
                continue
            jumlah = input_int("Jumlah stok: ")
            harga = input_float("Harga per unit: ")
            tambah_alat(nama, kategori, jumlah, harga)

        elif pilihan == "2":
            tampilkan_semua_alat()

        elif pilihan == "3":
            keyword = input("Masukkan nama alat yang dicari: ").strip()
            if keyword:
                cari_alat(keyword)
            else:
                print("Kata kunci tidak boleh kosong!")

        elif pilihan == "4":
            ubah_data_alat()

        elif pilihan == "5":
            hapus_alat()

        elif pilihan == "6":
            print(f"\n Terima kasih, {login_user}! Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")

        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    if login():
        menu()