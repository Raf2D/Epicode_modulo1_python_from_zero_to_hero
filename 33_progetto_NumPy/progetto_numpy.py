import numpy as np

# ================ PAZIENTE ======================================================================


class Paziente:

    def __init__(
        self,
        nome,
        cognome,
        codice_fiscale,
        eta,
        peso,
        analisi_effettuate,
        risultati_analisi,
    ):
        self.__nome = nome
        self.__cognome = cognome
        self.__codice_fiscale = codice_fiscale
        self.__eta = eta
        self.__peso = peso
        self.__analisi_effettuate = analisi_effettuate
        self.risultati_analisi = risultati_analisi # utilizzo il setter per la converisone in array numpy

    # --- NOME ---
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        if isinstance(nuovo_nome, str) and nuovo_nome.strip():
            self.__nome = nuovo_nome
        else:
            raise ValueError("Il nome deve essere una stringa valida.")

    # --- COGNOME ---
    @property
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, nuovo_cognome):
        if isinstance(nuovo_cognome, str) and nuovo_cognome.strip():
            self.__cognome = nuovo_cognome
        else:
            raise ValueError("Il cognome deve essere una stringa valida.")

    # --- CODICE FISCALE ---
    @property
    def codice_fiscale(self):
        return self.__codice_fiscale

    @codice_fiscale.setter
    def codice_fiscale(self, nuovo_cf):
        if isinstance(nuovo_cf, str) and len(nuovo_cf) == 16:
            self.__codice_fiscale = nuovo_cf.upper()
        else:
            raise ValueError(
                "Codice fiscale non valido (deve essere di 16 caratteri)."
            )

    # --- ETÀ ---
    @property
    def eta(self):
        return self.__eta

    @eta.setter
    def eta(self, nuova_eta):
        if isinstance(nuova_eta, int) and nuova_eta >= 0:
            self.__eta = nuova_eta
        else:
            raise ValueError("L'età deve essere un numero intero positivo.")

    # --- PESO ---
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, nuovo_peso):
        if (isinstance(nuovo_peso, (int, float))) and nuovo_peso > 0:
            self.__peso = nuovo_peso
        else:
            raise ValueError("Il peso deve essere un numero maggiore di zero.")

    # --- ANALISI EFFETTUATE ---
    @property
    def analisi_effettuate(self):
        return self.__analisi_effettuate

    @analisi_effettuate.setter
    def analisi_effettuate(self, nuove_analisi):
        if isinstance(nuove_analisi, list):
            self.__analisi_effettuate = nuove_analisi
        else:
            raise ValueError(
                "Le analisi effettuate devono essere inserite in una lista."
            )

    # --- RISULTATI ANALISI (NumPy) ---
    @property
    def risultati_analisi(self):
        return self.__risultati_analisi

    @risultati_analisi.setter
    def risultati_analisi(self, nuovi_risultati):
        try:
            array_np = np.asarray(nuovi_risultati, dtype=float)
            self.__risultati_analisi = array_np
        except (ValueError, TypeError):
            raise ValueError(
                "I risultati delle analisi devono essere convertibili in un array numerico."
            )

    # --- METODO STATISTICHE ---
    def statistiche_analisi(self):
        """Calcola e restituisce le statistiche descrittive dei risultati delle analisi."""
        if self.risultati_analisi.size == 0:
            return None

        media = np.mean(self.__risultati_analisi)
        minimo = np.min(self.__risultati_analisi)
        massimo = np.max(self.__risultati_analisi)
        deviazione_standard = np.std(self.__risultati_analisi)

        return {
            "media": media,
            "minimo": minimo,
            "massimo": massimo,
            "deviazione_standard": deviazione_standard,
        }

    def scheda_personale(self):
        
        risultati_str = ", ".join([str(x) for x in self.risultati_analisi])
        return (
            f"DATI PAZIENTE:\n"
            f"Nome: {self.nome}\n"
            f"Cognome: {self.cognome}\n"
            f"Codice fiscale: {self.codice_fiscale}\n"
            f"Età: {self.eta}\n"
            f"Peso: {self.peso} kg\n"
            f"Analisi effettuate: {', '.join(self.analisi_effettuate)}\n"
            f"Risultati analisi: [{risultati_str}]\n"
        )


# ================ MEDICO =========================================================================


class Medico:

    def __init__(self, nome, cognome, specializzazione):
        self.__nome = nome
        self.__cognome = cognome
        self.__specializzazione = specializzazione

    # --- NOME ---
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        if isinstance(nuovo_nome, str) and nuovo_nome.strip():
            self.__nome = nuovo_nome
        else:
            raise ValueError("Il nome del medico deve essere una stringa valida.")

    # --- COGNOME ---
    @property
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, nuovo_cognome):
        if isinstance(nuovo_cognome, str) and nuovo_cognome.strip():
            self.__cognome = nuovo_cognome
        else:
            raise ValueError(
                "Il cognome del medico deve essere una stringa valida."
            )

    # --- SPECIALIZZAZIONE ---
    @property
    def specializzazione(self):
        return self.__specializzazione

    @specializzazione.setter
    def specializzazione(self, nuova_spec):
        if isinstance(nuova_spec, str) and nuova_spec.strip():
            self.__specializzazione = nuova_spec
        else:
            raise ValueError("La specializzazione deve essere una stringa valida.")

    # --- METODO VISITA PAZIENTE ---
    def visita_paziente(self, paziente):
        print(
            f"Il Dott. {self.cognome} ({self.specializzazione}) sta visitando il paziente {paziente.nome} {paziente.cognome}."
        )


