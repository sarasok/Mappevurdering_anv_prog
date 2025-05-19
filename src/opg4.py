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
        self.df.columns = self.df.columns.str.strip()  # <–– denne linjen fjerner problemet!

        self.df["Dato"] = pd.to_datetime(self.df["Dato"], format="%Y-%m-%d", errors="coerce")
        self.df["År"] = self.df["Dato"].dt.year
        self.df["Måned"] = self.df["Dato"].dt.month

        self.kolonner = [
            "Temperatur (°C)",
            "Lufttrykk (hPa)",
            "Nedbør (mm)",
            "Relativ fuktighet (%)",
            "Skydekke (oktas)"
        ]

    def gjennomsnitt_per_mnd(self):
        return self.df.groupby(["År", "Måned"])[self.kolonner].mean().round(2)

    def median_per_mnd(self):
        return self.df.groupby(["År", "Måned"])[self.kolonner].median().round(2)

    def standardavvik_per_mnd(self):
        return self.df.groupby(["År", "Måned"])[self.kolonner].std(ddof=1).round(2)

