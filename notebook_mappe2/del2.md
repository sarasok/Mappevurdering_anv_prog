MAPPE DEL 2:
## Business Understanding
Vi ønsker å kunne forutsi skydekke ut fra værmålinger. Dette kan være nyttig for planlegging, miljøanalyse eller energibehov.

## Data Understanding
Vi bruker historiske værdata (temperatur, lufttrykk og fuktighet) sammen med skydekke som målvariabel. Vi visualiserer også datasettet for å forstå trender og mangler.



## Oppgave 6: Prediktiv analyse
- Koden ligger i `src/`, og visualiseringene er dokumentert i `notebooks/Opg6.ipynb`.
I denne delen av prosjektet brukte vi lineær regresjon med scikit-learn for å forutsi skydekke basert på historiske værdata. Målet var å undersøke om det finnes en sammenheng mellom temperatur, lufttrykk og relativ fuktighet – og hvor godt disse variablene kan predikere skydekke.

### Valg av funksjoner og målvariabel
   Vi brukte Temperatur (°C), Lufttrykk (hPa) og Relativ fuktighet (%) som uavhengige variabler, og Skydekke (oktas) som den avhengige variabelen vi ønsket å predikere.

### Datavask og håndtering av manglende verdier
   Vi håndterte manglende verdier med lineær interpolasjon og fjernet uteliggere med IQR-metoden. Dette forbedret modellens pålitelighet.

### Oppdeling og skalering
   Data ble delt i trenings- og testsett med train_test_split. Funksjoner ble standardisert med StandardScaler for å gi modellen lik skala å jobbe med.

### Modelltrening og evaluering 
   Vi trente en lineær regresjonsmodell og evaluerte den med MSE, RMSE og R². Resultatene viste moderat nøyaktighet og ga innsikt i modellens styrker og begrensninger.

### Visualisering av resultater
   Vi laget flere typer grafer for å støtte analysen:
   - Linjediagram for å vise hvordan verdier utviklet seg over tid
   - Stolpediagram for å vise ukentlige gjennomsnittsverdier
   - Heatmap for å vise korrelasjon mellom variabler
   - Dobbel y-akse for å sammenligne fuktighet og skydekke

### Håndtering og visualisering av manglende data
   Vi viste både før- og etterbilder av interpolering for å illustrere hvordan manglende verdier påvirker analysen. Dette gjorde det tydelig hvordan rensing påvirker trendene.

### Evaluering og refleksjon
- Heatmapet var viktig for å identifisere hvilke variabler som var relevante for regresjon.
- Linjediagrammene gjorde det lett å se sesongvariasjoner i skydekke og fuktighet.
- Vi valgte lineær regresjon fordi den er enkel å bruke og lett å tolke. Den ga oss en god introduksjon til prediktiv modellering i Python.
- Samlet sett har vi lært hvordan man forbereder, trener og evaluerer en enkel ML-modell, og hvordan visualisering støtter datadrevet innsikt.



