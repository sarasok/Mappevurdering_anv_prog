import unittest
import pandas as pd
import tempfile
import os
import sys

# Legg til src-mappa i path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from opg4 import MiljoPerMnd
from opg5 import VærDataPlotter
from opg6_analyse import bør_ta_med_paraply

class TestNegativMiljoPerMnd(unittest.TestCase):
    def test_mangler_kolonne(self):
        df = pd.DataFrame({
            "Dato": pd.date_range(start="2023-01-01", periods=5),
            "Lufttrykk (hPa)": [1010, 1012, 1011, 1013, 1010],
        })
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            df.to_csv(tmp.name, index=False)
        with self.assertRaises(KeyError):
            analyse = MiljoPerMnd(tmp.name)
            analyse.gjennomsnitt_per_mnd()
        os.remove(tmp.name)

class TestNegativVærDataPlotter(unittest.TestCase):
    def test_uten_numeriske_kolonner(self):
        df = pd.DataFrame({
            "Dato": pd.date_range(start="2023-01-01", periods=3),
            "Tekst": ["a", "b", "c"]
        })
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            df.to_csv(tmp.name, index=False)
        plotter = VærDataPlotter(tmp.name)
        with self.assertRaises(ValueError):
            plotter.tegn_korrelasjonsheatmap()
        os.remove(tmp.name)

class TestNegativParaply(unittest.TestCase):
    def test_ugyldige_input(self):
        with self.assertRaises(TypeError):
            bør_ta_med_paraply("høy", None)

if __name__ == "__main__":
    unittest.main()

