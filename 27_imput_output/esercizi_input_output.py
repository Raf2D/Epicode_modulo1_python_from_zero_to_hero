"""
Crea una classe Studente che chieda all'utente nome ed età e abbia un metodo presentati()
aggiungi a Studente un metodo __str__ che restituisca una stringa leggibile
crea una classe Diario che salvi su file un messaggio passato dall'utente
(facoltativo) Aggiungi un metodo che legga dal file e stampi i messaggi.

"""
#========= STUDENTE ======================================================#
#=========================================================================#
class Studente:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome 
    

    def chiedi_eta(self):
        self.eta = int(input("Inserisci la tua età:"))
    
    def presentati(self):
        print(f"Ciao sono {self.nome} {self.cognome} e ho {self.eta} anni.")

    def __str__(self):
        return f"class: Studente - nome {self.nome} - cognome {self.cognome} - età {self.eta}"

#===================================================================================================#
#===================================================================================================#


#======= DIARIO ====================================================================================#

class Diario:

    def __init__(self, etichetta, nome_file):
        self.etichetta = etichetta 
        self.nome_file = nome_file
    
    def stampa_su_file(self, messaggio):
        with open(self.nome_file,"a", encoding="utf-8") as f:
            f.write(messaggio + "\n")



#====== ESECUZIONE =================================================================================#

if __name__ == '__main__':


#------- studente --------------------------------------------
    studente1 = Studente("Raffaele","Caputi")
    studente1.chiedi_eta()
    print(studente1)



#------- diario ----------------------------------------------

diario1 = Diario("diario di raffaele","C:/Users/raffy/OneDrive/Documenti/GitHub/Epicode_modulo1_python_from_zero_to_hero/27_imput_output/diario.txt")
diario1.stampa_su_file("Ciao oggi è il 2 maggio")