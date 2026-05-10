"""
Esecizio che fa riferimento all'integrazione tra diverse librerie in Data Science, ciscuna con un ruolo specifico.
- numpy: gestisce gli array e le operazioni numeriche.
- pandas: organizza i dati in tabelle.
- matplotlib e seaborn: gestiscono la visualizzazione.
- scikit learn: costruisce modelli di machine learning.

Esercizio: 
crea una serie di date (30 giorni consecutivi)
genera valori casuali associati alle date
crea un dataframe con indice temporale
dai un grafico a linea con i valori nel tempo
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# 1 creare una serie di date di 30 giorni consecutivi.
date_range = pd.date_range(start = '2026-01-01', periods = 30, freq = 'D')


# 2 genera valori casuali associati alle date.
# genera un array di 30 numeri casuali da 10 a 100
valori_casuali = np.random.randint(10, 100, size = 30)


# 3 creare un DataFrame con un indice temporale
# passando index = data_range trasformiamo il DataFrame in una serie temporale.
# questo permette a Pandas e Matplotlib di gestire automaticamente le etichette delle date sull'asse X

df = pd.DataFrame(data = {'Valore': valori_casuali}, index = date_range)



# 4 Realizzare un grafico a linee con i valori nel tempo
# abbiamo aggiunto marker='o' per evidenziare i singoli punti dati
# plt.xticks(rotation=45) per rendere le date leggibili ed evitare che si sovrappongano)

plt.figure(figsize=(10,5))
plt.plot(df.index, df['Valore'], marker='o', linestyle='-', color='b')



# Personalizziamo il grafico
plt.title('Andamento Valori Casuali nel tempo')
plt.xlabel('Data')
plt.ylabel('Valore')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()


# Mostra il grafico
plt.show()
