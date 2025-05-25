Denne mappen inneholder tester for å verifisere at funksjonaliteten i prosjektet oppfører seg som forventet. 
I tests-mappen finner man systematiske, automatiserte tester med unittest, og manuelle negativtester som prøver å provosere frem feil. Dette gir en god balanse mellom bekreftelse på korrekt funksjonalitet og robusthet mot feilbruk eller manglende data.
Det er to testfiler her unitest og negativ test, som dekker ulike typer testing.

Totalt kjøres 13 automatiske tester:
3 tester for VærDataPlotter (f.eks. at data lastes riktig og at glidende gjennomsnitt kan beregnes)
3 tester for MiljoPerMnd (gjennomsnitt, median og standardavvik per måned)
7 tester for Databehandling (f.eks. interpolering, uteliggere, og manglende datoer)

*Unitest*
"test_alle_klasser.py" inneholder enhetstester med unittest
Dette er den viktigste testfilen og inneholder enhetstester for prosjektet. Testene er organisert i tre klasser (en fra hver oppgave):
- VærDataPlotter (fra "opg5.py")
- MiljoPerMnd (fra "opg4.py")
- Databehandling (fra "opg6_databehandling.py")
tearDown og setUp er ikke tester, men metoder som brukes i unittesten for hver klasse og har som formål å organisere og rydde opp imellom testene. Dette sikrer at testene er isolerte og ikke påvirker hverandre.
Før hver test kjøres, oppretter setUp()-metoden et nytt datasett og lagrer det som en midlertidig CSV-fil. Etter testene kjøres tearDown() for å rydde opp. 

*Negativ test* 
Denne testfilen er organisert i tre klasser (en fra hver oppgave):
- def test_miljo_negativ_mangler_kolonne (fra "opg4.py")
- test_korrelasjonsheatmap_negativ (fra "opg5.py")
- test_bør_ta_med_paraply_feil_input (fra "opg6_analyse.py")
Denne filen inneholder manuelle negativtester som sjekker hvordan programmet håndterer feil og ufullstendige data. Den bruker ikke unittest, men består av vanlige funksjoner med try/except og assert. Disse testene skriver ut meldinger i terminalen hvis forventede feil blir fanget opp.

test_miljo_negativ_mangler_kolonne inneholder en test der kolonnen "Temperatur (°C)" mangler fra datasettet  hvor man forventer at MiljoPerMnd kaster en KeyError.
test_korrelasjonsheatmap_negativ inneholder en test der VærDataPlotter prøver å lage et korrelasjonsheatmap uten noen numeriske kolonner som skal føre til en feilmelding.
test_bør_ta_med_paraply_feil_input inneholder en test som sender inn ugyldige verdier til en funksjon som skal gi råd om man bør ta med paraply for å sjekke at den takler feil input.