# Her har vi laget en kode som legger inn tilfeldige feil i CSV-filen 'R_Sammenslaaing_uten_feil.csv'.
#Dette er filen vi skal rense senere i denne oppgaven. Rensingen er laget i filen 'rense_data.ipynb'
# Den legger inn eksempelvis negative nedbør-, fuktighet-, lufttrykk- og skydekke-verdier
# Den fjerner også tilfeldige verdier fullstendig, eks t

import pandas as pd
import random

print('Programmet kjører')

# Henter CSV-filen
filnavn = "../data/R_Sammenslaaing_gjsnitt.csv"
df = pd.read_csv(filnavn)

# Legger inn én tilfeldig feil innenfor hver 10. rad
for start in range(0, len(df), 10):
    i = random.randint(start, min(start + 9, len(df) - 1))
    feiltype = random.choice(["negativ", "ekstrem_temp", "mangler", "duplikat_dato"])

    if feiltype == "negativ":
        kol = random.choice(["Nedbør (mm)", "Relativ fuktighet (%)", "Skydekke (oktas)", "Lufttrykk (hPa)"])
        df.at[i, kol] = -abs(df.at[i, kol])  # gjør verdien negativ

    elif feiltype == "ekstrem_temp":
        ekstrem_verdi = random.uniform(-100, -60) if random.random() < 0.5 else random.uniform(60, 100)
        df.at[i, "Temperatur (°C)"] = round(ekstrem_verdi, 1)


    elif feiltype == "mangler":
        kol = random.choice(["Temperatur (°C)", "Lufttrykk (hPa)", "Skydekke (oktas)", "Nedbør (mm)", "Relativ fuktighet (%)"])
        df.at[i, kol] = None  # setter cellen til tom (NaN)

    elif feiltype == "duplikat_dato":
        rad = df.iloc[i].copy()
        rad["Dato"] = "2023-12-18"  # gjentatt dato
        df = pd.concat([df.iloc[:i+1], pd.DataFrame([rad]), df.iloc[i+1:]], ignore_index=True)

# Lagrer de nye feilene i filen 'Sammenslaaing_gjsnitt.csv'
df.to_csv(filnavn, index=False, encoding="utf-8")

# Skriv dette i terminal enn så lenge for å kjøre: python kode_som_lager_feil.py