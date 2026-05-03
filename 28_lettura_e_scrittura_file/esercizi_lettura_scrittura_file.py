"""
Crea una classe Appunti che salvi in un file ogni riga scritta dall'utente
Aggiugi un metodo mostra() che stampi il contenuto del file
estendi la classe con un metodo cancella() che svuoti il file
"""

from datetime import datetime

class Appunti:

    def __init__(self, nome_file):
        self.nome_file = nome_file 

    def scrivi_appunti(self, testo):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(self.nome_file, "a") as f:
            f.write(f"[{timestamp}] {testo}\n")

    def leggi_appunti(self):
        with open(self.nome_file,"r") as f:
            return f.read()

class CancellaAppunti(Appunti):

    def __init__(self, nome_file):
        super().__init__(nome_file)

    def cancella_file(self,nome_file):
        with open(self.nome_file,"w"): #cancello il contenuto del file
            pass

#=======================================================================================#
#======== ESECUZIONE ===================================================================#

appunti = Appunti("28_lettura_e_scrittura_file/appunti.txt")

appunti.scrivi_appunti("Ciao oggi ho fatto una camminata.")
print(appunti.leggi_appunti())

