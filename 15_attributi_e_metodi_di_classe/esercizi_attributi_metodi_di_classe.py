"""
Esercizio di fine lezione "Attributi e metodi di classe"

crea una classe Studente con:
-attributo di classe scuola = "Liceo Classico"
-Attributo di istanza nome
-metodo di istanza presentati() che stampa "Sono X e frequento Y"
-metodo di classe cambia_scuola(cls, nuova_scuola) che modifica scuola per tutti gli studenti
-prova a creare 2 studenti e cambiare la scuola

"""

class Studente:

    scuola = "Liceo Classico" #attributo di classe 

    def __init__(self, nome):
        self.nome = nome 

    def presentati(self):
        print(f"Ciao sono {self.nome} e frequento {self.scuola}" )
    
    @classmethod #decoratore per dichiarare un metodo di classe
    def cambia_scuola(cls,nuova_scuola):
        cls.scuola = nuova_scuola


#------ESECUZIONE---------------------------------------------------------------------------------#

s1 = Studente("Raffaele")
s2 = Studente("Roberta")

s1.presentati()
s2.presentati()

s1.cambia_scuola("Tecnico commerciale")

s1.presentati()
s2.presentati()


