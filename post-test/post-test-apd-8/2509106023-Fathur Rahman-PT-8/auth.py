from data import users, login_user

def login() -> bool:
    global login_user
    print("=== SISTEM LOGIN ===")
    percobaan = 0
    while percobaan < 3:
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            print(f"\nSelamat datang, {username}!")
            login_user = username
            return True
        else:
            print("Username atau password salah!")
            percobaan += 1

    print("\nTerlalu banyak percobaan. Program berhenti.")
    return False