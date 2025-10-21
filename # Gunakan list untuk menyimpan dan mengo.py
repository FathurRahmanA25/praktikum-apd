# Gunakan list untuk menyimpan dan mengolah data
nilai_mahasiswa = [88, 79, 98, 89]
print("Data nilai:", nilai_mahasiswa)

# Tambahkan data baru ke dalam list
nilai_mahasiswa.append(91)
print("Setelah ditambah:", nilai_mahasiswa)

# Gunakan tuple untuk menyimpan data tetap (identitas)
data_mahasiswa = ("faris", "076054", "elektro")

# Lakukan analisis sederhana (rata-rata nilai)
rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)

# Tampilkan hasil
print("\nIdentitas Mahasiswa:", data_mahasiswa)
print("Rata-rata nilai:", rata_rata)