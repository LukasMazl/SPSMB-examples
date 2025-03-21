# Vytvoř program
#   kde budeš mít proměnné studenti, vek_studentu
#   uděláš třídu Student, kde bude jmeno a vek
#   vytvoříš funkci vytvor_studenty(), ve které bude lokální proměnná 
#       studenti_objekt, do kterého se uloží studenti se jmenem a vekem, funkce vrátí proměnnou studenti_objekt
#   vytvoris funkci ktera vypočítá průměrný věk studentů a zaokrouhli na cele cislo

import math

studenti = ["pepa", "michal", "petr"]
vek = [15, 18, 14]

class Student:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

def vytvor_studenty():
    studenti_objekt = []
    for i in range(0, len(studenti) - 1):
        student = Student(studenti[i], vek[i])
        studenti_objekt.append(student)
    return studenti_objekt

def prumerny_vek():
    prumer_vek = sum(vek) / len(vek)
    return prumer_vek

studenti = vytvor_studenty()
print(prumerny_vek())
