
import random
import json
from datetime import datetime, timedelta

#----------------------------------------------------------------
#----------- CLASSE UTENTE --------------------------------------

class Utente:

    _id_utente = 1 #variabile di classe

    def __init__(self, nome, eta):

        self._nome = nome 
        self._eta = eta 
        self._id_utente = Utente._id_utente
        Utente._id_utente += 1
    
    #--------GETTER---------------------------------#
    @property
    def nome(self):
        return self._nome 
    
    @property
    def eta(self):
        return self._eta 
    
    @property 
    def id_utente(self):
        return self._id_utente
    
    #---------SETTER--------------------------------#

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @eta.setter
    def eta(self, eta):
        self.eta = eta
    

    def scheda(self):
         
         return (f"-------------------\n"
                f"Nome utente: {self.nome}\n"
                f"età: {self.eta}\n"
                f"Id utente: {self.id_utente}\n"
                f"--------------------")
    
    # Definisce quando gli utenti sono considerati uguali
    def __eq__(self, other):
        if not isinstance(other, Utente):
            return False 
        return self._id_utente == other._id_utente #confronta gli ID 

    # Genera un codice numerico basato sull'ID (necessario per i set)
    def __hash__(self):
        return hash(self._id_utente)
    
    def __repr__(self):
        return f"Utente(ID: {self._id_utente}, Nome: {self._nome})"
    
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------- CLASSE LIBRO ---------------------------------------------------------


class Libro:

    def __init__(self, titolo_libro, autore, anno, numero_copie, prezzo: float, stato: bool): #Type Hints
        self._titolo_libro = titolo_libro
        self._autore = autore
        self._anno = anno
        self._numero_copie = numero_copie
        self._prezzo = prezzo
        self._stato = stato
    

    #------- GETTER -------------------------------#

    @property
    def titolo_libro(self):
        return self._titolo_libro
    
    @property
    def autore(self):
        return self._autore
    
    @property
    def anno(self):
        return self._anno
    
    @property
    def numero_copie(self):
        return self._numero_copie
    
    @property
    def prezzo(self):
        return self._prezzo
    
    @property
    def stato(self):
        return self._stato
    
    #------- SETTER -------------------------------#
    
    @titolo_libro.setter
    def titolo_libro(self, titolo):
         self._titolo_libro = titolo
    
    @autore.setter
    def autore(self, autore):
         self._autore = autore
    
    @anno.setter
    def anno(self, anno):
         self._anno = anno
    
    @numero_copie.setter
    def numero_copie(self, numero):
         self._numero_copie = numero
    
    @prezzo.setter
    def prezzo(self, prezzo):
         self._prezzo = prezzo
    
    @stato.setter
    def stato(self, stato):
         self._stato = stato

    def info(self):
         status = "Disponibile" if self.stato else "Non disponibile"
         return (f"-------------------\n"
                f"titolo: {self.titolo_libro}\n"
                f"autore: {self.autore}\n"
                f"anno: {self.anno}\n"
                f"prezzo: {self.prezzo}\n"
                f"stato: {self.stato}\n"
                f"-------------------")

class Prestito:

    def __init__(self, utente_obj, libro_obj):
        if libro_obj.numero_copie > 0:
            self._utente = utente_obj
            self._libro = libro_obj
            self._libro.numero_copie -= 1 #Sottraiamo una copia dall'oggetto Libro
            self._data_inizio = datetime.now()
            giorni_casuali = random.randint(7, 30) #generiamo un numero di giorni casuali per il prestito
            self._data_scadenza = self._data_inizio + timedelta(days = giorni_casuali)
        else:
            raise ValueError(f"Attenzione:copie esaurite. {libro_obj.titolo_libro}")
    
    def dettagli(self):
        #formattiamo le date per renderle leggibili 
        inizio_str = self._data_inizio.strftime("%d/%m/%Y")
        scadenza_str = self._data_scadenza.strftime("%d/%m/%Y")
        #accediamo ai getter degli oggetti collegati
        return (f"Libro: {self._libro.titolo_libro}\n | Prestato: {self._utente.nome}\n"
                f"Data Inizio: {inizio_str} | Scadenza: {scadenza_str}\n"
                f"---------------------------------------------------------------------\n")
    
    @staticmethod
    def elenco_prestiti(prestiti):
        inventario = {prestito._libro.titolo_libro: prestito._libro.numero_copie for prestito in prestiti}
        print("INVENTARIO AGGIORNATO: ")
        print(json.dumps(inventario, indent=4, sort_keys=True))
        return inventario
        

#------------------------------------------------------------

#============================================================================================
#===== ESECUZIONE PROGRAMMA =================================================================

if __name__ == '__main__':

    # Creazione degli oggetti libri
    libro1 = Libro("Il nome della rosa", "Umberto Eco", 1980, 4, 14.45, True)
    libro2 = Libro("1984", "George Orwell", 1949, 8, 12.45, True)
    libro3 = Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry", 1943, 1, 16.45, True)
    libro4 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 2, 19.60, True)
    libro5 = Libro("Cronaca di una morte annunciata", "Gabriel García Márquez", 1981, 8, 20.10, True)

    libri = [libro1, libro2, libro3, libro4, libro5]

    for libro in libri:
        print(libro.info())


    #------creazione del dizionario : titolo - numero di copie disponibili-----------

    inventario = {libro.titolo_libro: libro.numero_copie for libro in libri}
    print("DiZIONARIO: ",inventario)

    #------creazione set di utenti registrati----------------------------------------

    utenti_registrati = {Utente("mario85", 25), Utente("giulia_green", 22), Utente("luca_verdi", 30)}

    for utente in utenti_registrati:
        print(utente.scheda())

    for utente in utenti_registrati:
        print(utente)
    
    

    #Creazione prestiti
    prestiti = []
    for utente, libro in zip(utenti_registrati, libri):
        try:    
            nuovo_prestito = Prestito(utente, libro)
            prestiti.append(nuovo_prestito)
            print(f"Prestito creato con successo. Libro: {libro.titolo_libro} Detentore: {utente.nome} - {utente.id_utente}")
        except ValueError as e:
            print(e)

        #Stampo i prestiti
        for prestito in prestiti:
            print(prestito.dettagli())

    #stampiamo i dettagli del numero di copie rimanenti per ogni libro 
        Prestito.elenco_prestiti(prestiti)
    


    
    