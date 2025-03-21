# Naprogramuj v Pythonu Builder. Prodejce, který prodává jablka kde vždy uveden rok sklizně,
# původ a odrůdu. Využijte návrhového vzoru Builder k sestaveni instance objektu ,,Úroda“ 
# a udělejte výpis do konzole, který se zobrazí po spuštění kódu. Kde budou tři předchozí 
# údaje – sklizeň rok: 2010, původ: Morava a odrůda: sladké.


class Apple():
    def __init__(self, rok, puvod, odruda):
        self.rok = rok
        self.puvod = puvod
        self.odruda = odruda

    def __str__(self):
        return f"rok:{self.rok}; puvod:{self.puvod}; odruda:{self.odruda}"
    
class AppleBuilder():
    
    def __init__(self):
        pass

    def rok(self, rok):
        self.rok = rok
        return self
    
    def puvod(self, puvod):
        self.puvod = puvod
        return self
    
    def odruda(self, odruda):
        self.odruda = odruda
        return self
    
    def build(self):
        return Apple(self.rok, self.puvod, self.odruda)
        
if __name__ == "__main__":
    a = AppleBuilder().rok("2010").odruda("sladke").puvod("morava").build()
    print(a)
