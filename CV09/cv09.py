import random

def hod_minci():
    return random.choice([1, 2])

def hlavni_program():
    try:
        opakovani = int(input("zadej pocet opakovani: "))
        if opakovani <= 0:
            print("pocet opakovani musi byt kladne cislo")
            return
    except ValueError:
        print("zadej platne cislo")
        return
    
    vyhry = 0
    prohry = 0

    for i in range(opakovani):
        volba = input("chcete vsadit na Panna (1) nebo Orel (2)? Zadejte 1 nebo 2: ")

        if volba not in ['1', '2']:
            print("neplatna volba")
            continue
        volba = int(volba)

        vysledek = hod_minci()

        if volba == vysledek:
            print(f"Vybral jste{'Panna' if volba == 1 else 'Orel'}, a padl{'Panna' if vysledek == 1 else 'Orel'}. Vyhral jste")
            vyhry += 1
        else:
            print(f"Vybral jste{'Panna' if volba == 1 else 'Orel'}, a padl{'Panna' if vysledek == 1 else 'Orel'}. Prohral jste")
            prohry += 1

    print(f"\nCelkovy pocet vyher: {vyhry}, Celkovy pocet proher: {prohry}.")

hlavni_program()