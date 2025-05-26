I src-mappen inneholder all funksjonalitet for mappe del 2. Dette er gunstig fordi det gir oss bedre struktur og kontroll. på denne måten får vi kode som er skilt fra datafiler, notebooker og tester. Src-mappen vår inneholder .py filer som er strukturert som funksjoner og klasser. Denne funksjonaliteten importeres deretter videre i notebooken "del_2.ipynb" som fremstiller det vi har kodet i src.

# opg4.py: (Se filen: ['opg4.py'](opg4.py))
I filen opg4.py oppretter vi MiljoPerMnd-klassen.
Her analysere vi miljø- og værdata ved hjelp av statistiske metoder. Hensikten er å avdekke mønstre og variasjoner i viktige værvariabler over tid, spesielt på månedsbasis. Programmet er bygd opp som en Python-klasse kalt MiljoPerMnd, og benytter bibliotekene pandas og numpy til databehandling.

Når et objekt av MiljoPerMnd opprettes, leses en CSV-fil med værdata inn. Dataene forventes å inneholde en kolonne med datoer (Dato) og flere kolonner med værmålinger, som temperatur, lufttrykk, nedbør, relativ fuktighet og skydekke. Eventuelle mellomrom i kolonnenavn fjernes automatisk for å unngå feil. Dato-kolonnen konverteres til datetime-format, og det hentes ut to nye kolonner: År og Måned. Dette gjør det mulig å gruppere dataene etter måned og utføre statistiske beregninger måned for måned.

Analysen gir innsikt i både typiske forhold og hvor stabile disse forholdene er fra måned til måned.

I klassen har vi tre metoder:
## gjennomsnitt_per_mnd()
Beregner det  gjennomsnittet for hver variabel, gruppert etter år og måned. Dette gir et overblikk over den generelle utviklingen og variasjonen i værdataene.

## median_per_mnd()
Beregner medianverdien for hver variabel per måned. Medianen er nyttig for å forstå sentraltendensen uten å bli påvirket av ekstreme enkeltverdier (uteliggere).

## standardavvik_per_mnd():
Beregner standardavviket, som viser hvor mye målingene svinger rundt gjennomsnittet. Et høyt standardavvik indikerer store variasjoner fra dag til dag, mens lavt standardavvik tyder på stabile værforhold.


# opg5.py: (Se filen: ['opg5.py'](opg5.py))
Her lager vi VærDataPlotter-klassen
Den gjør det enklere å visualisere og utforske vær- og klimadata i datasettet vårt. Klassen bruker bibliotekene pandas, matplotlib, seaborn og plotly for å lage ulike typer grafer, både statiske og interaktive.
Klassen gjør det lettere å finne sammenhenger og trender i ulike værvariabler som temperatur, lufttrykk, nedbør, skydekke og relativ fuktighet over tid.

Ved opprettelse av et objekt av klassen, leses en CSV-fil med værdata inn som et pandas-datasett. Dato-kolonnen konverteres til datetime-format slik at data kan vises over tid. 

I klassen har vi 7 metoder:
## tegn_temp_lufttrykk_matplotlib()
Lager et linjediagram der temperatur og lufttrykk vises over tid, med to ulike y-akser. Temperatur vises til venstre, og lufttrykk til høyre. Denne visualiseringen bruker matplotlib og seaborn.

## tegn_nedbør_skydekke_sma()
Viser 7-dagers glidende gjennomsnitt for både nedbør og skydekke. Dette jevner ut dag-til-dag variasjoner og gjør det lettere å se langsiktige trender i nedbør og skyforhold.

## tegn_temp_vs_fuktighet()
Lager et scatterplot med en regresjonslinje som viser sammenhengen mellom temperatur og relativ fuktighet. Dette gir en visuell indikasjon på eventuell korrelasjon mellom disse to variablene.

## tegn_interaktiv_temp_lufttrykk_plotly()
Interaktiv versjon av temperatur og lufttrykk over tid, med to y-akser. Brukeren kan holde musen over et punkt for å få eksakte verdier. Lages med Plotly.

## tegn_korrelasjonsheatmap()
Lager et heatmap som viser korrelasjonsverdier mellom alle numeriske kolonner i datasettet. Det gir en rask oversikt over hvilke variabler som samvarierer.

## tegn_interaktiv_variabelvelger()
Lager et interaktivt linjediagram hvor brukeren kan velge hvilken variabel som skal vises over tid (temperatur, lufttrykk, nedbør, fuktighet eller skydekke) ved hjelp av en dropdown-meny.

