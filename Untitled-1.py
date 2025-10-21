nama_mahasiswa = ["Andi", "Faris", "Mozart"]
print("Data awal:", nama_mahasiswa)

nama_baru = input("Masukkan nama baru: ")
nama_mahasiswa.append(nama_baru)
print("Data setelah ditambah:", nama_mahasiswa)

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
jurusan = input("Masukkan jurusan: ")

data_mahasiswa = (nama, nim, jurusan)
print("Hasil tuple:", data_mahasiswa)