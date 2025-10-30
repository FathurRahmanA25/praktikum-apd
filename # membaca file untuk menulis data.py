# membaca file untuk menulis data
file = open("data.txt", "w")

# menulis data ke file
file.write("lari dengan kecepatan kencang tidak membuatmu lelah!\n")
file.write("bahasa indonesia merupakan bahasa yang digunakan pada negara indonesia!\n")

# menutup file setelah selesai menulis
file.close()

# membaca isi file dan menampilkan baris per baris
file_path = "data.txt"
with open(file_path, "r") as file:
    for line in file:
        print(line)

# membaca seluruh isi file dan memnyimpannya dalam list
file_path = "data.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

# menampilkan isi file dengan pemisah baru
print("\n".join(lines))