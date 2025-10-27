# penambahan, penghapusan, dan perulangan pada dictionary
data_dict = {'a': 1, 'b': 2, 'c': 3}

# penampilan elemen ke dalam dictoinary
data_dict['d'] = 4

# penghapusan elemen ke dari dictionary
del data_dict['b']

# perulangan pada dictionary (kunci)
for key in data_dict:
    print(key)

# perulangan pada dictionary (nilai)
for values in data_dict.values():
    print(values)