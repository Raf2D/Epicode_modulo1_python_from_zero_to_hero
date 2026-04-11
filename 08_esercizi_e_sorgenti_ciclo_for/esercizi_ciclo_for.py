#Esercizio lezione ciclo FOR:

#Scrivi un programma che:
#ha una lista di nomi
#stampa ogni nome preceduto dal proprio numero d'ordine (es. 1. Alice)
#usa enumerate() per ottenere numero e nome

lista = ["Francesco","Giacomo","Eraldo","Daniele"]

for i,nome in enumerate(lista): #prima l'indice poi il nome corrispondente della lista
    print(i+1," ",nome)