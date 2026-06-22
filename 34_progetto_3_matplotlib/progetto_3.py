import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pathlib import Path


"""
Parte 1 : definizione variabili
"""

nome = 'Enrico Povia'
eta = 32 
saldo = 2500.75
vip = True

destinazioni = ["Roma","Bisceglie","Genoa","Taranto","Bari","Camogli","Brindisi","Padova","Ginevra","Viareggio"]
viaggi = {destinazione: round(random.uniform(200.0,2000.0),2) for destinazione in destinazioni} #dizionario associa destionazioni a prezzi

print(viaggi)


"""
Parte 2 
"""

class Cliente :

    def __init__(self, nome, eta : int, vip : bool, saldo : float):
      self.__nome = nome 
      self.__eta = eta 
      self.__saldo = saldo
      self.__vip = vip 

    def __str__(self):
      return (  f"Nome: {self.__nome}\n"
                f"Età: {self.__eta}\n"
                f"Saldo: {self.__saldo}\n"
                f"Vip: {self.__vip}"    )
    
    @property
    def nome(self):
       return self.__nome 
    
    @nome.setter 
    def nome(self, nuovo_nome):
       self.__nome = nuovo_nome

    @property
    def eta(self):
       return self.__eta 
    
    @eta.setter
    def eta(self, nuova_eta):
       self.__eta = nuova_eta 

    @property
    def saldo(self):
       return self.__saldo
    
    @saldo.setter
    def saldo(self, nuovo_saldo):
       self.__saldo = nuovo_saldo
   
    @property
    def vip(self):
       return self.__vip 
    
    @vip.setter 
    def vip(self, nuovo_vip):
       self.__vip = nuovo_vip
      

class Viaggio:
   
    def __init__(self, destinazione, prezzo: float, durata_giorni: int):
      self.__destinazione = destinazione
      self.__prezzo = prezzo 
      self.__durata_giorni = durata_giorni 
    
    def __str__(self):
      return (
         f"Destinazione: {self.__destinazione}\n"
         f"Prezzo: {self.__prezzo}€\n"
         f"Durata: {self.__durata_giorni} giorni.\n"
      )
    
    @property
    def destinazione(self):
       return self.__destinazione 
    
    @destinazione.setter 
    def destinazione(self, nuova_destinazione):
       self.__destinazione = nuova_destinazione 
    
    @property
    def prezzo(self):
       return self.__prezzo
    
    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
       self.__prezzo = nuovo_prezzo 
    
    @property
    def durata_giorni(self):
       return self.__durata_giorni 
    
    @durata_giorni.setter
    def durata_giorni(self,nuova_durata):
       self.__durata_giorni = nuova_durata 


class Prenotazioni:
   
   def __init__(self, cliente: Cliente, viaggio: Viaggio):
        if isinstance(cliente, Cliente) and isinstance(viaggio,Viaggio):
            self.__cliente = cliente 
            self.__viaggio = viaggio 
        else: 
           raise ValueError(f"ATTENZIONE:\n"
                            f"La variabile {cliente} deve essere una istanza di Cliente, ricevuto: {type(cliente).__name__}\n" 
                            f"la variabile {viaggio} deve essere una istanza di Viaggio, ricevuto: {type(viaggio).__name__}")
   

   def set_sconto_vip(self):
      if self.__cliente.vip :
         self.__viaggio.prezzo = self.__viaggio.prezzo - ((self.__viaggio.prezzo*10)/100)
   
   
   def __str__(self):
      return (f"Prenotazione:\n"
              f"A nome di: {self.__cliente.nome}\n"
              f"Destinazione: {self.__viaggio.destinazione}\n"
              f"Durata: {self.__viaggio.durata_giorni} giorni\n"
              f"Prezzo: {self.__viaggio.prezzo}\n"
              f"Vip: {self.__cliente.vip}"
      )


# ===========================================================================================================
# ===========================================================================================================

