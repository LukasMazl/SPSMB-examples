class Person:
    def __init__(self, name, age, height, password):
        self.name = name
        self.age = age
        self.height = height
        self.__password = password

    def say_hi(self):
        return "Ahoj"

    def __str__(self):
        return f"{self.name}, {self.age}, {self.height}"
    
class Classmate(Person):
    def __init__(self, name, age, height, password):
        super().__init__(name, age, height, password)

    def say_hi(self):
        return super().say_hi() + " Nigga"
    
if __name__ == "__main__":
    person = Person("Kamil", 19, 193, "heslo123")
    classmate = Classmate("John", 20, 150, "heslo1234")
    print(person)
    print(classmate)
    print(person.say_hi())
    print(classmate.say_hi())
#Naprogramuj pomocí OOP kód, který vytvoří třídu Person, kde inicializujete name, age, height a password -> password bude využívat privátní modifikátor. Vytvořte ve třídě jednoduchou metodu, která bude vracet string “Ahoj“. Poté vytvoříte dunder metodu, která je určené pro výpis a pomocí ní vypíšete zmíněné informace Person (kromě password). Stejným způsob naprogramujte třídu Classmate, která nebude obsahovat metodu se stringem “Ahoj“, ale bude pomocí super() volat tuhle funkci od třídy Person