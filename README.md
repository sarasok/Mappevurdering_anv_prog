- 

# Prosjekttittel 
Kort prosjektbeskrivelse. 
## Innhold - Datainnsamling - Datavask og analyse - Simulering av fremtidig værdata 
## Installasjon 
1. Klon repoet 
2. Opprett virtuell miljø 
3. Installer avhengigheter(requirements.txt) 
## Bruk 
Hvordan kjøre koden. 
## Testing 
Hvordan kjøre tester. 


# Analyse av vær- og miljødata

Et tverrfaglig datavitenskapelig prosjekt som kombinerer innhenting, rensing, visualisering og prediksjon av vær- og luftkvalitetsdata. Prosjektet er utviklet med mål om å forstå sammenhenger mellom ulike miljøparametere og gi et grunnlag for å vurdere for eksempel luftforhold og behov for å ta med paraply.

---

## Innhold

### Datainnsamling

Vi hentet inn data fra to ulike API-kilder:

* **Frost.met**: Data om temperatur, lufttrykk, nedbør, skydekke og relativ fuktighet 
* **OpenWeatherMap**: Data om luftkvalitet (NO₂)

Dataene ble lagret i egne CSV-filer og behandlet i notebooken [`kode_som_henter_API.ipynb`](./notebook_mappe1/kode_som_henter_API.ipynb).

Alle værfilene ble  sammenslått i notebooken [`sammenslaaing_gjsnitt.ipynb`](./notebook_mappe1/sammenslaaing_gjsnitt.ipynb), og resultatet ble lagret som [`R_Sammenslaaing_gjsnitt.csv`](./data/R_Sammenslaaing_gjsnitt.csv).

For å kunne teste datarensing ble det laget en kode som manuelt og tilfeldig la inn feil i denne filen, som ble renset og oppdatert til [`R_Sammenslaaing_uten_feil.csv`](./data/R_Sammenslaaing_uten_feil.csv), som er det rene datasettet brukt videre i analysen.

---

### Datavask og analyse

Notebook: [`rense_data.ipynb`](./notebook_mappe1/rense_data.ipynb)

#### Tiltak utført i rensingen:

* Manglende verdier ble fylt inn med lineær interpolasjon (gjennomsnitt av dagen før og etter)
* Urealistiske verdier (f.eks. temperatur < -50 °C eller > 50 °C) ble erstattet
* Negative verdier i fysiske målinger ble gjort positive med `abs()`
* Datokonsistens ble sikret: alle datoer konvertert til `datetime` og gjort sammenhengende

For statistisk analyse ble det opprettet en klasse `MiljoPerMnd` i [`opg4.py`](./src/opg4.py), som viser:

* `gjennomsnitt_per_mnd()`
* `median_per_mnd()`
* `standardavvik_per_mnd()`

Dette gir innsikt i værdataenes mønstre og variasjoner over tid.

---

### Visualisering

I [`opg5.py`](./src/opg5.py) definerte vi klassen `VærDataPlotter` som gjør det enkelt å visualisere ulike værvariabler.

Funksjonaliteten dekker:

* Statisk linjeplott for temperatur og lufttrykk
* Glidende gjennomsnitt av nedbør og skydekke
* Scatterplot med regresjonslinje for temperatur vs. fuktighet
* Heatmap for korrelasjon mellom alle numeriske kolonner
* Interaktive grafer med `plotly`, inkludert dropdown-meny og boblegraf

---

### Simulering og modellering

I Oppgave 6 har vi bygget en komplett pipeline for prediktiv analyse av skydekke.

#### Dataforberedelse (`opg6_databehandling.py`):

* Resampling og interpolasjon av luftdata
* Fjerning av outliers med IQR
* Slå sammen ulike datasett til ett rent analysedatasett

#### Modellering (`opg6_analyse.py` og `opg6_skydekkemodel.py`):

* Trener regresjonsmodell (scikit-learn) med 3 inputvariabler
* Evaluerer ytelse med MSE, RMSE og R²
* Lagrer modell og scaler som `.pkl`
* Praktisk funksjon: `bør_ta_med_paraply()` gir anbefaling basert på modellresultat

#### Visualisering (`opg6_visualisering.py`):

* Interpolering og glatting av variabler over tid
* Sammenligning av faktisk vs. predikert skydekke
* Korrelasjonsmatrise for hele datasettet

---

## Installasjon

1. **Klon prosjektet**

```bash
git clone <repo-url>
cd prosjektmappe
```

2. **Opprett virtuelt miljø (valgfritt, men anbefalt)**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Installer avhengigheter**

```bash
pip install -r requirements.txt
```

---

## Bruk

Kjør notebookene i rekkefølge for å gjenskape analysen:

1. `kode_som_henter_API.ipynb`
2. `sammenslaaing_gjsnitt.ipynb`
3. `rense_data.ipynb`
4. `del_2.ipynb`

Alternativt kan funksjoner og klasser importeres direkte fra `src/` i egne skript.

---

## Testing

### Enhetstester med `unittest`

Fil: [`test.py`](./tests/test.py)

Kjøres slik:

```bash
python -m unittest tests/test.py
```

Tester:

* `MiljoPerMnd` (statistiske analyser)
* `VærDataPlotter` (datainnhenting og SMA)
* `Databehandling` (interpolasjon, outliers, manglende datoer)

Totalt 13 tester, isolert med `setUp` og `tearDown`.

---

### Negativtester (manuelle)

Fil: [`negativ_test.py`](./tests/negativ_test.py)

Kjøres slik:

```bash
python tests/negativ_test.py
```

Tester hvordan koden håndterer:

* Manglende kolonner (opg4)
* Ikke-numeriske data (opg5)
* Feil input i beslutningsfunksjon (opg6)

Disse testene bruker `try/except` og `assert` for å fange forventede feil.

---

> Prosjektet er bygget opp med god mappeinndeling og struktur (data, src, notebooks, tests), og viser hvordan datavitenskap kan brukes i praksis for å trekke innsikt fra reelle værdata.
