# gjennomsnitt, median og standardavvik (numpy, pandas)
# avdekke mønstre
# statistisk analyse for å finne sammenheng mellom to variabler i datasettet
# skjevheter under analyser, hvordan sikre at den er pålitelig
# visualisere

import pandas as pd  # Pandas brukes for å lese, gruppere og analysere datasett

class MiljoPerMnd:
    def __init__(self, filnavn):
        # Leser inn CSV-fil med miljødata
        self.df = pd.read_csv(filnavn)

        # Stripper mellomrom fra kolonnenavn for å unngå feiltolkning (f.eks. ' Temperatur' → 'Temperatur')
        self.df.columns = self.df.columns.str.strip()

        # Konverterer 'Dato'-kolonnen til datetime-format for å kunne trekke ut tid
        self.df["Dato"] = pd.to_datetime(self.df["Dato"], format="%Y-%m-%d", errors="coerce")

        # Trekker ut år og måned – dette gir mulighet til å gruppere dataene månedlig
        self.df["År"] = self.df["Dato"].dt.year
        self.df["Måned"] = self.df["Dato"].dt.month

        # Kolonner som skal analyseres statistisk
        self.kolonner = [
            "Temperatur (°C)",
            "Lufttrykk (hPa)",
            "Nedbør (mm)",
            "Relativ fuktighet (%)",
            "Skydekke (oktas)"
        ]

    def gjennomsnitt_per_mnd(self):
        # Beregner gjennomsnitt (mean) for hver kolonne per måned
        # Dette kan brukes til å se overordnede mønstre og trender i været
        return self.df.groupby(["År", "Måned"])[self.kolonner].mean().round(2)

    def median_per_mnd(self):
        # Beregner median (midtverdien) per måned
        # Median er mer robust enn gjennomsnitt ved skjevheter eller uteliggere
        return self.df.groupby(["År", "Måned"])[self.kolonner].median().round(2)

    def standardavvik_per_mnd(self):
        # Beregner standardavvik per måned (mål på spredning i data)
        # Dette hjelper med å oppdage ustabilitet eller store variasjoner i målinger
        return self.df.groupby(["År", "Måned"])[self.kolonner].std(ddof=1).round(2)
