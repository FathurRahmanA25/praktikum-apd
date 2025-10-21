# tuple
menu_latihan = ["easy run", "interval", "tempo run", "long run"]
hari_latihan = ["senin", "selasa", "kamis", "jumat", "minggu"]
nama_atlet = ["fachry", "iqbal"]

# list
personal_best = ["5 km 20menit", "10 km 40 menit", "21 km 1 jam 40 menit"]

data_hasil = ["menu latihan"[1],"hari latihan"[1],"personal best"[3],"nama atlet"
              "menu latihan"[4],"hari latihan"[4],"personal best"[1],"nama talet"[2]]

# tampilkan hasil 
for data in data_hasil:
    menu_latihan, nilai = data
    print("Nama atlet:", nama_atlet[0], ", menu latihan :", menu_latihan[1], ", hari latihan:", hari_latihan)


