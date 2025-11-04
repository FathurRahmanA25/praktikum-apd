import random

with open("data.txt", "w") as f:
    for _ in range(99):
        f.write(f"{random.randint(1,100)}\n")

with open("data.txt") as f:
    for baris in f:
        print(baris.strip())