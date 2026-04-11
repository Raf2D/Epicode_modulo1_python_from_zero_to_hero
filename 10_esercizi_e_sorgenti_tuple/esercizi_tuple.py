#Esercizio lezione Tuple

#Crea una tupla con 3 colori
#stampa il primo e l'ultimo
#conta quante volte compare un colore

colori = ("giallo","rosso","verde","giallo","verde","giallo","verde","verde")

#stampo il primo e ultimo elemento della tupla
for i in range(len(colori)):
    if i == 0 :
        print("Primo elemento : ", colori[i])
    if i == len(colori)-1:
        print("Ultimo elemento : ", colori[i])
    
colori_distinti = [] #per evitare la ripetizione della stampa

#stampo quante volte compare un elemento
for colore in colori:
    if colore not in colori_distinti:
        print(f"il colore {colore} compare {colori.count(colore)} volte")
        colori_distinti.append(colore)
    


        