## tegn_interaktiv_boblegraf()
Lager et scatterplot der x-aksen er temperatur, y-aksen er lufttrykk, fargen representerer relativ fuktighet og størrelsen på boblene viser nedbør. Denne typen graf gir mange dimensjoner av informasjon i ett plott.


# opg6.py
I oppgave 6 blir det kombinert, renset, analysert og modelleret både vær- og luftkvalitetsdata for å forutsi skydekke og evaluere luftforhold. Dette gjøres gjennom en helhetlig datapipeline som involverer preprocessing, outlierfjerning, interpolering, regresjonsmodellering og visualisering.

Modulen består av flere Python-filer som er organisert i klasser og funksjoner for god struktur og gjenbrukbarhet:

## opg6_databehandling.py: (Se filen: ['opg6_databehandling.py'](opg6_databehandling.py))
Denne modulen håndterer datarensing og sammenslåing. Vi interpolerer manglende verdier med lineær metode, fjerner uteliggere med IQR og definerte grenser, og sørger for at tidsseriene fra ulike datakilder (vær og luftkvalitet) blir synkronisert. Vi resampler også luftdata til daglig nivå og bruker merge for å kombinere datasettene på datokolonnen. Dette gir et komplett datasett for analyse og modellering.

Funksjonene i denne modulen er:
### les_og_forbered_data()
Leser inn to datasett (vær og luftkvalitet), konverterer datoformat og gjør dataene klare for sammenslåing.
### resample_og_interpoler()
Resampler luftkvalitetsdata til daglig nivå og fyller inn manglende verdier med lineær interpolasjon.
### fjern_iqr_outliers()
Fjerner outliers fra en tidsserie basert på IQR-metoden.
### slå_sammen_data()
Slår sammen vær- og luftdata på datokolonnen for videre analyse og modelltrening.


## opg6_analyse.py: (Se filen: ['opg6_analyse.py'](opg6_analyse.py))
Her defineres funksjoner for å trene en lineær regresjonsmodell med scikit-learn. Vi bruker standardisering (StandardScaler) før modelltrening, og funksjonen returnerer både modellen, skaleringsobjektet og evalueringsmetrikker som MSE, R² og RMSE. Det er også en hjelpefunksjon bør_ta_med_paraply() som gir anbefaling basert på predikert skydekke og luftfuktighet – et eksempel på praktisk bruk av modellresultatet.


Funksjonene i denne modulen er:
### tren_modell()
Trener en lineær regresjonsmodell med tre inputvariabler og returnerer modellen, en StandardScaler og evalueringsmetrikker (MSE, RMSE, R²).
### lagre_modell()
Lagrer modell og scaler som .pkl-filer for gjenbruk.
### bør_ta_med_paraply()
En enkel heuristisk funksjon som gir anbefaling (f.eks. ta med paraply) basert på skydekke og fuktighet – praktisk anvendelse av modellresultater.

## opg6_skydekkemodel.py: (Se filen: ['opg6_skydekkemodel.py'](opg6_skydekkemodel.py))
Klassen SkydekkePredictor bruker tre værvariabler – temperatur, lufttrykk og relativ fuktighet – som input for å predikere skydekke. Etter trening evalueres modellen og visualiserer forskjellen mellom predikert og faktisk skydekke. Modell og scaler lagres til fil for videre bruk.


Funksjonene i denne modulen er:
### forbered_data()
Splitter data i trenings- og testsett.
### tren_og_evaluer()
Trener modellen, evaluerer ytelse og viser graf over faktisk vs. predikert skydekke.
### lagre_modell()
Lagrer modellen og scaleren til fil.


## opg6_visualisering.py: (Se filen: ['opg6_visualisering.py'](opg6_visualisering.py))
Her lager vi visualiseringer av interpolerte data og resultatene fra modellen. Vi viser bl.a. interpolering av NO₂-data, glattet utvikling av skydekke og luftfuktighet, samt korrelasjonsmatrise for å utforske sammenhenger mellom variablene. Disse plottene gir innsikt i både datakvalitet og modellens ytelse.

Funksjonene i denne modulen er:
### plot_interpolation()
Viser hvordan interpolering fyller inn hull i tidsserier.
### plott_skydekke_fuktighet()
Lager dobbel y-akse-plott for å vise smoothed utvikling i skydekke og fuktighet.
### vis_korrelasjonsmatrise()
Lager et heatmap som viser samvariasjon mellom vær- og luftvariabler.