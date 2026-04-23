"""
Esercizio di fine lezione "Decoratori di classe e Property Decorators

crea una classe Studente che abbia:
@classmethod per creare uno studente a partire da una stringa tipo "Luca-20-Matematica"
@property per calcolare automaticamente l'anno di nascita a partire dall'età
@propery come setter per impedire età negative
"""

from datetime import datetime 

class Studente:
    
    def __init__(self,nome,eta,corso):
        self._nome = nome
        self._eta = eta 
        self._corso = corso

    @classmethod 
    def da_stringa(cls,stringa):
        nome, eta, corso = stringa.split("-")
        return cls(nome, eta, corso)
    
    @property
    def anno_di_nascita(self):
        return  datetime.now().year - self._eta
    
    @property 
    def nome(self):
        return self._nome
    @property 
    def eta(self):
        return self._eta
    @property 
    def corso(self):
        return self._corso
    

    @eta.setter
    def set_eta(self, eta):
        if(eta<0):
            print("Non puoi inserire una età negativa.")
        else:
            self._eta = eta

#--------------ESECUZIONE------------------------------------------#

studente1 = Studente("Luce",15,"informatica")

print(studente1.anno_di_nascita)
print(studente1.eta)
studente1.set_eta = 20 #viene considerato come un attributo
print(studente1.eta)



