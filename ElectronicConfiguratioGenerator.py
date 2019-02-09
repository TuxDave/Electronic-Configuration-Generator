import funzioni
import sys
import time

if __name__ == '__main__':
    while True:
        print(f"""
    Hi, welcome to the Electronic Configuration generator!!!""")

        tipo = int(input(f"""Choose uno of the following options
    -Extended electronic configuration (type 1)
    -Compact electronioc configuration (type 2)
    Your choise is => """))

        tatomo = int(input(f"""\nWould you prefer to choose the atom to do the electronic configuraiton from: 
    -Name[Type 1, (NOT RECOMMANDED because you will insert the name in italian and all lower)]
    -Atomic Number[Type 2, (RECCOMANDED)]
    => """))

        zn = input('Insert your atom => ')
        if tatomo == 1:
            z = funzioni.nametoz(zn)
        elif tatomo == 2:
            z = zn

        if tipo == 1:
            print(f"""
    The electronic configuration of the atom '{funzioni.ztoname(z)}', Z={z} is: '{funzioni.ces(z)}'""")
        elif tipo == 2:
            print(f"""
    The electronic configuration of the atom '{funzioni.ztoname(z)}', Z={z} is: '{funzioni.cesc(z)}'""")
        scelta = int(input('\nWish you exit[1] or continue[2] to use this script? => '))
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