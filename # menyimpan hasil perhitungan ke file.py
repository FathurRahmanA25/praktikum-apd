# menyimpan hasil perhitungan ke file
def hitungan_luas_persegi(sisi):
    return sisi * sisi

# buka file untuk menulis hasil perhitungan
file = open("hasil_perhitungan.txt", "w")

# hitungan dan simpan hasil perhitungan ke file
for sisi in range(20, 30):
    luas = hitungan_luas_persegi(sisi)
    file.write(f"sisi: {sisi}, luas: {luas}\n")

# tutup file setelah selesai menulis
file.close()

# menyimpan data list ke file
data_list = [16, 26, 36, 46, 56]

# buka file untuk menulis data list
file = open("data_list.txt", "w")

# simpan data list ke file
for data in data_list:
    file.write(str(data) + '\n')

# tutup file setelah selesai menulis
file.close()