# Vytvoř složku, v ní soubor a poté přes git příkazy ukaž, kde se nachází. Vytvoř 3 inputy, do kterých uživatel postupně zadá 3 hodnoty (jméno, příjmení, věk), které poté vypíšeš v printu ve stylu (Uživatel se jmenuje [jmeno] [prijmeni] a je mu [vek] let.)
# Nakonec si vem od uzivatele 2 proměnné a udělej s nimi základní matematické operace (+, -, *, /) a jejich součet změň místo věku uživatele a vypiš to jako další print

name = input("Zadej jmeno: ")
surname = input("Zadej prijmeni: ")
age = int(input("Zadej vek"))

print("Uzivatel se jmenuje ", name , surname, "a je mu ", age, " let")

cislo1 = int(input("Prvni cislo"))
cislo2 = int(input("Druhy cislo"))

print(cislo1 + cislo2)
print(cislo1 - cislo2)
print(cislo1 * cislo2)
print(cislo1 / cislo2)
print(cislo1 ** cislo2)

print(cislo1 **0.5)