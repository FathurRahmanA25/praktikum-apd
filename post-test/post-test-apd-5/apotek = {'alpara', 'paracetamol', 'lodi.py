apotek = {'alpara', 'paracetamol', 'lodia', 'tera f'}
apotek.add("spasminal")

# Dictionary 
harga = {
    'alpara': 18000,
    'paracetamol': 5000,
    'lodia': 17000,
    'tera f': 10000,
    'spasminal': 15000
}

print("Daftar barang yang ada ")
for item in apotek:
     print(item)
 
print("\nharga Produk")
for nama, jumlah in harga.items():
    print(f"{nama}: {jumlah}")
