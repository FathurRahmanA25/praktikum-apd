# contoh dictionary
data_mhs = {
    'nim': '2509076056',
    'nama': 'fachry nazrul ramadhan',
    'jurusan': 'teknik elekro',
    'semester': 1
}

nilai_mhs = {
    'fachry': 100,
    'fatur': 100,
    'nurul': 100
}


#menamipilkan data dictionary data_mhs
print("\ndata mahasasiswa:")
for key, value in data_mhs.items():
    print(f"{key}: {value}")\
    
# menampilkan data dictionary nilai_mhs
print("\nnilai mahasiswa:")
for nama, nilai in nilai_mhs.items():
    print(f"{nama}: {nilai}")