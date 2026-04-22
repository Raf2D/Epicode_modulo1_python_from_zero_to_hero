"""
Esercizio di fine lezione "Classi astratte"

Crea una classe astratta Veicolo con metodo astratto muovi()
poi crea due classi concrete:
Auto: muovi() stampa "L'auto si muove su strada"
Aereo: muovi() stampa "L'aereo vola nel cielo"

infine, scrivi una funzione che accetti un generico Veicolo e chiami muovi()

"""

from abc import ABC, abstractmethod

class Veicolo(ABC):

    @abstractmethod
    def muovi(self):
        pass 


#----Classe 1 : Auto ----------------------------------------------#
class Auto(Veicolo):

    def __init__(self, marca, tipo = 'auto'):
        self.marca = marca
        self.tipo = tipo
    
    def muovi(self):
        print("L'auto si muove su strada")

#----Classe 2 : Aereo ---------------------------------------------#
class Aereo(Veicolo):

    def __init__(self, marca, tipo = 'aereo'):
        self.marca = marca 
        self.tipo = tipo 

    def muovi(self):
        print("L'aereo vola nel cielo")


#------funzione esterna alle classi---------------------------------#
def esegui_muovi(veicolo):
    if not isinstance(veicolo, Veicolo):
        print(f"Errore {type(veicolo).__name__} non è un Veicolo")
    else:
        veicolo.muovi()


#-----ESECUZIONE---------------------------------------------#

auto1 = Auto("nissan")
aereo1 = Aereo("ryanair")

veicoli = [auto1, aereo1]

for veicolo in veicoli:
    esegui_muovi(veicolo)
