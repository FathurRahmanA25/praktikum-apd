# Fungsi untuk menggabungkan dua string
def gabung_string(string1, string2):
    hasil = string1 + string2
    return hasil

# Input dari pengguna
string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")

# Panggil fungsi dan tampilkan hasil
print("Hasil penggabungan string:", gabung_string(string1, string2))