# ================ ANALISI =========================================================================


class Analisi:

    __VALORI_RIFERIMENTO = {
        "Glicemia": (70, 100),
        "Colesterolo Totale": (130, 200),
        "Trigliceridi": (50, 150),
        "Azotemia": (10, 50),
    }

    @classmethod
    def ottieni_range(cls, tipo_esame):
        return cls.__VALORI_RIFERIMENTO.get(tipo_esame.title(), None)

    def __init__(self, tipo, risultato):
        self.__tipo = tipo
        self.__risultato = risultato

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuovo_tipo):
        if (isinstance(nuovo_tipo, str)) and nuovo_tipo.strip():
            self.__tipo = nuovo_tipo
        else:
            raise ValueError("Il tipo di analisi deve essere una stringa valida!")

    @property
    def risultato(self):
        return self.__risultato

    @risultato.setter
    def risultato(self, nuovo_risultato):
        if isinstance(nuovo_risultato, (int, float)) and nuovo_risultato >= 0:
            self.__risultato = nuovo_risultato
        else:
            raise ValueError(
                "Il risultato deve essere un numero maggiore o uguale a zero!"
            )

    # --- METODO VALUTA ---
    def valuta(self):

        tipo_corretto = self.tipo.title()
        if tipo_corretto in self.__VALORI_RIFERIMENTO:
            limite_min, limite_max = self.__VALORI_RIFERIMENTO[tipo_corretto]

            if limite_min <= self.__risultato <= limite_max:
                return f"Risultato nella norma (Range ideale per {tipo_corretto}: {limite_min}-{limite_max})"
            elif self.__risultato < limite_min:
                return f"Valore BASSO (Rilevato: {self.__risultato}, Minimo atteso: {limite_min})"
            elif self.__risultato > limite_max:
                return f"Valore ALTO (Rilevato: {self.__risultato}, Massimo atteso: {limite_max})"
        else:
            return f"Analisi '{self.tipo}' non riconosciuta nei parametri di routine. Impossibile valutare automaticamente."

    def __str__(self):
        return f"{self.tipo}: {self.risultato}"


# =================================================================================================
# ====================================== MAIN =====================================================
# =================================================================================================

if __name__ == "__main__":
    print("=== AVVIO SISTEMA GESTIONALE CLINICA ===\n")

    # 1. Creazione di almeno 3 Medici
    medici = [
        Medico("Alessandro", "Borghi", "Cardiologia"),
        Medico("Elena", "Sofia", "Endocrinologia"),
        Medico("Francesco", "Totti", "Medicina dello Sport"),
    ]

    # 2. Creazione di almeno 5 Pazienti (Ognuno con almeno 3 analisi e relativi valori numerici)
    pazienti = [
        Paziente(
            "Enrico",
            "Ferrero",
            "FRRNRC03A01H501U",
            23,
            78.5,
            ["glicemia", "colesterolo totale", "azotemia"],
            [95.0, 185.0, 32.0],
        ),
        Paziente(
            "Mario",
            "Rossi",
            "RSSMRA81A01H501W",
            45,
            80.0,
            ["glicemia", "colesterolo totale", "trigliceridi"],
            [112.0, 215.0, 160.0],
        ),
        Paziente(
            "Daniele",
            "Sasso",
            "SSSDNL92A01H501Z",
            34,
            105.5,
            ["glicemia", "trigliceridi", "azotemia"],
            [88.0, 142.0, 41.0],
        ),
        Paziente(
            "Giulia",
            "Verdi",
            "VRDGLI95A41H501X",
            31,
            62.0,
            ["glicemia", "colesterolo totale", "trigliceridi"],
            [74.0, 135.0, 55.0],
        ),
        Paziente(
            "Laura",
            "Bianchi",
            "BNCHLR88A41H501Y",
            38,
            54.2,
            ["glicemia", "colesterolo totale", "azotemia"],
            [99.0, 198.0, 18.0],
        ),
    ]

    # 3. Stampa delle schede di ogni paziente e delle loro statistiche NumPy
    print("--- SCHEDE PAZIENTI E STATISTICHE ANALISI ---")
    for p in pazienti:
        print(p.scheda_personale())

        # Calcolo delle statistiche tramite il metodo NumPy interno alla classe
        stats = p.statistiche_analisi()
        if stats:
            print("STATISTICHE CLINICHE VETTORIALI (NumPy):")
            print(f"  > Media valori:       {stats['media']:.2f}")
            print(f"  > Valore Minimo:      {stats['minimo']:.2f}")
            print(f"  > Valore Massimo:     {stats['massimo']:.2f}")
            print(f"  > Deviazione Standard: {stats['deviazione_standard']:.2f}")
        else:
            print("Nessun dato numerico disponibile per le statistiche.")

        print("-" * 50)

    print("\n--- ASSEGNAZIONE VISITE MEDICHE ---")
    # 4. Mostra quale medico visita quale paziente (simulazione incrociata)
    # Medico 0 visita Paziente 0 e 1
    medici[0].visita_paziente(pazienti[0])
    medici[0].visita_paziente(pazienti[1])

    # Medico 1 visita Paziente 2 e 3
    medici[1].visita_paziente(pazienti[2])
    medici[1].visita_paziente(pazienti[3])

    # Medico 2 visita Paziente 4
    medici[2].visita_paziente(pazienti[4])

    print("\n=======================================================")