if __name__ == "__main__" :

   """
   Parte 3 – NumPy
   """

   prezzi_casuali = np.random.default_rng(seed=42).uniform(200.0, 2000.0, size = 100).round(2)

   # --- CALCOLI STATISTICI --- #

   prezzo_medio = np.mean(prezzi_casuali)
   prezzo_min = np.min(prezzi_casuali)
   prezzo_max = np.max(prezzi_casuali)
   # Deviazione standard (indica quanto i prezzi variano rispetto alla media)
   deviazione_standard = np.std(prezzi_casuali)
   # Creiamo una maschera booleana (True dove il prezzo è maggiore della media)
   # restituisce un array booleano, un valore per ogni prezzo o true o false a seconda dell'esito della condizione
   sopra_media = prezzi_casuali > prezzo_medio 
   perc_prenotazioni_sopra_media = np.mean(sopra_media) * 100

   print("--- STATISTICHE PRENOTAZIONI ---")
   # Allinea il testo a sinistra occupando 30 spazi (<30) e i numeri a destra occupando 8 spazi con 2 decimali (>8.2f)
   print(f"{'Prezzo Medio:':<30}{prezzo_medio:>8.2f} €")
   print(f"{'Prezzo Minimo:':<30}{prezzo_min:>8.2f} €")
   print(f"{'Prezzo Massimo:':<30}{prezzo_max:>8.2f} €")
   print(f"{'Deviazione Standard:':<30}{deviazione_standard:>8.2f} €")
   print(f"{'Prenotazioni sopra la media:':<30}{perc_prenotazioni_sopra_media:>8.1f} %")


   """
   Parte 4 – Pandas
   """

   # Creiamo un pool di clienti fittizi da cui pescare casualmente
   nomi_clienti = ["Alice Rossi", "Bob Bianchi", "Charlie Verdi", "Diana Bruno", "Enrico Povia", "Francesca Neri"]
   destinazioni_disponibili = ["Roma", "Bisceglie", "Genoa", "Taranto", "Bari", "Camogli", "Brindisi", "Padova", "Ginevra", "Viareggio"]

   # Definiamo un intervallo di tempo reale per le partenze
   data_inizio = datetime(2026,6,1)
   data_fine = datetime(2026,9,30)
   giorni_totali = (data_fine - data_inizio).days


   # Prepariamo delle liste vuote per raccogliere i dati delle 100 righe
   lista_clienti = []
   lista_destinazioni = []
   lista_date_partenza = []
   lista_durate = []
   lista_incassi = []

   # Usiamo un generatore random per diversificare i dati
   rng = np.random.default_rng(seed=42)

   for i in range(100):
      # Generiamo dati casuali per la riga corrente
      nome_scelto = random.choice(nomi_clienti)
      dest_scelta = random.choice(destinazioni_disponibili)
      eta_casuale = int(rng.integers(18, 75))
      vip_casuale = random.choice([True, False])
      saldo_casuale = round(float(rng.uniform(500, 5000)), 2)

      durata_casuale = int(rng.integers(2, 15)) # durata tra 2 e 14 giorni

      # Generiamo una data casuale nell'intervallo stabilito
      giorni_da_aggiungere = int(rng.integers(0, giorni_totali + 1))
      data_casuale = data_inizio + timedelta(days=giorni_da_aggiungere)
      #prezzo_scelto = random.choice(prezzi_casuali)

      # Istanziamo gli oggetti
      cliente_obj = Cliente(nome_scelto, eta_casuale, vip_casuale, saldo_casuale)
      viaggio_obj = Viaggio(dest_scelta, prezzi_casuali[i], durata_casuale)
      prenotazione = Prenotazioni(cliente_obj, viaggio_obj)
      prenotazione.set_sconto_vip() #se è vip applico lo sconto del 10%
   
      lista_clienti.append(cliente_obj.nome)
      lista_destinazioni.append(viaggio_obj.destinazione)
      # Salviamo la data formattata come stringa pulita (GG-MM-AAAA)
      lista_date_partenza.append(data_casuale.strftime("%d-%m-%Y"))
      lista_durate.append(f"{viaggio_obj.durata_giorni} giorni")
      lista_incassi.append(round(viaggio_obj.prezzo,2))

   # Creiamo il DataFrame inserendo direttamente le liste popolate
   df_travels = pd.DataFrame({
      "Cliente": lista_clienti,
      "Destinazione": lista_destinazioni,
      "Prezzo_Originario": prezzi_casuali, # Il prezzo prima dello sconto
      "Giorno_Partenza": lista_date_partenza,
      "Durata": lista_durate,
      "Incasso_Effettivo": lista_incassi   # Il prezzo potenzialmente scontato del 10%
   })

   print("\n--- DATAFRAME TRAVELS (PRIME 10 RIGHE) ---")
   print(df_travels.head(10))

   # Calcola con Pandas:incasso totale dell’agenzia,incasso medio per destinazione,top 3 destinazioni più vendute.

   print("\n" + "="*40)
   print("RELAZIONE AGENZIA CON PANDAS")
   print("="*40)

   # 1. incasso totale agenzia 
   incasso_totale = df_travels["Incasso_Effettivo"].sum()
   print(f"Incasso Totale Agenzia: {incasso_totale:,.2f} €")

   # 2. incasso medio del destinazione 
   # Raggruppiamo per destinazione e calcoliamo la media della colonna Incasso_Effettivo
   incasso_medio_dest = df_travels.groupby("Destinazione")["Incasso_Effettivo"].mean()
   print("\n--- Incasso Medio per Destinazione ---")
   print(incasso_medio_dest.map("{:.2f} €".format))

   # 3. Top 3 destinazioni più vendute (in base al numero di prenotazioni)
   # value_counts() conta quante volte appare ogni destinazione, head(3) prende le prime 3
   top_3_destinazioni = df_travels["Destinazione"].value_counts().head(3)
   print("\n--- Top 3 Destinazioni più vendute (numero di biglietti) ---")
   for i, (dest, count) in enumerate(top_3_destinazioni.items(),1):
      print(f"{i}. {dest:<15} ({count} prenotazioni)")

   
   """
   Parte 5 – Matplotlib

   Crea un grafico a barre che mostri l’incasso per ogni destinazione.
   Crea un grafico a linee che mostri l’andamento giornaliero degli incassi.
   Crea un grafico a torta che mostri la percentuale di vendite per ciascuna destinazione.
   """

   # dati grafico a barre incasso per ogni destinazione
   incasso_per_destinazione = df_travels.groupby("Destinazione")["Incasso_Effettivo"].sum().sort_values(ascending=False)

   # dati per il grafico a linee (andamento giornaliero degli incassi)
   df_travels['Data_Drop'] = pd.to_datetime(df_travels['Giorno_Partenza'], format='%d-%m-%Y')
   andamento_giornaliero = df_travels.groupby('Data_Drop')["Incasso_Effettivo"].sum().sort_index()

   # dati per il grafico a torta (Percentuale di biglietti/vendite per destinazione)
   conteggio_vendite = df_travels["Destinazione"].value_counts()


   # --- 1. GRAFICO A BARRE ---
   plt.figure(figsize=(10, 5))
   plt.bar(incasso_per_destinazione.index.to_numpy(), incasso_per_destinazione.values, color='skyblue', edgecolor='black')
   plt.title("Incasso totale per ogni destinazione", fontsize=14, fontweight='bold')
   plt.xlabel("Destinazione", fontsize=12)
   plt.ylabel("Incasso Totale (€)", fontsize=12)
   plt.xticks(rotation=45) # ruota delle città per non farli sovrapporre
   plt.grid(axis='y', linestyle='--', alpha=0.7)
   plt.tight_layout() # ottimizza gli spazi 
   plt.show()

   # --- 2. GRAFICO A LINEE ---
   plt.figure(figsize=(12, 5))
   plt.plot(andamento_giornaliero.index, andamento_giornaliero.values, color='orange', marker='o', linestyle='-', linewidth=2)
   plt.title("Andamento giornaliero degli incassi (Estate 2026)", fontsize=14, fontweight='bold')
   plt.xlabel("Data di partenza", fontsize=12)
   plt.ylabel("Incasso giornaliero (€)", fontsize=12)
   plt.grid(True, linestyle=':', alpha=0.6)
   plt.xticks(rotation=45)
   plt.tight_layout()
   plt.show()

   # --- 3- GRAFICO A TORTA ---
   plt.figure(figsize=(8, 8))
   # autopct='%1.1f%%' calcola e mostra automaticamente le percentuali sul grafico
   plt.pie(conteggio_vendite.values, labels=conteggio_vendite.index, autopct='%1.1f%%',
          startangle=140, colors=plt.cm.Paired.colors, wedgeprops={'edgecolor': 'white'})
   plt.title("Percentuale di vendite (Biglietti) per ciascuna destinazione", fontsize=14, fontweight='bold')
   plt.tight_layout()
   plt.show()



   """
   Parte 6 – Analisi Avanzata

   Raggruppa i viaggi in categorie:

   "Europa", "Asia", "America", "Africa".(Puoi usare un dizionario che associa ogni destinazione a una categoria).

   Calcola con Pandas:incasso totale per categoria,durata media dei viaggi per categoria.
   Salva il DataFrame aggiornato in un CSV chiamato prenotazioni_analizzate.csv.
   """
   # Definiamo il dizionario geografico per mappare le destinazioni esistenti
   mappa_categorie = {
      "Roma": "Europa",
      "Bisceglie":"Europa",
      "Genoa":"Europa",
      "Taranto": "Europa",
      "Bari":"Europa",
      "Camogli":"Europa",
      "Brindisi": "Europa",
      "Padova":"Europa",
      "Ginevra":"Europa",
      "Viareggio":"Europa"
   }

   # Creiamo dinamicamente la nuova colonna 'Categoria' usando il dizionario
   df_travels['Categoria'] = df_travels['Destinazione'].map(mappa_categorie)

   # Pulizia del dato 'Durata' per il calcolo della media
   df_travels['Durata_Numerica'] = df_travels['Durata'].str.replace(' giorni','').astype(int)

   analisi_categoria = df_travels.groupby('Categoria').agg(
      incasso_totale=('Incasso_Effettivo','sum'),
      durata_media_giorni=('Durata_Numerica','mean')
   ).round(2)

   print("\n" + "="*40)
   print("ANALISI AVANZATA PER CATEGORIA")
   print("="*40)
   print(analisi_categoria)

   # Pulizia finale del DataFrame prima del salvataggio 
   # rimuoviamo la colonna di supporto numerica per lasciare il file CSV pulito
   df_travels = df_travels.drop(columns=['Durata_Numerica'])

   if 'Data_Drop' in df_travels.columns:
      df_travels = df_travels.drop(columns=['Data_Drop'])

   # Salvataggio in formato CSV
   # index=False evita di salvare la colonna dei numeri di riga (0, 1, 2, ...) nel file

   percorso_salvataggio = Path(__file__).resolve().parent /"prenotazioni_analizzate.csv"
   df_travels.to_csv(percorso_salvataggio, index=False, encoding="utf-8")
   print(f"\n[INFO] Il DataFrame aggiornato è stato salvato con successo in {percorso_salvataggio}")

   """
   Parte 7 – Estensioni

   Crea una funzione che restituisce i N clienti con più prenotazioni.
   Realizza un grafico combinato (barre + linea) che mostri:barre = incasso medio per categoria,linea = durata media per categoria.
   """

   # --- 1 FUNZIONE PER I TOP N CLIENTI ---
   def get_top_clienti(dataframe: pd.DataFrame, n: int = 3) -> pd.DataFrame:
      """
      Restituisce un DataFrame con i primi N clienti per numero di prenotazioni effettuate
      """
      # Contiamo le prenotazioni per ogni cliente 
      conteggio_clienti = dataframe["Cliente"].value_counts().reset_index()
      conteggio_clienti.columns = ["Cliente", "Numero_Prenotazioni"]
      return conteggio_clienti.head(n)
   
   # --- TEST DELLA FUNZIONE ---
   print("\n" + "="*40)
   print("TEST FUNZIONE: TOP 3 CLIENTI CON PIÙ PRENOTAZIONI")
   print("="*40)
   top_3_clienti_test = get_top_clienti(df_travels, n=3)
   print(top_3_clienti_test.to_string(index=False))

   # --- PREPARAZIONE DATI PER IL GRAFICO COMBINATO ---
   if 'Durata_Numerica' not in df_travels.columns:
      df_travels['Durata_Numerica'] = df_travels['Durata'].str.replace(' giorni', '').astype(int)
   
   # calcoliamo le medie raggruppate per categoria
   medie_categoria = df_travels.groupby('Categoria').agg(
      incasso_medio=('Incasso_Effettivo','mean'),
      durata_media=('Durata_Numerica','mean')
   ).reset_index()

   # --- 3. REALIZZAZIONE GRAFICO COMBINATO (BARRE + LINEA) ---
   fig, ax1 = plt.subplots(figsize=(10, 6))

   # Grafico a Barre: Incasso Medio (Asse Y di sinistra)
   colore_barre = '#4A90E2' # Un blu moderno
   ax1.bar(medie_categoria['Categoria'].to_numpy(), medie_categoria['incasso_medio'].to_numpy(), 
           color=colore_barre, alpha=0.7, edgecolor='black', width=0.4, label='Incasso Medio (€)')
   
   # Configurazione del primo asse (Y1)
   ax1.set_xlabel('Categoria Geografica', fontsize=12, fontweight='bold')
   ax1.set_ylabel('Incasso Medio (€)', color=colore_barre, fontsize=12, fontweight='bold')
   ax1.tick_params(axis='y', labelcolor=colore_barre)
   ax1.grid(axis='y', linestyle='--', alpha=0.5)

   # Creazione del secondo asse Y (condivide lo stesso asse X)
   ax2 = ax1.twinx()

   # Grafico a Linea: Durata Media (Asse Y di destra)
   colore_linea = '#E24A4A' # Un rosso/arancio vivace
   ax2.plot(medie_categoria['Categoria'].to_numpy(), medie_categoria['durata_media'].to_numpy(), 
            color=colore_linea, marker='o', linewidth=3, markersize=8, label='Durata Media (Giorni)')
   
   # Configurazione del secondo asse (Y2)
   ax2.set_ylabel('Durata Media (Giorni)', color=colore_linea, fontsize=12, fontweight='bold')
   ax2.tick_params(axis='y', labelcolor=colore_linea)

   # Titolo e ottimizzazione
   plt.title('Analisi Combinata: Incasso Medio vs Durata Media per Categoria', fontsize=14, fontweight='bold', pad=15)
   
   # Uniamo le legende di entrambi gli assi in un'unica scatola
   linee, etichette = ax1.get_legend_handles_labels()
   linee2, etichette2 = ax2.get_legend_handles_labels()
   ax1.legend(linee + linee2, etichette + etichette2, loc='upper left')

   plt.tight_layout()
   plt.show()