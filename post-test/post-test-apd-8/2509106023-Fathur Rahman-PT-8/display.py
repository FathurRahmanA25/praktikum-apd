from prettytable import PrettyTable
from data import inventory

def tampilkan_semua_alat():
    if not inventory:
        print("Belum ada alat yang terdaftar.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama", "Kategori", "Jumlah", "Harga (Rp)"]
    for i, (nama, data) in enumerate(inventory.items(), start=1):
        table.add_row([i, nama, data["kategori"], data["jumlah"], f"{data['harga']:.2f}"])
    
    print(table)

def tampilkan_hasil_pencarian(hasil: dict):
    if not hasil:
        print("Alat tidak ditemukan.")
        return

    table = PrettyTable()
    table.field_names = ["Nama", "Kategori", "Jumlah", "Harga (Rp)"]
    for nama, data in hasil.items():
        table.add_row([nama, data["kategori"], data["jumlah"], f"{data['harga']:.2f}"])
    
    print(f"\nDitemukan {len(hasil)} hasil:")
    print(table)