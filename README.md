
# Analyse av vær- og miljødata
I dette prosjektet har vi analysert vær- og miljødata i Trondheim i perioden 1. januar 2023 - 30. desember 2024. Vi har samlet inn og renset data, og deretter laget visualiseringer. Fra disse analysene ble det oppdaget sammenhenger og trender mellom de ulike miljøparametere. Videre la dette et grunnlag for å prediktere vær- og luftkvalitetsdata, for å kunne si noe om utviklingen i fremtiden.


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
* Negative verdier i fysiske målinger ble gjort positive med abs()
* Datokonsistens ble sikret: alle datoer konvertert til datetime og gjort sammenhengende

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
* Interaktive grafer med plotly, inkludert dropdown-meny og boblegraf

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
## Dokumentasjon
Fil | Beskrivelse
`README.md`: Hovedbeskrivelse av prosjektet, struktur, innhold og hvordan det kjøres. 
`Refleksjonsnotat.md`: Refleksjon over hva vi har lært, utfordringer vi møtte, og erfaring med verktøy og samarbeid. 
`data/data.md`: Informasjon om hvilke vær- og miljødata som er brukt, hvordan de er samlet inn og renset. 
`notebook_mappe1/del1.md`: Dokumentasjon av oppgave 2: datainnsamling fra Frost API og aggregering av målinger. 
`notebook_mappe2/del2.md`: Dokumentasjon av oppgave 6: prediktiv analyse med lineær regresjon, datarensing og visualiseringer. 
`src/src.md`: Beskrivelse av Python-koden i `src/`, inkludert klasser og funksjoner brukt i analyse og visualisering. 
`tests/tests.md`: Oversikt over teststrategien: både automatiske unittester og manuelle negative tester er inkludert. 

---
## Installasjon

1. **Klon repoet**

git clone <https://github.com/sarasok/Mappevurdering_anv_prog.git>

2. **Opprett virtuelt miljø**

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. **Installer avhengigheter**

pip install -r requirements.txt

---

## Bruk

Kjør filene i rekkefølge for å gjenskape analysen:

1. ['kode_som_henter_API.ipynb'](./notebook_mappe1/kode_som_henter_API.ipynb)
2. ['sammenslaaing_gjsnitt.ipynb'](./notebook_mappe1/sammenslaaing_gjsnitt.ipynb)
3. ['kode_som_lager_feil.py'](./notebook_mappe1/kode_som_lager_feil.py)
4. ['rense_data.ipynb'](./notebook_mappe1/rense_data.ipynb)
5. ['opg4.py'](./src/opg4.py)
6. ['opg5.py'](./src/opg5.py)
7. ['opg6_analyse.py'](./src/opg6_analyse.py)
8. ['opg6_databehandling.py'](./src/opg6_databehandling.py)
9. ['opg6_skydekkemodel.py'](./src/opg6_skydekkemodel.py)
10. ['opg6_visualisering.py'](./src/opg6_visualisering.py)
11. ['Opg_4_5.ipynb'](./notebook_mappe2/Opg_4_5.ipynb)
12. ['Opg6.ipynb'](./notebook_mappe2/Opg6.ipynb)

---

## Testing

### Enhetstester med `unittest`
,
Fil: [`test.py`](./tests/test.py)

Kjøres slik:
python -m unittest tests/test.py

Tester klassene:

* MiljoPerMnd
* VærDataPlotter
* Databehandling

Prosjektet har totalt 13 tester.

---

### Negativtester 
Fil: [`negativ_test.py`](./tests/negativ_test.py)

Kjøres slik:
python tests/negativ_test.py

Tester hvordan koden håndterer:

* Manglende kolonner
* Ikke-numeriske data 
* Feil input i beslutningsfunksjon
