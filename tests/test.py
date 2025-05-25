import unittest
import pandas as pd
import numpy as np
import tempfile
import os
import sys

# Legg til src-mappa i søkestien
sti_til_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(sti_til_src)

from opg5 import VærDataPlotter #Henter klassen VærDataPlotter fra opg5 som er hentet inn via src path
from opg4 import MiljoPerMnd #Henter klassen MiljoPerMnd fra opg4 som er hentet inn via src path
from opg6_databehandling import Databehandling #Henter klassen Databehandling fra opg6_databehandling som er hentet inn via src path

# Tester funksjonalitet i klassen VærDataPlotter fra opg5.py
class TestVærDataPlotter(unittest.TestCase):

    def setUp(self):  # ikke en test, men gjør at hver test i TestVærDataPlotter får et  nytt datasett å jobbe med, så testene ikke påvirker hverandre
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

    def tearDown(self): #ikke en test, men Kjøres etter hver enkelt testmetode – uansett om testen passerte eller feilet. For å rydde opp.
        os.remove(self.testfile.name)

    def test_data_lasting(self):
        self.assertEqual(len(self.plotter.df), 10)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.plotter.df["Dato"]))

    def test_kolonner_tilgjengelige(self):
        forventede = [
            "Dato", "Temperatur (°C)", "Lufttrykk (hPa)",
            "Nedbør (mm)", "Relativ fuktighet (%)", "Skydekke (oktas)"
        ]
        for kol in forventede:
            self.assertIn(kol, self.plotter.df.columns)

    def test_glidende_gjennomsnitt_beregning(self):
        self.plotter.df['Nedbør SMA'] = self.plotter.df['Nedbør (mm)'].rolling(window=7).mean()
        self.plotter.df['Skydekke SMA'] = self.plotter.df['Skydekke (oktas)'].rolling(window=7).mean()
        self.assertIn("Nedbør SMA", self.plotter.df.columns)
        self.assertIn("Skydekke SMA", self.plotter.df.columns)
        self.assertEqual(len(self.plotter.df["Nedbør SMA"]), 10)


# Tester klassen MiljoPerMnd fra opg4.py
class TestMiljoPerMnd(unittest.TestCase):

    def setUp(self):
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
        os.remove(self.testfile.name)

    def test_gjennomsnitt(self):
        result = self.analyse.gjennomsnitt_per_mnd()
        self.assertFalse(result.empty)
        self.assertIn("Temperatur (°C)", result.columns)

    def test_median(self):
        result = self.analyse.median_per_mnd()
        self.assertFalse(result.empty)
        self.assertIn("Lufttrykk (hPa)", result.columns)

    def test_standardavvik(self):
        result = self.analyse.standardavvik_per_mnd()
        self.assertFalse(result.empty)
        self.assertIn("Nedbør (mm)", result.columns)


# Tester oppgave 6 – klassen Databehandling
class TestDatabehandling(unittest.TestCase):

    def setUp(self):
        datoer = pd.date_range(start="2024-01-01", periods=10, freq="D")
        self.df = pd.DataFrame({
            "date": datoer,
            "temp": [1, 2, np.nan, 4, 5, 6, 7, np.nan, 9, 100]  # 100 er outlier
        })

        self.df_luft = pd.DataFrame({
            "date": datoer.delete([2, 4]),
            "luft": [10, 12, 14, 15, 17, 19, 21, 22]
        })

    def test_resample_og_interpoler(self):
        df_incomplete = self.df.copy()
        df_incomplete.rename(columns={"date": "Dato"}, inplace=True)
        daily, interpolert = Databehandling.resample_og_interpoler(df_incomplete)
        self.assertEqual(len(daily), 10)
        self.assertFalse(interpolert["temp"].isna().any())

    def test_sjekk_manglende_data(self):
        result = Databehandling.sjekk_manglende_data(self.df, self.df_luft)
        self.assertEqual(result["len_df"], 10)
        self.assertGreater(result["missing_df"].sum(), 0)
        self.assertLess(result["len_df_luft"], 10)

    def test_fjern_iqr_outliers(self):
        ny_serie = Databehandling.fjern_iqr_outliers(self.df["temp"].dropna())
        self.assertTrue(100 not in ny_serie.values)
        self.assertLess(len(ny_serie), len(self.df.dropna()))

    def test_finn_manglende_datoer(self):
        mangler_i_luft, mangler_i_df = Databehandling.finn_manglende_datoer(self.df, self.df_luft)
        self.assertIn(pd.Timestamp("2024-01-03"), mangler_i_luft)
        self.assertIn(pd.Timestamp("2024-01-02"), mangler_i_df)

    def test_fjern_outliers(self):
        df_renset = Databehandling.fjern_outliers(self.df, "temp", øvre_grense=50)
        self.assertTrue((df_renset["temp"] <= 50).all())
        self.assertNotIn(100, df_renset["temp"].values)

    def test_slå_sammen_data(self):
        df_sammenslått = Databehandling.slå_sammen_data(self.df, self.df_luft)
        self.assertIn("temp", df_sammenslått.columns)
        self.assertIn("luft", df_sammenslått.columns)
        self.assertLessEqual(len(df_sammenslått), len(self.df_luft))

    def test_tilbakestill_indeks(self):
        df_indexed = self.df.set_index("date")
        df_reset = Databehandling.tilbakestill_indeks(df_indexed)
        self.assertIn("date", df_reset.columns)
        self.assertFalse(df_reset.index.name == "date")


# testklassene blir registrert før kjøring
if __name__ == "__main__":
    unittest.main()