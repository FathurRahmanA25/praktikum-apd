# Program Latihan Lari Menggunakan Tuple dan List

hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu") 
jarak = [6.5, 5.2, 7.0, 0, 6.5, 7.0, 21.8] 
menu_latihan = ["easy run", "tempo run", "interval", "long run"]

print("Menu Latihan Lari")
for i in range(len(hari)):
    print(f"{hari[i]} : {jarak[i]} km : {menu_latihan}")
    

