#Vytvořte konzolovou kalkulačku
#○ v konzolovém menu bude na výběr sčítání, odčítání, násobení, dělení a ukončení programu
# ○ uživatel si vybere operaci, poté zadá 2 čísla
# ○ uživatel kalkulačku může využívat opakovaně, ukončí se až to uživatel vybere v menu

while True:
    print("Vyber operaci")
    print("1 - sčítání")
    print("2 - odcitani")
    print("3 - nasobeni")
    print("4 - deleni")
    print("5 - ukonceni programu")

    picked_number = int(input("Zadej číslo: "))

    if picked_number > 5 or picked_number < 1:
        print("špatne cislo")
        continue

    if picked_number == 5:
        break

    num1 = int(input("cislo 1: "))
    num2 = int(input("cislo 2: "))

    if picked_number == 1:
        print(f"Scitani - {num1} + {num2} = {num1+num2}")
    elif picked_number == 2:
        print(f"Scitani - {num1} - {num2} = {num1-num2}")
    elif picked_number == 3:
        print(f"Scitani - {num1} * {num2} = {num1*num2}")
    elif picked_number == 4:
        print(f"Scitani - {num1} / {num2} = {num1/num2}")

    