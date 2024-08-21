def media_mobile(lista_numeri, n):
    medie_mobili = []
    somma_parziale = 0
    
    #Grazie ad enumerate posso ottenere direttamente l'indice i e il valore corrente numero dalla lista
    for i, numero in enumerate(lista_numeri):
        # Aggiungo il nuovo elemento alla somma parziale
        somma_parziale += numero
        
        # Se ho raggiunto almeno 'n' elementi, sottraggo l'elemento che esce dalla finestra
        if i >= n:
            somma_parziale -= lista_numeri[i - n]
        
        # Calcolo la media mobile e la aggiungo alla lista
        medie_mobili.append(somma_parziale / min(i + 1, n))
        #print(min(i + 1, n))
    
    return medie_mobili

# Definisco la lista di numeri e la passo alla funzione media_mobile per eseguire il calcolo
lista_numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

# Stampo il risultato
print(media_mobile(lista_numeri, n))
