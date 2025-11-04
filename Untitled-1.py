
with open("nilai.txt", "w") as f:
    f.write("80\n75\n90\n60\n85\n")

total = 0
jumlah = 0

with open("nilai.txt", "r") as f:
    for baris in f:
        nilai = int(baris.strip())
        total += nilai
        jumlah += 1

rata_rata = total / jumlah

print("Daftar nilai disimpan di file 'nilai.txt'")
print("Rata-rata nilainya adalah:", rata_rata)
