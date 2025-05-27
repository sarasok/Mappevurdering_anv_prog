# Her har vi laget en kode som legger inn tilfeldige feil i CSV-filen 'R_Sammenslaaing_uten_feil.csv'.
#Dette er filen vi skal rense senere i denne oppgaven. Rensingen er laget i filen 'rense_data.ipynb'
# Den legger inn eksempelvis negative nedbør-, fuktighet-, lufttrykk- og skydekke-verdier
# Den fjerner også tilfeldige verdier fullstendig, eks t


# Importerer nødvendige biblioteker
import pandas as pd       # For å lese og skrive CSV-filer
import random             # For å generere tilfeldige tall og valg
import os                 # For å håndtere filstier

# Funksjon som legger inn forskjellige typer "feil" i et CSV-datasett
def lager_feil():
    # Finner sti til datafilen relativt til denne filen (bruker __file__)
    base_dir = os.path.dirname(__file__)
    filnavn = os.path.join(base_dir, "../data/R_Sammenslaaing_gjsnitt.csv")

    # Leser inn CSV-filen som en DataFrame
    df = pd.read_csv(filnavn)

    # Går gjennom datasettet i bolker på 10 rader
    for start in range(0, len(df), 10):
        # Velger en tilfeldig rad innenfor denne bolken
        i = random.randint(start, min(start + 9, len(df) - 1))

        # Velger en tilfeldig type feil å introdusere
        feiltype = random.choice(["negativ", "ekstrem_temp", "mangler", "duplikat_dato"])

        # Feiltype 1: Setter en negativ verdi i en målekolonne (selv om det egentlig ikke skal være negativt)
        if feiltype == "negativ":
            kol = random.choice(["Nedbør (mm)", "Relativ fuktighet (%)", "Skydekke (oktas)", "Lufttrykk (hPa)"])
            df.at[i, kol] = -abs(df.at[i, kol])  # Sørger for at verdien blir negativ

        # Feiltype 2: Setter inn ekstrem temperaturverdi langt utenfor normalen
        elif feiltype == "ekstrem_temp":
            ekstrem_verdi = random.uniform(-100, -60) if random.random() < 0.5 else random.uniform(60, 100)
            df.at[i, "Temperatur (°C)"] = round(ekstrem_verdi, 1)

        # Feiltype 3: Fjerner en verdi (gjør den til None = manglende data)
        elif feiltype == "mangler":
            kol = random.choice(["Temperatur (°C)", "Lufttrykk (hPa)", "Skydekke (oktas)", "Nedbør (mm)", "Relativ fuktighet (%)"])
            df.at[i, kol] = None

        # Feiltype 4: Legger inn en duplikat-rad med samme dato
        elif feiltype == "duplikat_dato":
            rad = df.iloc[i].copy()             # Kopierer en rad
            rad["Dato"] = "2023-12-18"          # Setter datoen til en fast verdi (gir dobbel oppføring)
            df = pd.concat([df.iloc[:i+1], pd.DataFrame([rad]), df.iloc[i+1:]], ignore_index=True)

    # Skriver det manipulerte datasettet tilbake til samme CSV-fil
    df.to_csv(filnavn, index=False, encoding="utf-8")

# Kjør funksjonen direkte dersom scriptet kjøres alene (ikke importert som modul)
if __name__ == "__main__":
    lager_feil()
