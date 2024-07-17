def eingabenamen():
    # Initialisierung der Variable für den Namen
    ws_name = " " * 5

    # Benutzer zur Eingabe des Namens auffordern
    print("Bitte geben Sie Ihren Namen an:")
    
    # Namen vom Benutzer akzeptieren
    ws_name = input()[:5]  # maximal 5 Zeichen übernehmen

    # Begrüßung mit dem Namen anzeigen
    print(f"Hallo {ws_name}")

# Hauptprogramm ausführen
if __name__ == "__main__":
    eingabenamen()

