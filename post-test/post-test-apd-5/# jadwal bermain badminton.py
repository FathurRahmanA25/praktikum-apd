# jadwal bermain badminton
hari = {'Senin', 'Rabu', 'Jumat'}
waktu = {'malam', 'Sore'}

print("Jadwal Bermain Badminton:")
for h in hari:
    for w in waktu:
        print(f"Hari: {h}, Waktu: {w}")
print(f"\nTotal Jadwal Bermain Badminton: {len(hari) * len(waktu)}\n")