# Refleksjonsnotat
Gjennom dette prosjektet har vi jobbet med flere deler av datavitenskap, fra å sette opp utviklingsmiljø til å samle inn og analysere miljødata. Vi fikk testet ut mange ulike verktøy og metoder. Selv om mye var nytt, føltes det motiverende å jobbe med et prosjekt som hadde en tydelig rød tråd med tydelige arbeidsoppgaver. Det gjorde samarbeidet lettere da vi lettere kunne fordele arbeidsoppgaver. 

Allerede i oppgave 1 lærte vi viktigheten av et godt utviklingsmiljø med Visual Studio Code, GitHub, Python og Jupyter Notebooks. Det tok litt tid å forstå hvordan det hele hang sammen, men det var nyttig å få det på plass tidlig slik at vi kunne jobbe mer effektivt. Å bruke Git for versjonskontroll krevde litt øving, men vi fikk bedre flyt etter hvert.

I oppgave 2 hentet vi værdata via åpne API-er fra Frost.met og OpenWeatherMap ved hjelp av pandas og requests. Det ga oss praktisk innsikt i hvordan åpne data kan integreres i et program. Vi merket at datasettene ofte hadde begrenset dekning, noe som gjorde det vanskelig å sammenligne over tid. Vi løste dette ved å samle data i flere CSV-filer og kombinere dem til én med pandas.

I oppgave 3 jobbet vi med å rydde og analysere dataene. Vi lærte å håndtere manglende verdier, og å bruke list comprehensions og iteratorer mer effektivt. Vi lagde også en kode som la inn tilfeldige feil, slik at vi senere kunne teste funksjoner for datarensing og feilkontroll.

Analyse- og visualiseringsdelen handlet mye om å regne ut statistiske mål som gjennomsnitt, median og standardavvik. I tilegg har vi laget visualiseringer som hjalp oss å avdekke sammenhenger og trender mellom vær- og miljødata. Her har læringskurven vært bratt, men vi har lært  hvordan NumPy, Seaborn, Plotly og Pandas fungerer i praksis, og hvordan vi kan trekke ut informasjon fra dataene. Ett eksempel på dette er at det er en negativ sammenheng mellom temperatur og relativ fuktighet. Det har vært nyttig å eksperimentere med ulike grafer for å avdekke trendene på best mulig måte.

For den prediktaktive analysen i oppgave 6 har vi brukt en lineær regresjonsmodell for å forutsi skydekke basert på temperatur, lufttrykk og relativ fuktighet. Først skalerte vi funksjonene med StandardScaler, og deretter trente vi modellen med LinearRegression fra sklearn. Resultatene viste moderat presisjon (R² og RMSE ble beregnet), og visualiseringer av faktisk vs. predikert verdier ga oss innsikt i modellens begrensninger. Modell og skalering ble også lagret med joblib for fremtidig bruk. Denne delen ga oss erfaring med både tren/test-splitting, evaluering av maskinlæringsmodeller, og hvordan disse kan brukes til å gi innsikt i miljødata.


Det å lære mange nye biblioteker og konsepter samtidig kunne bli litt overveldende. Vi brukte en del tid på å forstå dokumentasjon og finne ut hvordan ting henger sammen. Men det har også gjort oss tryggere på å lære nye verktøy på egen hånd. I læringsprosessen har vi benyttet oss av ulike læringsressurser som «Jupyter-boken» (fra Blackboard), forelesningsnotater og kunstig intelligens. 

Gruppen opplevde noen merge-konflikter i Git når flere jobbet på samme filer. For å unngå dette begynte vi alltid å pulle før vi startet å jobbe, slik at vi hadde siste versjon. Noen ganger skrev vi også kode i eksterne filer først, for så å lime det inn senere. Dette gjorde samarbeidet enklere og ga oss bedre forståelse for versjonskontroll.


Samarbeidet i gruppa har vært preget av god kommunikasjon, tydelig fordeling av ansvar og jevnlig kontakt. Vi startet hver oppgave med en felles gjennomgang, og fordelte deretter konkrete oppgaver basert på styrker og interesser. Hvis noen stod fast hjalp vi hverandre. Det gjorde prosjektet mer oversiktlig og mindre stressende. Resultatet ble en fungerende analyseapplikasjon som kunne hente, rydde, analysere og visualisere miljødata. 


Selv om vi kunne forbedret visualiseringene, er vi fornøyde med resultatet. Vi har lært mye om hele analyseprosessen og verktøy vi vil bruke videre. Totalt sett har prosjektet gitt oss bedre forståelse for hvordan data kan brukes til å si noe om miljøet.


Videre utvikling:
Om vi skulle jobbet videre med prosjektet, kunne vi gjort det mer brukervennlig ved å legge inn enkel brukerinput, for eksempel slik at brukeren kunne skrive inn en dato og få opp relevant graf. Vi kunne også lagt til flere typer grafer og prøvd å hente data automatisk hver dag. I tillegg kunne vi testet ut enkle klassifiseringsmodeller, for eksempel for å forutsi om det blir regn eller ikke.


Gjennom dette prosjektet har vi lært mye om hvordan man bruker Python til å hente, analysere og visualisere data. Vi har også fått erfaring med samarbeid, versjonskontroll og hvordan man løser praktiske problemer. Denne erfaringen gir oss et godt grunnlag for videre kurs og prosjekter, og vi føler oss tryggere på å jobbe med data og programmering i fremtiden.
