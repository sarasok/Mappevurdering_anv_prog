#gjennomsnitt, median og standardavvik (numpy, pandas)
#avdekke mønstre
#statistisk analyse for å finne sammenheng mellom to variabler i datasettet
#skjevheter under analyser, hvordan sikre at den er pålitelig
#visualisere

import pandas as pd
import numpy as np

class MiljoPerMnd:
    def __init__(self, filnavn):
        self.df = pd.read_csv(filnavn)

        # Sørg for at 'Dato' er datetime-objekt
        self.df["Dato"] = pd.to_datetime(self.df["Dato"], errors="coerce")

        # Legg til en månedskolonne for gruppering
        self.df["Måned"] = self.df["Dato"].dt.month

        # Kolonner vi skal analysere
        self.kolonner = [
            "Temperatur (°C)",
            "Lufttrykk (hPa)",
            "Nedbør (mm)",
            "Relativ fuktighet (%)",
            "Skydekke (oktas)"
        ]

    def gjennomsnitt_per_mnd(self):
        return self.df.groupby("Måned")[self.kolonner].mean().round(2)

    def median_per_mnd(self):
        return self.df.groupby("Måned")[self.kolonner].median().round(2)

    def standardavvik_per_mnd(self):
        return self.df.groupby("Måned")[self.kolonner].std(ddof=1).round(2)
