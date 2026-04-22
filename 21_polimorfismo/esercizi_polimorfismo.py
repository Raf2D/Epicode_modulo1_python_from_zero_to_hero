"""
Esercizio lezione "Polimorfismo"

crea una classe base Forma con metodo area()
crea due classi derivate:
-Rettangolo: area = base * altezza
-Cerchio: area = pigreco * r^2 

crea una lista di forme e stampa l'area di ciascuna usando lo stesso metodo area()

"""
import math as mt

class Forma:

    def area(self):
        raise NotImplementedError("Sottoclasse deve implementare area()")

class Rettangolo(Forma):

    def __init__(self, base, altezza, tipo = 'Rettangolo'):
        self.base = base 
        self.altezza = altezza 
        self.tipo = tipo

    def area(self):
        return self.base*self.altezza
    
class Cerchio(Forma): 

    def __init__(self,raggio, tipo ='Cerchio'):
        self.raggio = raggio 
        self.tipo = tipo

    def area(self):
        return (self.raggio**2) * mt.pi
    

#--------ESECUZIONE------------------------------------------#

forme = [Rettangolo(10,5),Cerchio(7),Rettangolo(4,4)]

for forma in forme:
    print(f"L'area del {forma.tipo} è: ", forma.area())
