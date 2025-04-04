import threading
import time
import random

class Parkoviste:
    def __init__(self, kapacita):
        self.semafor = threading.Semaphore(kapacita)
        self.kapacita = kapacita
        self.obsazeno = 0
        self.lock = threading.Lock()

    def zaparkovat(self, auto_id):
        print(f"Auto {auto_id} se snaží zaparkovat.")
        self.semafor.acquire()
        with self.lock:
            self.obsazeno += 1
            print(f"Auto {auto_id} zaparkovalo {self.obsazeno}/{self.kapacita} míst obsazeno.")
        time.sleep(random.randint(1, 3))
        with self.lock:
            self.obsazeno -= 1
            print(f"Auto {auto_id} odjíždí {self.obsazeno}/{self.kapacita} míst obsazeno.")
        self.semafor.release()
    
kapacita = 5
parkoviste = Parkoviste(kapacita)
auta = []
for i in range(5):
    auto = threading.Thread(target=parkoviste.zaparkovat, args=(i,))
    auta.append(auto)
    auto.start()

for auto in auta:
    auto.join()

print("Všechna auta projela parkovištěm.")