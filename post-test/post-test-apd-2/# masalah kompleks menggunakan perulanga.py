data = {
    "Kelas A": [
        {"nama": "fatur", "nilai": {"Olahraga": 80, "alpro": 70}},
        {"nama": "fachry", "nilai": {"olahraga": 90, "alpro": 85}}
    ],
}
for kelas, siswa_list in data.items():
    print(f"\n{kelas}")
    total_kelas = 0
    siswa_terbaik = ""
    nilai_tertinggi = 0

    for siswa in siswa_list:
        total_nilai = 0
        jumlah_mapel = 0

        for nilai in siswa["nilai"].values():
            total_nilai += nilai
            jumlah_mapel += 1

        rata2 = total_nilai / jumlah_mapel
        print(f"{siswa['nama']} - Rata-rata: {rata2:.2f}")

