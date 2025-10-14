# menghitung rata-rata produk

data_produk = {
    'produk_sepatu': [100, 200, 300],
    'produk_baju': [150, 250, 350],
    'produk_celana': [200, 300, 400]
}

for produk, nilai in data_produk.items():
    total_nilai = 0
    for n in nilai:
        total_nilai += n
    rata_rata = total_nilai / len(nilai)
    print(f"Rata-rata nilai {produk} adalah {rata_rata}")