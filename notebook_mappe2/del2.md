MAPPE DEL 2:


## Oppgave 4: Statistisk analyse av miljødata

I denne delen av prosjektet brukte vi statistiske metoder med NumPy og pandas for å analysere månedlige trender i værdata. Målet var å oppsummere dataene med sentralmål og spredningsmål, samt undersøke mulige sammenhenger mellom variabler.

### Beregning av statistiske mål
Vi brukte følgende statistiske mål for å beskrive utviklingen av værvariabler over tid:
- Gjennomsnitt: For å finne den typiske verdien hver måned.
- Median: For å unngå skjevhet fra ekstreme verdier.
- Standardavvik: For å måle hvor mye verdiene varierer hver måned.

Disse ble beregnet månedlig for fem sentrale variabler:
- Temperatur (°C)
- Lufttrykk (hPa)
- Nedbør (mm)
- Relativ fuktighet (%)
- Skydekke (oktas)

### Metodikk og gruppering
Vi brukte pandas `groupby` for å gruppere data etter år og måned. Dette gjorde det mulig å trekke ut mønstre i dataene over tid, og sammenligne hvordan ulike måneder skiller seg ut.

### Avdekking av mønstre og sammenhenger
Ved å analysere gjennomsnitt og standardavvik kunne vi se:
- Sesongvariasjoner i temperatur og nedbør
- Hvor stabile eller variable forholdene var måned for måned

I tillegg ble sammenhenger mellom variabler utforsket ved hjelp av korrelasjonsanalyse i andre oppgaver, men resultatene her la grunnlaget for videre tolkning.

### Visualisering og tolkning
Resultatene fra statistikken ble senere visualisert, hvor vi brukte linjeplott, glidende gjennomsnitt og korrelasjonsheatmaps. Den statistiske oppsummeringen i denne oppgaven ga et godt grunnlag for disse visualiseringene.

### Erfaring og refleksjon
- Vi lærte hvordan man bruker pandas og NumPy for å gruppere og analysere store datasett.
- Oppgaven viste verdien av å bruke flere statistiske mål samtidig.
- Den gjorde det også tydelig hvor viktig det er å kontrollere for skjevheter i datagrunnlaget før man går videre til tolkning og modellering.


## Oppgave 5: Visualisering av værdata

- Koden ligger i `src/`, og visualiseringene er dokumentert i `notebooks/Opg5.ipynb`.

I denne delen av prosjektet utviklet vi en fleksibel Python-klasse for visualisering av værdata. Målet var å utforske hvordan ulike klimavariabler som temperatur, lufttrykk, fuktighet, nedbør og skydekke varierer over tid, og hvordan disse kan presenteres på både statiske og interaktive måter.

### Brukte biblioteker
Vi benyttet flere populære biblioteker for databehandling og visualisering:
- Pandas for lasting og behandling av datasettet
- Matplotlib og Seaborn for å lage statiske grafer
- Plotly for å lage interaktive visualiseringer

### Implementering
Vi opprettet en klasse `VærDataPlotter` med metoder som:
- Leser værdata fra CSV
- Konverterer datoer til riktig format
- Tilrettelegger og tegner ulike grafer

### Typer visualiseringer
Vi lagde en rekke ulike visualiseringer for å utforske sammenhenger og mønstre:

- Linjediagram med dobbel y-akse  
  Viser temperatur og lufttrykk samtidig for å fange daglig variasjon i begge.

- Glidende gjennomsnitt 
  Viser trender i nedbør og skydekke ved å bruke 7-dagers snitt for å glatte ut støy.

- Scatterplot med regresjonslinje
  Visualiserer sammenhengen mellom temperatur og relativ fuktighet, med automatisk regresjonslinje.

- Interaktive grafer
  Brukeren kan:
  - Se temperatur og lufttrykk med hover-effekt og zoom
  - Velge mellom ulike variabler i en meny (én variabel om gangen)
  - Utforske en boblegraf med temperatur (x), lufttrykk (y), farge (fuktighet) og størrelse (nedbør)

- Korrelasjonsheatmap
  Viser styrken på lineære sammenhenger mellom alle numeriske værvariabler.

### Refleksjon og innsikt
- Dobbel y-akse og glidende gjennomsnitt gjorde det enklere å tolke samvariasjoner og trender.
- Interaktive grafer ga en mer utforskende opplevelse.
- Heatmapet ga innsikt i hvilke variable som korrelerer sterkest


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



