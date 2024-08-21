import re
from collections import defaultdict

def analizza_parole(testo):
    # Converto tutto il testo in minuscolo
    testo = testo.lower()
    
    # Utilizzo una regex per rimuovere tutta la punteggiatura
    testo = re.sub(r'[^\w\s]', '', testo)
    
    # Suddivido il testo in parole
    parole = testo.split()
    
    # Inizializzo un dizionario per tenere traccia delle occorrenze delle parole
    conteggio_parole = defaultdict(int)
    
    # Conta le occorrenze di ciascuna parola
    for parola in parole:
        conteggio_parole[parola] += 1
    
    return dict(conteggio_parole)


testo = "Ciao! Python e' un bel linguaggio di programmazione ma preferisco Java, non vedo l'ora di iniziare la parte di attacchi, exploit etc. Ciao Python."
print(analizza_parole(testo))

# Trova tutte le parole che iniziano con 'C'
pattern = re.compile(r'\bC\w+')
risultato = pattern.findall(testo)
print("Parole che iniziano con C: ")
print(risultato)

# Trova tutta la punteggiatura
pattern = re.compile(r'[^\w\s]')
risultato = pattern.findall(testo)
print("Punteggiatura : ")
print(risultato)

# Sostituisco 'Python' con 'C'
risultato = re.sub(r'Python', 'C', testo)
print("Il testo modificato e' : ")
print(risultato)