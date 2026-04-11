#Esercizio lezione "Funzioni"

#Definisci una funzione chiamata media che:
#riceve una lista di numeri (parametro)
#calcola e restituisce la media (somma/numero elementi)

#ad esempio:
#print(media([2,4,6]))

#usa len() e sum() per renderla più semplice, leggibile ed efficacie

#--------------------------------------------------------------------------------------#

def media (lista_numeri):
    return sum(lista_numeri)/len(lista_numeri)

def media2 (*args):
    return sum(args)/len(args)

lista = [1,2,4,6,7,8,9]

print("Ecco la media della lista: ", media(lista))
print("Ecco la media della lista: ", media2(1,2,4,6,7,8,9))
