nama = input("Masukkan Nama Pasien : ")
tinggiBadan = float(input("Masukkan Tinggi Badan (cm): "))
beratBadan = float(input("Masukkan Berat Badan (kg): "))

beratIdeal = tinggiBadan - 100

isKelebihan = beratBadan > beratIdeal

statusList = ["Berat Badan Ideal", "Kelebihan Berat Badan"]
status = statusList[int(isKelebihan)]

print("-" * 70)
print(f"|{'HASIL CEK BERAT BADAN':^68}|")
print("-" * 70)
print(f"| Nama Pasien   : {nama:<45}|")
print(f"| Tinggi Badan  : {tinggiBadan:.0f} cm{'':<34}|")
print(f"| Berat Badan   : {beratBadan:.0f} kg{'':<34}|")
print(f"| Berat Ideal   : {beratIdeal:.0f} kg{'':<34}|")
print(f"| Status        : {status:<45}|")
print("-" * 70)