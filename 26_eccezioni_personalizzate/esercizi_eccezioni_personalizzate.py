"""
Crea una classe Studente con attributo età
se l'età è negativa solleva EtàNonValidaError
crea una classe Magazzino con metodo rimuovi_prodotto(nome, quantità)
se non ci sono abbastanza pezzi, solleva ProdottoEsauritoError

(Facoltativo) Organizza le tue eccezioni sotto una clase base ErroreScuola o ErroreMagazzino

"""

#============= SEZIONE MAGAZZINO e PRODOTTO ============================================
class Prodotto:
    #classe prodotto per dare un ordine di struttura al programma
    def __init__(self, nome, quantita):
        self.nome = nome 
        self.quantita = quantita

    def __repr__(self): #per riprodurre l'oggetto in maniera testuale
        return f"{self.nome} (qt: {self.quantita})"
    

class MagazzinoError(Exception):
    pass

class QuantitaInvalidaError(MagazzinoError):
    def __init__(self, prodotto, qta):
        super().__init__(f"Errore: il prodotto {prodotto} non può avere quantità negativa.")
        self.prodotto = prodotto 
        self.qta = qta

class QuantitaInsufficenteError(MagazzinoError):
    #Sollevata quando si prava a rimuovere piu di tanto disponibile
    def __init__(self, disponibile, richiesto):
        super().__init__(f"Quantità insufficiente: disponibili {disponibile}, richiesti {richiesto}")
        self.richiesto = richiesto 
        self.disponibile = disponibile

class Magazzino:
    def __init__(self, dizionario_prodotti):
        #usiamo una list comprehension per creare la lista di oggetti Prodotto
        self.inventario = []
        for nome, qta in dizionario_prodotti.items():
            if qta < 0: 
                raise QuantitaInvalidaError(nome, qta)
            self.inventario.append(Prodotto(nome,qta))


    def rimuovi_prodotti(self, nome_prodotto, quantita_da_togliere):

        presente = False

        for p in self.inventario:
            if p.nome == nome_prodotto:
                
                presente = True

                if p.quantita < quantita_da_togliere:
                    #possiamo sollevare un'eccezione se non ce ne abbastanza 
                    raise QuantitaInsufficenteError(p.quantita, quantita_da_togliere)
                else:
                    p.quantita -= quantita_da_togliere
                    print(f"Rimosse {quantita_da_togliere} unità di {nome_prodotto}")

                if p.quantita == 0:
                    self.inventario.remove(p)
                    print(f"Prodotto {nome_prodotto} esaurito e rimosso dall'inventario.")
        
        if not presente :
            print(f"Errore: il prodotto {nome_prodotto} non è presente in magazzino.")


#==============================================================================================
#===============SEZIONE SCUOLA E STUDENTE======================================================

class ErroreScuola(Exception):
    """Classe base per tutti gli errori della scuola."""
    pass 

class StudenteError(ErroreScuola):
    def __init__(self, nome, cognome, eta):
        # Usiamo 'eta' senza accento per convenzione nei nomi variabili, 
        # ma nel messaggio mettiamo quello che vogliamo
        super().__init__(f"L'età {eta} per lo studente {nome} {cognome} non è valida.")
        self.nome = nome 
        self.cognome = cognome 
        self.eta = eta

class Studente:
    def __init__(self, nome, cognome, eta, corso):
        # Controllo più robusto
        if eta < 0:
            raise StudenteError(nome, cognome, eta)
        if eta < 16:
            raise StudenteError(nome, cognome, eta)
        
        self.nome = nome 
        self.cognome = cognome 
        self.eta = eta 
        self.corso = corso 

if __name__ == '__main__':

    #--------ESECUZIONE TEST STUDENTE---------------------------------------------------
    try:
        s1 = Studente("Raffaele", "Caputi", -1, "Informatica")
    except StudenteError as e: 
        print(f"Errore rilevato: {e}")
        if e.eta < 0:
            print("Nota: L'età non può essere un numero negativo!")
        else:
            print("Nota: L'iscrizione è riservata ai maggiori di 16 anni.")
    
    
    #----ESECUZIONE TEST MAGAZZINO--------------------------------------------

    #----aggiungo prodotti all'inventario magazzino---------------------------

    dati = {"Laptop":5, "Mouse":10}
    miei_prodotti = Magazzino(dati)


    #----------RIMOZIONE prodotto MOUSE---------------------------------------

    try:
        #tentativo di rimuove troppi Mouse 
        miei_prodotti.rimuovi_prodotti("Mouse",15)
        
        
    except QuantitaInsufficenteError as e:
        print(f"ERRORE: {e}")
        print(f"Mancano {e.richiesto - e.disponibile} per completare l'eliminazione.")
    else: 
        print(f"Inventario aggiornato: {miei_prodotti.inventario}")

    #---------RIMOZIONE prodotto LAPTOP-----------------------------------------------------
    try:

        #tentativo corretto
        miei_prodotti.rimuovi_prodotti("Laptop", 5)
        
        
    except QuantitaInsufficenteError as e:
        print(f"ERRORE: {e}")
        print(f"Mancano {e.richiesto - e.disponibile} per completare l'eliminazione.")
    else: 
        print(f"Inventario aggiornato: {miei_prodotti.inventario}")


    #--------RIMOZIONE PRODOTTO NON PRESENTE--------------------------------------------
    try:

        #tentativo corretto
        miei_prodotti.rimuovi_prodotti("Computer", 2)
        
        
    except QuantitaInsufficenteError as e:
        print(f"ERRORE: {e}")
        print(f"Mancano {e.richiesto - e.disponibile} per completare l'eliminazione.")
    else: 
        print(f"Inventario aggiornato: {miei_prodotti.inventario}")

    
    


