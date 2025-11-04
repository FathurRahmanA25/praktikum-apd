# Buat file dengan 20 angka (tanpa random)
with open("angka.txt", "w") as f:
    for i in range(1, 21):
        f.write(f"{i}\n")

# Baca dan tampilkan angka genap
with open("angka.txt") as f:
    for x in f:
        n = int(x)
        if n % 2 == 0:
            print(n)
