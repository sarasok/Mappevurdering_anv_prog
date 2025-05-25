# MAPPE DEL 1:

Har hentet inn 3 csv filer fra frost med ulike dataer for været. En for lufttrykk, en for nedbør og en for temperatur. 
Videre er dataene gruppert etter dato. Derfor ble det laget en ny csv fil for temperatur data, fordi disse målingene
var for hvert 15. min, og ikke for hver dag. Av denne grunn, ble det laget en funksjon som regner ut gjennomsnittet for hver dag. 
(Dette blir gjort i "kode_som_henter_API.ipynb")

Når denne samlet csv-filen ble opprettet, opprettet vi en backup, slik at man manuelt kunne legge inn feil/mangler for å
deretter rette opp i feilene. Dette var fordi det ikke fantes noen naturlige feil i de datasettene vi hentet inn. 
(Dette blir gjort i "sammenslaaing_gjsnitt.ipynb")

## Data rensing:
Manglende verdier: Verdier som manglet i sentrale kolonner som temperatur, lufttrykk, nedbør, relativ fuktighet og skydekke ble fylt inn med gjennomsnittet av dagen før og etter – en form for lineær imputering.
Urealistiske verdier: Ekstreme eller ulogiske målinger, som temperaturer under -50°C eller over 50°C, ble oppdaget og erstattet på samme måte som manglende verdier.
Negative verdier: Absoluttverdier ble tatt av Nedbør (mm), Lufttrykk (hPa), Skydekke (oktas), og Relativ fuktighet (%) for å sikre at ingen fysiske umuligheter var i datasettet.
Dato-konsistens: Dato-kolonnen ble konvertert til datetime og kontinuerlige datoer ble generert, for å sikre at datasettet representerer en sammenhengende tidsserie.
(Dette blir gjort i "rense_data.ipynb")

I tillegg ble det opprettet en ny csv-fil (R_Sammenslaaing_uten_feil.csv) som oppdaterer de verdiene som var feil i den originale csv-filen. For å gjøre dataen mer oversiktlig, har pandas blitt tatt i bruk. 