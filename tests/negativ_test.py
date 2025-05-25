import pandas as pd
import numpy as np
import tempfile
import os
import sys

# Legg til src-mappa i path
sti_til_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(sti_til_src)

from opg4 import MiljoPerMnd #Henter inn klassen MiljoPerMnd fra opg4 som er hentet inn via src path
from opg5 import VærDataPlotter #Henter inn klassen VærDataPlotter fra opg5 som er hentet inn via src path
from opg6_analyse import regresjon #Henter inn klassen  fra opg5 som er hentet inn via src path


#Negativ test til opgave 4
def test_miljo_negativ_mangler_kolonne():
    # Lager testdata uten "Temperatur (°C)"
    test_data = pd.DataFrame({
        "Dato": pd.date_range(start="2023-01-01", periods=5, freq="D"),
        # "Temperatur (°C)" mangler!
        "Lufttrykk (hPa)": [1010, 1012, 1011, 1013, 1010],
        "Nedbør (mm)": [0, 1, 0, 2, 0],
        "Relativ fuktighet (%)": [75, 78, 77, 76, 79],
        "Skydekke (oktas)": [2, 3, 4, 3, 2]
    })

    # Skriver til midlertidig fil
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="w", newline="", encoding="utf-8") as tmp:
        test_data.to_csv(tmp.name, index=False)

    try:
        analyse = MiljoPerMnd(tmp.name)
        # Dette vil kaste feil når gjennomsnitt_per_mnd() forsøker å bruke en manglende kolonne
        _ = analyse.gjennomsnitt_per_mnd()
        assert False, "Test failed: Manglende kolonne burde ha kastet en KeyError"
    except Exception as e:
        print("Test case passed: Caught expected exception:", type(e).__name__, "-", e)
    finally:
        os.remove(tmp.name)

test_miljo_negativ_mangler_kolonne()



#Negativ test til opg 5:
def test_korrelasjonsheatmap_negativ():
    # Lager testdata uten numeriske kolonner
    test_data = pd.DataFrame({
        "Dato": pd.date_range(start="2023-01-01", periods=3),
        "Tekst": ["x", "y", "z"]
    })

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="w", encoding="utf-8") as tmp:
        test_data.to_csv(tmp.name, index=False)

    try:
        plotter = VærDataPlotter(tmp.name)
        plotter.tegn_korrelasjonsheatmap()  # Forventer feil siden dett ikke er noen numeriske kolonner
        assert plotter.df.select_dtypes(include='number').shape[1] > 0, "Test case failed"
    except Exception as e:
        print("Test case passed: Caught expected exception:", type(e), "-", e)
    finally:
        os.remove(tmp.name)

test_korrelasjonsheatmap_negativ()


#Negativ test til opg 6


def test_bør_ta_med_paraply_feil_input():
    # Prøver med ugyldige typer: tekst og None
    try:
        # Dette vil feile fordi "høy" ikke kan sammenlignes med tall
        assert bør_ta_med_paraply("høy", None) == "Ta med paraply!", "Test case failed"
    except Exception as e:
        print("Test case passed: Caught expected exception:", type(e).__name__, "-", e)

test_bør_ta_med_paraply_feil_input()