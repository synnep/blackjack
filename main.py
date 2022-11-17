# Importerer klasser fra andre lokale filer:
import hånd_spiller_dealer
import kort_og_kortstokk

# Definerer noen funksjoner for brukervennlighet og funksjonalitet
def leggTilSpillere():
    print("Hei")
    antall = int(input("Hvor mange spillere ønsker du å legge til?: "))

    for i in range(antall):
        navn = input(f"Navnet til spiller {i+1}: ")
        # kanskje startpenger som input også?

        # LEGGER TIL OBJEKTET


# Lager litt kode som vil kjøres på begynnelsen av programmet
leggTilSpillere()

"""
while True:
   her kommer det valg:

   "s" for å starte neste runde
   "l" for å fjerne eller legge til spillere

    .. med muligheter for flere valg etterhvert
"""
