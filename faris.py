with open("nilai.txt", "w") as f:
    nilai = [85, 95, 90, 97, 100]
    for n in nilai:
        f.write(str(n) + "\n")

with open("nilai.txt", "r") as f:
    data = f.readlines()

data = [int(x.strip()) for x in data]
rata = sum(data) / len(data)

print("Nilai siswa:", data)
print("Rata-rata nilai:", rata)