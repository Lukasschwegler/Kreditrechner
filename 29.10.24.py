kreditbetrag = int(input("Kreditbetrag "))

jahre = int(input("Laufzeit "))

zinssatz = float(input("Zinssatz in % "))

monatliche_rate = int(input("Monatlicherate "))

#sonder_tilgung = int(input("Sondertilgung "))

#Anuität
# Berechnen der Annuität
anu = monatliche_rate  * 12
#print(f"f string: Die Annuität beträgt : {anu:.2f} Euro")

# Zinsen gesamt 
#zinsen = 


kapital = kreditbetrag

for jahr in range(1, jahre + 1):
    zinsen = kapital/100 * zinssatz  # Berechnung der Zinsen für das Jahr
    tilgen = anu - zinsen 
    kapital -= tilgen                # Die Tilgung
    #kapital -= sonder_tilgung        # Die Sondertilgung
    print(f"Jahr {jahr}: Zinsen = {zinsen:.2f} EUR, Tilgung = {tilgen:.2f} EUR, Restschuld = {kapital:.2f} EUR")
   

def kreditrate_berechnen(kreditbetrag, zinssatz, jahre):
    # Zinssatz von Prozent in Dezimal umwandeln und monatlichen Zinssatz berechnen
    r = (zinssatz / 100) / 12
    # Anzahl der Monate berechnen
    n = jahre * 12
    # Annuitätenformel zur Berechnung der monatlichen Rate
    monatliche = (kreditbetrag * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return monatliche

#Anuitätenformel 
# Funktion aufrufen und Ergebnis ausgeben
monatliche = kreditrate_berechnen(kreditbetrag, zinssatz, jahre)
#print(f"Rate bei Volltilgung: {monatliche:.2f} Euro")

# Beispiel-Dictionary
# Färben des Dictionary
farbe = "\033[90m"  # Grau
reset = "\033[0m"  # Zurücksetzen der Farbe
mein_dict = {

    "Kreditbetrag": f"{farbe}Meine Kreditbetrag beträgt: {kreditbetrag:.2f}€{reset}",
    "Laufzeit": f"{farbe}Meine Laufzeit beträgt: {jahre:.2f} Jahre{reset}",
    "Monatsrate": f"{farbe}Meine Monatsrate beträgt: {monatliche_rate:.2f}€{reset}",
    "Rate bei Volltilgung": f"{farbe}Die Volltilgung beträgt: {monatliche:.2f}€{reset}",
    "Zinssatz": f"{farbe}Meine Zinssatz beträgt: {zinssatz:.2f} %{reset}",
   # "Die gesamten Zinsen": f"{farbe}Die gesamten Zinsen betragen: {zinsen:.2f}€{reset}",
    "Annuität": f"{farbe}Die Annuität beträgt: {anu:.2f}€{reset}",
   # "Sondertilgung im Jahr": f"{farbe}Die Sondertilgung beträgt: {sonder_tilgung:.2f}€{reset}",
   # "Sondertilgung gesamt": f"{farbe}Die gesamte Sondertilgung beträgt: {gesamt:.2f}€{reset}",4
   # "Gesamtkosten":
}

# Manuelle Formatierung
for key, value in mein_dict.items():
    print(f"{key}: {value}")








