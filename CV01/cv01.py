# Naprogramujte program pro výpočet kvadratické rovnice v reálných číslech.
# Celý program bude v jedné funkci. Na vstupu budou hodnoty a, b, c. 
# V programu budou obsaženy všechny podmínky potřebné pro výpočet kvadratické rovnice. 
# Program udělejte tak, aby zde platil DRY princip. 
# Na výstupu bude/budou výsledek/výsledky kvadratické rovnice.
import math

def kvadraticka_rovnice(a, b, c):
    diskriminant = (b * b) - (4 * a * c)
    if diskriminant < 0:
        raise ValueError("Nelze odmocnovat zaporna cisla.")
    elif diskriminant > 0:
        x1 = ((-1 * b) + math.sqrt(diskriminant)) / (2 * a)
        x2 = ((-1 * b) - math.sqrt(diskriminant)) / (2 * a)
        return x1, x2
    elif diskriminant == 0: 
        x = (-1 * b) / (2 * a)
        return x

hodnota = kvadraticka_rovnice(1, -4, 1)
print(hodnota)