"""
programek
"""

seznam = [10,20,30,40,"ebahada"]

SOUCET = 0

try:
    for prvek in seznam:
        SOUCET += prvek
except TypeError:
    print("chyba")
else:
    print("výhra")
    print(f"vysledek je {SOUCET}")
finally:
    print("ende šlus")
