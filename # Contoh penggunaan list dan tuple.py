# Contoh penggunaan list dan tuple
jenis_latihan = ("Lari", "Push-up", "Sit-up") 
durasi = [30, 15, 20]  

print("Jadwal latihan awal:")
for i in range(len(jenis_latihan)):
    print(f"{jenis_latihan[i]} - {durasi[i]} menit")

durasi[0] = 40  # ubah durasi lari

print("\nJadwal latihan setelah diubah:")
for i in range(len(jenis_latihan)):
    print(f"{jenis_latihan[i]} - {durasi[i]} menit")
