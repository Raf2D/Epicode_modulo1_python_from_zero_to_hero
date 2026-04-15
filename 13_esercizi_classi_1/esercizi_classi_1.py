#Esercizio di fine lezione  "Il concetto di Oggetto"

#Scrivi una classe Studente con attributi nome e corso, e un metodo presentati() che stampa
#una frase di presentazione.

class Studente:

    def __init__(self, nome, cognome, corso):
            self.nome = nome 
            self.cognome = cognome 
            self.corso = corso 
    
    def presentazione(self):
          print(f"Ciao sono {self.nome} {self.cognome} e sono iscritto al corso di {self.corso}")


studente1 = Studente("Raffaele","Caputi","Informatica")
studente1.presentazione()
