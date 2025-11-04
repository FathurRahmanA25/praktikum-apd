import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka!")

def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input harus berupa angka desimal/integer!")