"""
crea un file libri.csv con colonne: titolo, autore, anno.
scrivi una classe GestoreLibri che legga il file e stampi i titoli
aggiungi un metodo che stampi solo i libri di un certo autore
"""
import csv

class GestoreLibri:

    def __init__(self, file):
        self.file = file 
    
    def leggi(self):
        try:
            with open(self.file, "r", encoding="utf-8", newline='') as f:
                dati = list(csv.DictReader(f))

                if not dati:
                    print("Il file è vuoto.")
                    return []

                # --- Logica di stampa ordinata ---
                print(f"\n{'CONTENUTO DEL FILE':-^60}") # Titolo centrato
                print("-" * 60)

                # Prende le intestazioni dalle chiavi del primo dizionario
                headers = dati[0].keys()
                header_line = " | ".join(f"{h.upper():<18}" for h in headers)
                print(header_line)
                print("-" * 60)

                # Stampa ogni riga
                for riga in dati:
                    row_line = " | ".join(f"{str(riga[h]):<18}" for h in headers)
                    print(row_line)
                print("-" * 60 + "\n")
                # ---------------------------------

                return dati

        except FileNotFoundError:
            print("Errore: File non trovato.")
            return []


    def leggi_autore(self,autore):

        trovato = False

        with open (self.file,"r") as f:
            reader = csv.DictReader(f)
            
            for riga in reader:
                if riga["autore"] == autore:
                    trovato = True
                    print(riga["titolo"], riga["autore"], riga["anno"])
                    
            if trovato == False:
                print("Autore non trovato")
                    

#===================================================================================#

if __name__ == '__main__':

    gestoreLibri = GestoreLibri("29_lettura_di_file_CSV/libri.csv")

    gestoreLibri.leggi()
    
    gestoreLibri.leggi_autore("Primo Levi")