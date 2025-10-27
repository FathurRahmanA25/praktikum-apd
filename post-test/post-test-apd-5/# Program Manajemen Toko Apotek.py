# Program manajemen apotek tanpa while True

obat = [
    {"nama": "Paracetamol", "harga": 5000, "stok": 10},
    {"nama": "Vitamin C", "harga": 3000, "stok": 15}
]

print("1. Lihat daftar obat")
print("2. Tambah obat baru")

pilih = input("Pilih menu (1/2): ")

if pilih == "1":
    for o in obat:
        print(f"{o['nama']} - Rp{o['harga']} ({o['stok']} stok)")

elif pilih == "2":
    n = input("Nama obat: ")
    h = int(input("Harga: "))
    s = int(input("Stok: "))
    obat.append({"nama": n, "harga": h, "stok": s})
    print("Obat berhasil ditambahkan!")
    print(obat)

else:
    print("Pilihan tidak tersedia.")
