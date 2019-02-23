import csv
import time

def cesc(z):
    with open('elementi.csv',encoding='ISO-8859-1',newline="") as elm:
        elm = csv.reader(elm,delimiter=',')
        for lista in elm:
            if str(z) == lista[0]:
                elemento = lista
        nat = int(elemento[0])
        if nat >= 2 and nat <= 10:
            gasnobile = 'He'
        elif nat >= 11 and nat <= 18:
            gasnobile = 'Ne'
        elif nat >= 19 and nat <= 36:
            gasnobile = 'Ar'
        elif nat >= 37 and nat <= 54:
            gasnobile = 'Kr'
        elif nat >= 55 and nat <= 86:
            gasnobile = 'Xe'
        elif nat >= 87 and nat <= 118:
            gasnobile = 'Rn'
        blocco = elemento[4]
        valenza = int(elemento[5])
        lv = int(elemento[3])
        if nat == 1:
            econf = f"1s1"
        elif blocco == 's':
            econf = f"[{gasnobile}] {lv}s{valenza}"
        elif blocco == 'p' and (lv == 2 or lv == 3):
            econf = f"[{gasnobile}] {lv}s2 {lv}p{valenza}"
        elif blocco == 'p' and (lv == 4 or lv == 5):
            econf = f"[{gasnobile}] {lv}s2 {lv - 1}d10 {lv}p{valenza}"
        elif blocco == 'p' and (lv == 6 or lv == 7):
            econf = f"[{gasnobile}] {lv}s2 {lv - 2}f14 {lv -1}d10 {lv}p{valenza}"
        elif blocco == 'd' and (lv == 4 or lv == 5):
            econf = f"[{gasnobile}] {lv}s2 {lv - 1}d{valenza}"
        elif blocco == 'd' and (lv == 6 or lv == 7):
            econf = f"[{gasnobile}] {lv}s2 {lv - 2}f14 {lv - 1}d{valenza}"
        elif blocco == 'f':
            econf = f"[{gasnobile}] {lv}s2 {lv - 2}f{valenza}"
        return econf

def ces(z):
    with open('elementi.csv',encoding='ISO-8859-1',newline="") as elm:
        elm = csv.reader(elm,delimiter=',')
        for lista in elm:
            if str(z) == lista[0]:
                elemento = lista
        nat = int(elemento[0])
        if nat >= 2 and nat <= 10:
            gasnobile = '1s2'
        elif nat >= 11 and nat <= 18:
            gasnobile = '1s2 2s2 2p6'
        elif nat >= 19 and nat <= 36:
            gasnobile = '1s2 2s2 2p6 3s2 3p6'
        elif nat >= 37 and nat <= 54:
            gasnobile = '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6'
        elif nat >= 55 and nat <= 86:
            gasnobile = '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6'
        elif nat >= 87 and nat <= 118:
            gasnobile = '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6'
        blocco = elemento[4]
        valenza = int(elemento[5])
        lv = int(elemento[3])
        if nat == 1:
            econf = f"1s1"
        elif blocco == 's':
            econf = f"{gasnobile} {lv}s{valenza}"
        elif blocco == 'p' and (lv == 2 or lv == 3):
            econf = f"{gasnobile} {lv}s2 {lv}p{valenza}"
        elif blocco == 'p' and (lv == 4 or lv == 5):
            econf = f"{gasnobile} {lv}s2 {lv - 1}d10 {lv}p{valenza}"
        elif blocco == 'p' and (lv == 6 or lv == 7):
            econf = f"{gasnobile} {lv}s2 {lv - 2}f14 {lv -1}d10 {lv}p{valenza}"
        elif blocco == 'd' and (lv == 4 or lv == 5):
            econf = f"{gasnobile} {lv}s2 {lv - 1}d{valenza}"
        elif blocco == 'd' and (lv == 6 or lv == 7):
            econf = f"{gasnobile} {lv}s2 {lv - 2}f14 {lv - 1}d{valenza}"
        elif blocco == 'f':
            econf = f"{gasnobile} {lv}s2 {lv - 2}f{valenza}"
        return econf

def nametoz(name):
    while True:
        try:
            with open('elementi.csv') as elementi2:
                elementi2 = csv.reader(elementi2)
                for zn in elementi2:
                    if name == zn[1]:
                        z = zn[0]
                return z
        except UnboundLocalError:
            print('Please, insert an existing atom...')
            name = input('Insert the atom\'s name => ')
            continue

def ztoname(z):
    while True:
        try:
            with open('elementi.csv') as elementi:
                elementi = csv.reader(elementi)
                for zn in elementi:
                    if zn[0] == str(z):
                        zn = zn[1]
                        name = str.upper(zn[0]) + zn[1:]
                        return name
        except UnboundLocalError:
            print(f"Your atom (z={z}) doesn't exist...")
            z = input('Insert your atom => ')
            continue

def zncreation(tatomo):
    while True:
        if tatomo == 2:
            try:
                zn = int(input('Insert your atom => '))
            except ValueError:
                print('Please, insert a whole numeric value!')
                continue
            if int(zn) <= 0 or int(zn) >= 119:
                print('Your atom doesn\'t exist, insert an existing atom [1-118]')
                continue
            else:
                return zn
        else:
            zn = input('Insert your atom => ')
            zn = nametoz(zn)
            return zn

def scelta(mod,atom):
    if int(mod) == 1: #configurazione elettronica estesa.
        econf = ces(atom)
    elif int(mod) == 2: #Conifgurazione elettronica compatta.
        econf = cesc(atom)
    return econf

def reboot():
    print('Reboot in:\n3')
    time.sleep(1)
    print('\n2')
    time.sleep(1)
    print('\n1')
    time.sleep(1)
    print('\n\n\n\n\n')
    return