import unittest
import pandas as pd
import numpy as np
import tempfile
import os
import sys

# Legg til src-mappa i søkestien
sti_til_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(sti_til_src)

from opg5 import VærDataPlotter
from opg4 import MiljoPerMnd


# Tester funksjonalitet i klassen VærDataPlotter fra opg5.py
class TestVærDataPlotter(unittest.TestCase):

    def setUp(self):
        # Lager en liten test-datastruktur og skriver til en midlertidig CSV
        self.test_data = pd.DataFrame({
            "Dato": pd.date_range(start="2024-01-01", periods=10, freq="D"),
            "Temperatur (°C)": [1,2,3,4,5,6,7,8,9,10],
            "Lufttrykk (hPa)": [1010,1005,1007,1012,1011,1009,1013,1010,1008,1006],
            "Nedbør (mm)": [0,1,0,2,5,0,3,4,0,1],
            "Relativ fuktighet (%)": [80,82,85,78,76,79,81,83,84,77],
            "Skydekke (oktas)": [2,3,4,5,6,5,4,3,2,1]
        })
        self.testfile = tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="w", newline="", encoding="utf-8")
        self.test_data.to_csv(self.testfile.name, index=False)
        self.testfile.close()
        self.plotter = VærDataPlotter(self.testfile.name)

    def tearDown(self):
        # Sletter midlertidig fil etter hver test
        os.remove(self.testfile.name)

    def test_data_lasting(self):
        # Tester at dataene lastes korrekt og at Dato-kolonnen er konvertert til datetime
        self.assertEqual(len(self.plotter.df), 10)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.plotter.df["Dato"]))

    def test_kolonner_tilgjengelige(self):
        # Tester at alle forventede kolonner finnes i datasettet
        forventede = [
            "Dato", "Temperatur (°C)", "Lufttrykk (hPa)",
            "Nedbør (mm)", "Relativ fuktighet (%)", "Skydekke (oktas)"
        ]
        for kol in forventede:
            self.assertIn(kol, self.plotter.df.columns)

    def test_glidende_gjennomsnitt_beregning(self):
        # Tester at glidende gjennomsnitt kan beregnes og kolonnene blir lagt til
        self.plotter.df['Nedbør SMA'] = self.plotter.df['Nedbør (mm)'].rolling(window=7).mean()
        self.plotter.df['Skydekke SMA'] = self.plotter.df['Skydekke (oktas)'].rolling(window=7).mean()
        self.assertIn("Nedbør SMA", self.plotter.df.columns)
        self.assertIn("Skydekke SMA", self.plotter.df.columns)
        self.assertEqual(len(self.plotter.df["Nedbør SMA"]), 10)

# Tester klassen MiljoPerMnd fra opg4.py
class TestMiljoPerMnd(unittest.TestCase):

    def setUp(self):
        # Oppretter testdata og skriver til midlertidig CSV
        self.test_data = pd.DataFrame({
            "Dato": pd.date_range(start="2023-01-01", periods=60, freq="D"),
            "Temperatur (°C)": np.linspace(-5, 5, 60),
            "Lufttrykk (hPa)": np.random.uniform(980, 1030, 60),
            "Nedbør (mm)": np.random.randint(0, 10, 60),
            "Relativ fuktighet (%)": np.random.randint(60, 100, 60),
            "Skydekke (oktas)": np.random.randint(0, 9, 60)
        })
        self.testfile = tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="w", newline="", encoding="utf-8")
        self.test_data.to_csv(self.testfile.name, index=False)
        self.testfile.close()
        self.analyse = MiljoPerMnd(self.testfile.name)

    def tearDown(self):
        # Fjerner testfilen etter test
        os.remove(self.testfile.name)

    def test_gjennomsnitt(self):
        # Tester at gjennomsnitt_per_mnd gir resultater og inneholder riktig kolonne
        result = self.analyse.gjennomsnitt_per_mnd()
        self.assertFalse(result.empty)
        self.assertIn("Temperatur (°C)", result.columns)

    def test_median(self):
        # Tester at median_per_mnd gir resultater og inneholder riktig kolonne
        result = self.analyse.median_per_mnd()
        self.assertFalse(result.empty)
        self.assertIn("Lufttrykk (hPa)", result.columns)

    def test_standardavvik(self):
        # Tester at standardavvik_per_mnd gir resultater og inneholder riktig kolonne
        result = self.analyse.standardavvik_per_mnd()
        self.assertFalse(result.empty)
        self.assertIn("Nedbør (mm)", result.columns)

if __name__ == "__main__":
    unittest.main()
