jadwal_kelas = {
    'senin': 'PTE', 'kalkulus'
    'selasa': 'bahasa indonesia', 
    'rabu': 'fsika', 
    'kamis': 'Bahasa inggris', 
    'jumat': 'ISBD'
}

data_mhs = {
    'nim': '2509076056',
    'nama': 'fachry nazrul ramadhan',
    'jurusan': 'teknik elekro',
    'semester': 1
}

print("\njadwal kelas:")
for hari, matkul in jadwal_kelas.items():
    print(f"{hari}: {matkul}")

print("\ndata mahasasiswa:")
for key, value in data_mhs.items():
    print(f"{key}: {value}")
   

