"""
esercizio della lezione "Incapsulamento"

crea una classe ContoBancario con:
-attributo privato __saldo
-metodo deposita(importo) che aggiunge soldi solo se > 0
-metodo preleva(importo) che riduce il saldo solo se sufficiente
-simula alcune operazioni di deposito e prelievo

"""

class ContoBancario:

    def __init__(self, nome, saldo):
        self.nome = nome
        self.__saldo = saldo

    def deposita(self, saldo):
        if saldo > 0:
            self.__saldo = self.__saldo + saldo
            print("----------STAI SVOLGENDO UN'AZIONE DI DEPOSITO ----------------------------")
            print(f"SALDO DEPOSITATO {saldo} --- SALDO ATTUALE: {self.__saldo}")
    
    def preleva(self, saldo):
        print("----------STAI SVOLGENDO UN'AZIONE DI PRELIEVO ----------------------------")
        if saldo <= self.__saldo:
            self.__saldo = self.__saldo - saldo
            print(f"SALDO PRELEVATO: {saldo}")
        else:
            print("ATTENZIONE: NON CI SONO SOLDI DISPONIBILI!!!")
        return f"SALDO ATTUALE: {self.__saldo}"
    
    def __str__(self):
        return f"IDSALDO: {self.nome}\nSALDO:{self.__saldo}"
    
    @property #metodo getter che considera __saldo come un attributo pubblico
    def saldo(self):
        return self.__saldo


#----------ESECUZIONE-------------------------------------------------#

conto1 = ContoBancario("conto1",1300)

print(conto1) #uso del metodo speciale __str__ customizzato
print(conto1.saldo)

print(conto1.preleva(400))
print(conto1.preleva(400))
print(conto1.preleva(400))
print(conto1.preleva(400))
conto1.deposita(1000)
print(conto1.preleva(400))








