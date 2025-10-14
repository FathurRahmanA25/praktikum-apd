# Fungsi untuk menghitung luas persegi panjang
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# Input dari pengguna
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

# Panggil fungsi dan tampilkan hasil
print("Luas persegi panjang adalah:", hitung_luas_persegi_panjang(panjang, lebar))