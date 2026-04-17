"""
Esercizio di fine lezione "Attributi e metodi di istanza"

-crea una classe Studente con attributi nome ed età
-istanzia due studenti diversi e stampane i dati
-aggiungi alla classe Studente un metodo presentati() che stampi un messaggio con nome ed età
-prova ad aggiungere un attributo "al volo" a uno studente, ad esempio corso, e stampalo

"""

class Studente:

    def __init__(self,nome, eta):
        self.nome = nome 
        self.eta = eta 
    
    def presentati(self):
        print(f"Ciao sono {self.nome} e ho {self.eta} anni.")


s1 = Studente("Raffaele",33)
s2 = Studente("Roberta",27)

print(f"Studente {s1.nome}, {s1.eta} anni")
print(f"Studente {s2.nome}, {s2.eta} anni")

#In questo caso l'errore è evidenziato da Pylance che è una estensione dell'editor rigorosa
# type: ignore
s1.corso = "Informatica" #metodo aggiunto al volo, consentito da python

print(f"Studente {s1.nome}, {s1.eta} anni e frequento {s1.corso}")