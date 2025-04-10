#gjennomsnitt, median og standardavvik (numpy, pandas)
#avdekke mønstre
#statistisk analyse for å finne sammenheng mellom to variabler i datasettet
#skjevheter under analyser, hvordan sikre at den er pålitelig
#visualisere

import pandas as pd
import numpy as np

class MiljoAnalyse:
    def __init__(self, "R_sammenslaaing_gjsnitt.csv"):
        self.df = pd.read_csv("R_sammenslaaing_gjsnitt.csv")

    def kolonner(self):
        return list(self.df.columns)

    def median(self, kol):
        return np.median(self.df[kol].dropna())

    def standardavvik(self, kol):
        return np.std(self.df[kol].dropna(), ddof=1)
    def
    
