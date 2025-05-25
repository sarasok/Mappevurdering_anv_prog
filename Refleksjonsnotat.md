# Refleksjonsnotat
# 1
Gjennom dette prosjektet har vi jobbet med flere deler av datavitenskap, fra å sette opp utviklingsmiljø til å samle inn og analysere miljødata. Vi fikk testet ut mange ulike verktøy og metoder. Selv om mye var nytt, føltes det motiverende å jobbe med et prosjekt som hadde en tydelig rød tråd med tydelige arbeidsoppgaver. Det gjorde samarbeidet lettere da vi lettere kunne fordele arbeidsoppgaver. 
# 2
Allerede i oppgave 1 lærte vi viktigheten av et godt utviklingsmiljø med Visual Studio Code, GitHub, Python og Jupyter Notebooks. Det tok litt tid før vi forstod mekanismene bak, men vi så at det var nyttig å få det på plass tidlig så vi kunne jobbe mer effektivt sammen. Å bruke Git for versjonskontroll var også noe vi fikk mer erfaring med, selv om det tok litt tid å venne seg til arbeidsflyten. 

Når det kom til datainnsamling i oppgave 2, brukte vi åpne API-er fra Frost.met og OpenWeatherMap vha. bibliotekene pandas og requests. Det ga oss en praktisk forståelse av hvordan åpne data kan integreres i applikasjoner. Det var vanskelig å finne nok data. Vi merket fort at åpne datasett ofte har sine begrensninger. Et eksempel er begrenset dekning, da noen av datasettene bare dekket visse tidspunkter. Dette kunne gjøre det vanskeligere å sammenligne over lange perioder, men ved hjelp av ulike moduler i python, så klarte vi å samle dataene i ulike CSV-filer. Videre så vi at det ville bli lettere å analysere dataene hvis de var samlet i en stor CSV-fil og gjorde derfor dette vha. pandas.

I oppgave 3 tok vi for oss databehandlingsdelen av prosjektet. Her lærte vi hvordan vi kunne bruke bla. Pandas for å rydde og analysere informasjonen. Det å forstå hvordan vi skulle håndtere manglende verdier, og bruke list comprehensions og iteratorer på en effektiv måte, tok litt tid, men ga oss god læring. Vi fant heller ikke datasett med feil, så vi lagde en kode som manuelt la inn tilfeldige feil for oss. Formålet med dette var at vi senere skulle lage koder for lokalisering av feil samt datarensing. 

Analyse- og visualiseringsdelen handlet mye om å regne ut statistiske mål som gjennomsnitt, median og standardavvik. I tilegg har vi laget visualiseringer som hjalp oss å avdekke sammenhenger og trender mellom vær- og miljødata. Her har læringskurven vært bratt, men vi har lært  hvordan NumPy, Seaborn, Plotly og Pandas fungerer i praksis, og hvordan vi kan trekke ut informasjon fra dataene. Ett eksempel på dette er at det er en negativ sammenheng mellom temperatur og relativ fuktighet. Det har vært nyttig å eksperimentere med ulike grafer for å avdekke trendene på best mulig måte.

For den prediktaktive analysen vår har vi brukt en lineær regresjonsmodell for å forutsi skydekke basert på temperatur, lufttrykk og relativ fuktighet. Først skalerte vi funksjonene med StandardScaler, og deretter trente vi modellen med LinearRegression fra sklearn. Resultatene viste moderat presisjon (R² og RMSE ble beregnet), og visualiseringer av faktisk vs. predikert verdier ga oss innsikt i modellens begrensninger. Modell og skalering ble også lagret med joblib for fremtidig bruk. Denne delen ga oss erfaring med både tren/test-splitting, evaluering av maskinlæringsmodeller, og hvordan disse kan brukes til å gi innsikt i miljødata.

# 3 
Det å lære mange nye biblioteker og konsepter samtidig kunne bli litt overveldende. Vi brukte en del tid på å forstå dokumentasjon og finne ut hvordan ting henger sammen. Men det har også gjort oss tryggere på å lære nye verktøy på egen hånd. I læringsprosessen har vi benyttet oss av ulike læringsressurser som «Jupyter-boken» (fra Blackboard), forelesningsnotater og kunstig intelligens. 

Gruppen opplevde noen merge-konflikter i Git når flere jobbet på samme filer. For å unngå dette begynte vi alltid å pulle før vi startet å jobbe, slik at vi hadde siste versjon. Noen ganger skrev vi også kode i eksterne filer først, for så å lime det inn senere. Dette gjorde samarbeidet enklere og ga oss bedre forståelse for versjonskontroll.


# 4
Samarbeidet i gruppa har vært preget av god kommunikasjon, tydelig fordeling av ansvar og jevnlig kontakt. Vi startet hver oppgave med en felles gjennomgang, og fordelte deretter konkrete oppgaver basert på styrker og interesser. Hvis noen stod fast hjalp vi hverandre. Det gjorde prosjektet mer oversiktlig og mindre stressende. Resultatet ble en fungerende analyseapplikasjon som kunne hente, rydde, analysere og visualisere miljødata. 

# 5
Det er fortsatt ting som kunne vært forbedret, som å gjøre visualiseringene mer interaktive, men vi er fornøyde med det vi fikk til innenfor tidsrammen. I etterkant ser vi at vi har lært mye om hele prosessen rundt dataanalyse: fra henting til ferdige visualiseringer. Vi har også blitt mer kjent med verktøy som vi kommer til å bruke videre i både studier og jobb. Alt i alt har det vært en lærerik erfaring, og vi sitter igjen med en bedre forståelse av hvordan data kan brukes til å si noe om miljøet rundt oss.


# 6
Videre utvikling:
Om vi skulle jobbet videre med prosjektet, kunne vi gjort det mer brukervennlig ved å legge inn enkel brukerinput, for eksempel slik at brukeren kunne skrive inn en dato og få opp relevant graf. Vi kunne også lagt til flere typer grafer og prøvd å hente data automatisk hver dag. I tillegg kunne vi testet ut enkle klassifiseringsmodeller, for eksempel for å forutsi om det blir regn eller ikke.

# 7
Gjennom dette prosjektet har vi lært mye om hvordan man bruker Python til å hente, analysere og visualisere data. Vi har også fått erfaring med samarbeid, versjonskontroll og hvordan man løser praktiske problemer. Denne erfaringen gir oss et godt grunnlag for videre kurs og prosjekter, og vi føler oss tryggere på å jobbe med data og programmering i fremtiden.
