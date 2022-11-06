from pathlib import Path

def waliduj_liste(plik) -> None:
    is_valid = True
    for i in plik:
        wav, *_ = i.strip().split('|')
        sciezka_do_pliku = Path(wav)
        if not sciezka_do_pliku.exists():
            print(f'ERROR: Plik {sciezka_do_pliku} nie istnieje')
            is_valid = False
    return is_valid