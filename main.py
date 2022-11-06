from walidacja import waliduj_liste
from losowy_zbior import stworz_listy

UDZIAL_TRENINGU = 90 # %

def main():
    with open('list.txt', 'r', encoding='utf8') as f_input:
        czy_poprawna = waliduj_liste(f_input)
        if not czy_poprawna:
            return 'Lista niepoprawna'
        stworz_listy(UDZIAL_TRENINGU, "list.txt")
        return 'Listy stworzone'

print(main())