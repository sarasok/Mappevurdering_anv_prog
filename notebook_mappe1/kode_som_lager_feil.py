# Her har vi laget en kode som legger inn tilfeldige feil i CSV-filen 'R_Sammenslaaing_uten_feil.csv'.
#Dette er filen vi skal rense senere i denne oppgaven. Rensingen er laget i filen 'rense_data.ipynb'
# Den legger inn eksempelvis negative nedbør-, fuktighet-, lufttrykk- og skydekke-verdier
# Den fjerner også tilfeldige verdier fullstendig, eks t

import pandas as pd
import random
import os

def lager_feil():
    base_dir = os.path.dirname(__file__)
    filnavn = os.path.join(base_dir, "../data/R_Sammenslaaing_gjsnitt.csv")

    df = pd.read_csv(filnavn)

    for start in range(0, len(df), 10):
        i = random.randint(start, min(start + 9, len(df) - 1))
        feiltype = random.choice(["negativ", "ekstrem_temp", "mangler", "duplikat_dato"])

        if feiltype == "negativ":
            kol = random.choice(["Nedbør (mm)", "Relativ fuktighet (%)", "Skydekke (oktas)", "Lufttrykk (hPa)"])
            df.at[i, kol] = -abs(df.at[i, kol])

        elif feiltype == "ekstrem_temp":
            ekstrem_verdi = random.uniform(-100, -60) if random.random() < 0.5 else random.uniform(60, 100)
            df.at[i, "Temperatur (°C)"] = round(ekstrem_verdi, 1)

        elif feiltype == "mangler":
            kol = random.choice(["Temperatur (°C)", "Lufttrykk (hPa)", "Skydekke (oktas)", "Nedbør (mm)", "Relativ fuktighet (%)"])
            df.at[i, kol] = None

        elif feiltype == "duplikat_dato":
            rad = df.iloc[i].copy()
            rad["Dato"] = "2023-12-18"
            df = pd.concat([df.iloc[:i+1], pd.DataFrame([rad]), df.iloc[i+1:]], ignore_index=True)

    df.to_csv(filnavn, index=False, encoding="utf-8")

#Kjør funksjonen direkte hvis scriptet kjøres alene
if __name__ == "__main__":
    lager_feil()
    