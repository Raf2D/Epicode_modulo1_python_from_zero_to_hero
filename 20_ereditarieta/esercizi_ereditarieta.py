"""

Esercizio di fine lezione "Ereditarietà"

crea una classe Animale con attributo nome e metodo verso()
poi crea due classi derivate:
-cane verso() stampa "bau"
-gatto verso() stampa "miao"

crea un oggetto di ciascuna classe e chiama il metodo verso()
questo esercizio mostra chiaramente come ereditare e sovrascrivere i metodi

"""

class Animale:

    def __init__(self, nome, specie):
        self.nome = nome 
        self.specie = specie

    def verso(self): 
        return ""
    
    def __str__(self):
        # Questo funzionerà per Cane, Gatto e qualsiasi altro animale
        return f"{self.nome} è un {self.specie}"

class Cane(Animale):

    def __init__(self, nome, razza):
        super().__init__(nome, specie = "CANE")
        self.razza = razza 

    def verso(self): # type: ignore
        return "Bau Bau" 

    def __str__(self):
        # super().__str__() richiama "Nome: Fido (CANE)"
        # e noi aggiungiamo " - Razza: Labrador"
        return f"{super().__str__()} - Razza: {self.razza}"
    
class Gatto(Animale):

    def __init__(self, nome,razza):
        super().__init__(nome, specie = "GATTO")
        self.razza = razza 

    def verso(self): # type: ignore
        return "Miao Miao" 
    
    def __str__(self):
        return f"{super().__str__()} - Razza: {self.razza}"
    
#-----ESECUZIONE-------------------------------------------#

cane1 = Cane("fido","Labrador") 
gatto1 = Gatto("Birba","Siamese") 

print(cane1)
print(cane1.verso())
print(gatto1)
print(gatto1.verso())


