from second import *


def main():
    while True:
        load()
        mood = input('\nBagaimana Mood kalian hari ini?(ketik 0 jika ingin keluar) ')
        print(mood)
        delayInput()
        clear()
        if mood == '0':
            return False

if __name__ == "__main__":
    main()