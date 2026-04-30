"""

esercizio di fine lezione: Operator overloading

Crea una classe Frazione che rappresenti una frazione con numeratore e denominatore.
implementa i seguenti operatori:

+ somma tra frazioni
== uguaglianza tra frazioni, semplificando i valori
__str__ per stampare la frazione come 3/4

"""
import math 

class Frazione:

    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        if denominatore == 0:
            return f"Il denominatore non può essere 0"
        else:
            self.denominatore = denominatore
    
    def __add__(self,other):
        if isinstance(other,Frazione):
            return Frazione(self.numeratore * other.denominatore + other.numeratore * self.denominatore, self.denominatore * other.denominatore)
        else: 
            return NotImplemented
    
    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"
    
    def __eq__(self,other):
        #prodotto incrociato senza semplificare: a/b = c/d è vero se a * d = c * b 
        if isinstance(other,Frazione):
            #Calcoliamo l'MCD per la prima frazione 
            mcd1 = math.gcd(self.numeratore, self.denominatore)
            s_num = self.numeratore // mcd1 
            s_den = self.denominatore // mcd1

            mcd2 = math.gcd(other.numeratore, other.denominatore)
            o_num = other.numeratore // mcd2 
            o_den = other.denominatore // mcd2 

            return s_num == o_num and s_den == o_den
        return False



        

#================ESECUZIONE==========================================#

if __name__ == '__main__':

    print("Avvio del programma...")

    frazione1 = Frazione(1,6)
    frazione2 = Frazione(7,17)

    print(frazione1 + frazione2)

    print(f"{frazione1} e {frazione2} sono uguali ?", frazione1 == frazione2)

    frazione3 = Frazione(1,6)
    frazione4 = Frazione(2,12)

    print(frazione1 + frazione2)

    print(f"{frazione3} e {frazione4} sono uguali ?", frazione3 == frazione4)


