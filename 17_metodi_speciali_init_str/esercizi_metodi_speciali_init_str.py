"""
Esercizio di fine lezione "Metodi speciali __init__ e __str__

crea una classe Libro con attributi titolo e autore
nel __init__ inizializza i valori
nel __str__ restituisci una frase tipo: "Titolo: X , Autore: Y"

Esempio

libro = Libro("1984","George Orwell")
print(libro) #output: titolo: 1984, autore: George Orwell
"""

class Libro:

    def __init__(self, titolo, autore):
        self.titolo = titolo 
        self.autore = autore 

    def __str__(self):
        return f"Titolo: {self.titolo}\nAutore: {self.autore}"
    


#Esecuzione 

libro1 = Libro("1984","George Orwell")

print(libro1)