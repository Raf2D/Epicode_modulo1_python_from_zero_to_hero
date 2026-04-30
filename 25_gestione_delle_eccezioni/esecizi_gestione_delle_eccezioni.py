"""
Crea una classe Divisione con un metodo dividi(a, b) che gestisca la divisione per zero.

Crea una classe Persona che sollevi un ValueError se l'età inserita è negativa.

Crea una classe Banca con metodo preleva(). Se il saldo non basta, solleva un'eccezione personalizzata.

"""


class Divisione:

    @staticmethod
    def dividi(a,b):
        try:
            risultato = a/b

        except ValueError:
            print("Devi inserire un numero valido")
        except ZeroDivisionError:
            print("Non puoi dividere per zero")
        else: 
            return risultato
        
class Persona:

    def __init__(self, nome, cognome, eta):

        if eta < 0 : 
            raise ValueError("L'età inserita è negativa quindi non valida")
        else:
            self.nome = nome 
            self.cognome = cognome
            self.eta = eta
       
class Banca: 

    def __init__(self, nome_intestatario, saldo):
        self.nome_intestatario = nome_intestatario
        self.saldo = saldo 
    
    def preleva(self, prelievo):
        if prelievo > self.saldo:
            raise SaldoNonDisponibile("Non ci sono abbastanza soldi per prelevare la somma richiesta.")
        else: 
            self.saldo = self.saldo - prelievo

class SaldoNonDisponibile(Exception):
    pass 



#=============== ESECUZIONE =============================================================#


if __name__ == '__main__': 

    a = 3 
    b = 4 
    Divisione.dividi(a,b)
    print(f"la divisione tra {a} e {b} è {Divisione.dividi(a,b)}")

    conto = Banca('Raffaele_Caputi', 1200)

    conto.preleva(1000)
    print(conto.saldo)
    conto.preleva(300)