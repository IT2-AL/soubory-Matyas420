import os 

def vytvoreni_slozky(nazev_slozky):
    try:
        os.makedirs(nazev_slozky, exist_ok=True)
        print(f"Složka '{nazev_slozky}' byla úspěšně vytvořena")
    except OSError as e:
        print(f"Nepodařilo se vytvořit složku: {e}")

vytvoreni_slozky("nova_složka")

def vytvoreni_souboru(nazev_slozky, obsah):
    try:
        with open(nazev_slozky, 'w', ) as soubor:
            soubor.write(obsah)
        print(f"Soubor '{nazev_slozky}' byl úspěšně vytvořen.")
    except OSError as e:
        print(f"Nepodařilo se vytvořit soubor: {e}")

nazev_slozky = os.path.join("nova_složka", "soubor.txt")
vytvoreni_souboru(nazev_slozky, "Toto je obsah souboru")