jenis_latihan = {'easy run', 'tempo run', 'interval run'}
jarak_tempuh = {5, 8, 10, 12, 15}
durasi_latihan = {30, 45, 60, 75, 90}

def buat_rencana_latihan(jenis, jarak, durasi):
    rencana = []
    for j in jenis:
        for d in jarak:
            for s in durasi:
                rencana.append((j, d, s))
    return rencana

print("Rencana Latihan Lari:")
for latihan in buat_rencana_latihan(jenis_latihan, jarak_tempuh, durasi_latihan):
    print(f"Jenis: {latihan[0]}, Jarak: {latihan[1]} km, Durasi: {latihan[2]} menit")

print(f"\nTotal Rencana Latihan: {len(buat_rencana_latihan(jenis_latihan, jarak_tempuh, durasi_latihan))}")
for latihan in buat_rencana_latihan(jenis_latihan, jarak_tempuh, durasi_latihan):
    if latihan[1] >= 10 and latihan[2] <= 60:
        print(f"Rencana Intensif - Jenis: {latihan[0]}, Jarak: {latihan[1]} km, Durasi: {latihan[2]} menit")