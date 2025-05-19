I src-mappen inneholder all funksjonalitet for mappe del 2. Dette er gunstig fordi det gir oss bedre struktur og kontroll. på denne måten får vi kode som er skilt fra datafiler, notebooker og tester. Src-mappen vår inneholder .py filer som er strukturert som funksjoner og klasser. Denne funksjonaliteten importeres deretter videre i notebooken "del_2.ipynb" som fremstiller det vi har kodet i src.

*opg4.py:*
I filen opg4.py oppretter vi MiljoPerMnd-klassen.
Her analysere vi miljø- og værdata ved hjelp av statistiske metoder. Hensikten er å avdekke mønstre og variasjoner i viktige værvariabler over tid, spesielt på månedsbasis. Programmet er bygd opp som en Python-klasse kalt MiljoPerMnd, og benytter bibliotekene pandas og numpy til databehandling.

Når et objekt av MiljoPerMnd opprettes, leses en CSV-fil med værdata inn. Dataene forventes å inneholde en kolonne med datoer (Dato) og flere kolonner med værmålinger, som temperatur, lufttrykk, nedbør, relativ fuktighet og skydekke. Eventuelle mellomrom i kolonnenavn fjernes automatisk for å unngå feil. Dato-kolonnen konverteres til datetime-format, og det hentes ut to nye kolonner: År og Måned. Dette gjør det mulig å gruppere dataene etter måned og utføre statistiske beregninger måned for måned.

Analysen gir innsikt i både typiske forhold og hvor stabile disse forholdene er fra måned til måned.

I klassen har vi tre metoder:
- gjennomsnitt_per_mnd()
Beregner det  gjennomsnittet for hver variabel, gruppert etter år og måned. Dette gir et overblikk over den generelle utviklingen og variasjonen i værdataene.

- median_per_mnd()
Beregner medianverdien for hver variabel per måned. Medianen er nyttig for å forstå sentraltendensen uten å bli påvirket av ekstreme enkeltverdier (uteliggere).

- standardavvik_per_mnd():
Beregner standardavviket, som viser hvor mye målingene svinger rundt gjennomsnittet. Et høyt standardavvik indikerer store variasjoner fra dag til dag, mens lavt standardavvik tyder på stabile værforhold.


*opg5.py:*
Her lager vi VærDataPlotter-klassen
Den gjør det enklere å visualisere og utforske vær- og klimadata i datasettet vårt. Klassen bruker bibliotekene pandas, matplotlib, seaborn og plotly for å lage ulike typer grafer, både statiske og interaktive.
Klassen gjør det lettere å finne sammenhenger og trender i ulike værvariabler som temperatur, lufttrykk, nedbør, skydekke og relativ fuktighet over tid.

Ved opprettelse av et objekt av klassen, leses en CSV-fil med værdata inn som et pandas-datasett. Dato-kolonnen konverteres til datetime-format slik at data kan vises over tid. 

I klassen har vi 7 metoder:
- tegn_temp_lufttrykk_matplotlib()
Lager et linjediagram der temperatur og lufttrykk vises over tid, med to ulike y-akser. Temperatur vises til venstre, og lufttrykk til høyre. Denne visualiseringen bruker matplotlib og seaborn.

- tegn_nedbør_skydekke_sma()
Viser 7-dagers glidende gjennomsnitt for både nedbør og skydekke. Dette jevner ut dag-til-dag variasjoner og gjør det lettere å se langsiktige trender i nedbør og skyforhold.

- tegn_temp_vs_fuktighet()
Lager et scatterplot med en regresjonslinje som viser sammenhengen mellom temperatur og relativ fuktighet. Dette gir en visuell indikasjon på eventuell korrelasjon mellom disse to variablene.

- tegn_interaktiv_temp_lufttrykk_plotly()
Interaktiv versjon av temperatur og lufttrykk over tid, med to y-akser. Brukeren kan holde musen over et punkt for å få eksakte verdier. Lages med Plotly.

- tegn_korrelasjonsheatmap()
Lager et heatmap som viser korrelasjonsverdier mellom alle numeriske kolonner i datasettet. Det gir en rask oversikt over hvilke variabler som samvarierer.

- tegn_interaktiv_variabelvelger()
Lager et interaktivt linjediagram hvor brukeren kan velge hvilken variabel som skal vises over tid (temperatur, lufttrykk, nedbør, fuktighet eller skydekke) ved hjelp av en dropdown-meny.

- tegn_interaktiv_boblegraf()
Lager et scatterplot der x-aksen er temperatur, y-aksen er lufttrykk, fargen representerer relativ fuktighet og størrelsen på boblene viser nedbør. Denne typen graf gir mange dimensjoner av informasjon i ett plott.