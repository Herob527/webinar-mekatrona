from random import sample

def stworz_listy(udzial_walidacji, plik_zrodlowy):
    with open(plik_zrodlowy, "r", encoding='utf8') as f_lista_wejscie:
        linie = f_lista_wejscie.readlines()

    ilosc_lini = len(linie)
    randomizowane = sample(linie, k=ilosc_lini)
    
    ilosc_lini_treningu = ilosc_lini // udzial_walidacji
    
    linie_treningowe = randomizowane[ilosc_lini_treningu:]
    linie_walidacji = randomizowane[:ilosc_lini_treningu]
    
    with open("list_train.txt", "w", encoding='utf8') as f_lista_treningowa, \
        open("list_val.txt", "w", encoding='utf8') as f_lista_walidacji:
    
        f_lista_treningowa.writelines(linie_treningowe)
        f_lista_walidacji.writelines(linie_walidacji)
            
        
        