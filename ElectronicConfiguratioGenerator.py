import funzioni
import sys
import time

if __name__ == '__main__':
    while True:
        print(f"""
    Hi, welcome to the Electronic Configuration generator!!!""")

        try:
            tipo = int(input(f"""Choose uno of the following options
        -Extended electronic configuration (type 1)
        -Compact electronioc configuration (type 2)
        Your choise is => """))
        except ValueError:
            print('Please, insert a numeric value [1/2]...')
            funzioni.reboot()
            continue

        if tipo <= 0 or tipo >= 3:
            print('Please, choose a value between 1 and 2!')
            funzioni.reboot()
            continue

        try:
            tatomo = int(input(f"""\nWould you prefer to choose the atom to do the electronic configuraiton from: 
    -Name[Type 1, (NOT RECOMMANDED because you will insert the name in italian and all lower)]
    -Atomic Number[Type 2, (RECCOMANDED)]
    => """))
        except ValueError:
            print('Please, insert a numeric value [1/2]...')
            funzioni.reboot()
            continue

        if tatomo <= 0 or tatomo >= 3:
            print('Please, choose a value between 1 and 2!')
            funzioni.reboot()
            continue

        z = funzioni.zncreation(tatomo)

        if tipo == 1:
            print(f"""
    The electronic configuration of the atom '{funzioni.ztoname(z)}', Z={z} is: '{funzioni.ces(z)}'""")
        elif tipo == 2:
            print(f"""
    The electronic configuration of the atom '{funzioni.ztoname(z)}', Z={z} is: '{funzioni.cesc(z)}'""")

        numerowhile = 1
        while numerowhile == 1:
            try:
                scelta = int(input('\nWish you exit[1] or continue[2] to use this script? => '))
                numerowhile += 1
            except ValueError:
                sys.exit()
        if scelta == 1:
            print('I\'m exiting...')
            break
        elif scelta == 2:
            print('''Reboot in:
             3...
             2...
             1...''')
            time.sleep(2)
            continue