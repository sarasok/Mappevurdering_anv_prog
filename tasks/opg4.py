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

    # Lager gruppe for gjennomsnittlige verdier per måned
    def gjennomsnitt_per_mnd(self):
        return self.df.groupby(["År", "Måned"])[self.kolonner].mean().round(2)

    # Lager en gruppe for gjennomsnittlig median per måned
    def median_per_mnd(self):
        return self.df.groupby(["År", "Måned"])[self.kolonner].median().round(2)

    # Lager en gruppe for gjennomsnittlig standardavvik per måned
    def standardavvik_per_mnd(self):
        return self.df.groupby(["År", "Måned"])[self.kolonner].std(ddof=1).round(2)

