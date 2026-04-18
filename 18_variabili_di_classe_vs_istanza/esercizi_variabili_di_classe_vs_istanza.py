"""
esercizio di fine lezione "Varibili di classe Automobili con:
-variabile di classe ruote = 4
-variabile di istanza modello
crea due automobili con modelli diversi e stampa il numero di ruote e i modelli
"""

class Automobile:

    ruote = 4

    def __init__(self,modello):
        self.modello = modello 

    def __str__(self):
        return f"Modello: {self.modello}\nRuote: {self.ruote}"

#-----------ESECUZIONE------------------------------------------------#

auto1 = Automobile("fiat 1")
auto2 = Automobile("fiat 2")

print(auto1)
print(auto2)
auto2.ruote = 6 #qui creao una variabile ruote al volo che si riferisce solo all'istanza
print(auto1)
print(auto2)

print("\nCambio valore della varibile di classe RUOTE")
Automobile.ruote = 2
print(auto1)
print(auto2)


