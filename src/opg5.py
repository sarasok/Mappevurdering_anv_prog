# Importerer nødvendige biblioteker for databehandling og visualisering
import pandas as pd  # Pandas brukes til å lese, organisere og analysere datasett (f.eks. CSV-filer)
import matplotlib.pyplot as plt  # Matplotlib er et kraftig bibliotek for å lage statiske grafer og figurer
import seaborn as sns  # Seaborn bygger på matplotlib og gjør det enklere å lage pene og statistiske grafer
import plotly.graph_objects as go  # Plotly.graph_objects brukes for å bygge detaljerte, interaktive figurer manuelt
import plotly.express as px  # Plotly Express er en enklere og raskere måte å lage interaktive grafer med få linjer kode

# Lager en klasse som kapsler inn funksjoner for å laste, bearbeide og visualisere værdata
class VærDataPlotter:
    def __init__(self, filsti):
        # Leser CSV-filen som inneholder værdata, og lagrer den som en DataFrame (tabell)
        self.df = pd.read_csv(filsti)

        # Konverterer kolonnen 'Dato' fra tekst (string) til datotid-objekter
        # Dette gjør det mulig å bruke datotid-funksjonalitet, som sortering og plotting over tid
        self.df['Dato'] = pd.to_datetime(self.df['Dato'])

        # Setter standardtema for grafer laget med Seaborn
        sns.set_theme(style="whitegrid")  # Gir lys bakgrunn og diskret rutenett som forbedrer lesbarhet

    def tegn_temp_lufttrykk_matplotlib(self):
        """
        Lager en statisk linjegraf som viser både temperatur og lufttrykk over tid ved hjelp av matplotlib og seaborn.
        Temperatur og lufttrykk vises med to separate y-akser.
        """

        # Oppretter figur og hovedakse for temperaturplottet
        fig, ax1 = plt.subplots(figsize=(12, 6))  # Lager en figur med spesifisert størrelse

        # Plotter temperaturdata som en linje over tid på den første y-aksen (venstre)
        sns.lineplot(data=self.df, x='Dato', y='Temperatur (°C)', ax=ax1,
                     label="Temperatur (°C)", color='tab:red')  # Bruker rød farge for temperatur

        # Setter y-akseetikett og farge for temperaturaksen
        ax1.set_ylabel("Temperatur (°C)", color='tab:red')
        ax1.tick_params(axis='y', labelcolor='tab:red')  # Sørger for at tallene på y-aksen får samme farge

        # Lager en ny y-akse som deler x-aksen, men vises på høyre side (for lufttrykk)
        ax2 = ax1.twinx()
        sns.lineplot(data=self.df, x='Dato', y='Lufttrykk (hPa)', ax=ax2,
                     label="Lufttrykk (hPa)", color='tab:blue')  # Bruker blå farge for lufttrykk

        # Setter etikett og farge for lufttrykksaksen
        ax2.set_ylabel("Lufttrykk (hPa)", color='tab:blue')
        ax2.tick_params(axis='y', labelcolor='tab:blue')

        # Setter tittel for hele grafen
        plt.title("Temperatur og Lufttrykk over tid")

        # Roterer datoene på x-aksen for bedre lesbarhet
        fig.autofmt_xdate()

        # Justerer layouten slik at elementene ikke overlapper
        fig.tight_layout()

        # Viser figuren
        plt.show()

    def tegn_nedbør_skydekke_sma(self):
        """
        Lager en statisk graf som viser 7-dagers glidende gjennomsnitt for nedbør og skydekke.
        Dette gjør det enklere å se trender over tid ved å glatte ut daglige variasjoner.
        """

        # Lager to nye kolonner med glidende gjennomsnitt (SMA = Simple Moving Average)
        self.df['Nedbør SMA'] = self.df['Nedbør (mm)'].rolling(window=7).mean()
        self.df['Skydekke SMA'] = self.df['Skydekke (oktas)'].rolling(window=7).mean()

        # Starter figur og første y-akse (for nedbør)
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # Plotter nedbør som 7-dagers glidende gjennomsnitt
        sns.lineplot(data=self.df, x='Dato', y='Nedbør SMA', ax=ax1,
                     color='skyblue', label="Nedbør (7-dagers snitt)")

        ax1.set_ylabel("Nedbør (mm)", color='skyblue')
        ax1.tick_params(axis='y', labelcolor='skyblue')

        # Lager ny y-akse for skydekke
        ax2 = ax1.twinx()
        sns.lineplot(data=self.df, x='Dato', y='Skydekke SMA', ax=ax2,
                     color='gray', label="Skydekke (7-dagers snitt)", linewidth=2)

        ax2.set_ylabel("Skydekke (oktas)", color='gray')
        ax2.tick_params(axis='y', labelcolor='gray')

        # Legger til tittel og formaterer x-aksen
        plt.title("Glidende gjennomsnitt: Nedbør og Skydekke over tid")
        fig.autofmt_xdate()
        fig.tight_layout()

        # Legger til separate legender for hver akse
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        # Viser figuren
        plt.show()

    def tegn_temp_vs_fuktighet(self):
        """
        Lager et scatterplot (punktsky) med en regresjonslinje som viser sammenhengen
        mellom temperatur og relativ fuktighet.
        """

        plt.figure(figsize=(8, 6))  # Oppretter figur med passende størrelse

        # Bruker Seaborn til å lage scatterplot med automatisk regresjonslinje
        sns.regplot(data=self.df, x='Temperatur (°C)', y='Relativ fuktighet (%)',
                    scatter_kws={'alpha': 0.6},  # Gjør punktene litt gjennomsiktige
                    line_kws={'color': 'red'})  # Gjør regresjonslinjen tydelig rød

        # Setter tittel og akseetiketter
        plt.title("Sammenheng mellom temperatur og relativ fuktighet")
        plt.xlabel("Temperatur (°C)")
        plt.ylabel("Relativ fuktighet (%)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def tegn_interaktiv_temp_lufttrykk_plotly(self):
        """
        Lager en interaktiv linjegraf som viser både temperatur og lufttrykk over tid.
        Bruker to y-akser og Plotly for zoom, hover-effekter og interaktivitet.
        """

        fig = go.Figure()  # Oppretter tom figur

        # Legger til temperatur som rød linje
        fig.add_trace(go.Scatter(
            x=self.df['Dato'], y=self.df['Temperatur (°C)'],
            mode='lines+markers', name='Temperatur (°C)',
            line=dict(color='red')
        ))

        # Legger til lufttrykk som blå linje, koblet til y2 (høyre y-akse)
        fig.add_trace(go.Scatter(
            x=self.df['Dato'], y=self.df['Lufttrykk (hPa)'],
            mode='lines+markers', name='Lufttrykk (hPa)',
            line=dict(color='blue'), yaxis='y2'
        ))

        # Oppdaterer layout med to y-akser og hover-effekt
        fig.update_layout(
            title="Interaktiv graf: Temperatur og Lufttrykk over tid",
            xaxis=dict(title="Dato"),
            yaxis=dict(
                title=dict(text="Temperatur (°C)", font=dict(color="red")),
                tickfont=dict(color="red")
            ),
            yaxis2=dict(
                title=dict(text="Lufttrykk (hPa)", font=dict(color="blue")),
                tickfont=dict(color="blue"),
                overlaying="y",
                side="right"
            ),
            legend=dict(x=0.01, y=0.99),
            hovermode="x unified"  # Gjør hover-informasjon synlig for begge y-verdier samtidig
        )

        fig.show()

    def tegn_korrelasjonsheatmap(self):
        """
        Beregner og visualiserer korrelasjon mellom alle numeriske variabler i datasettet.
        Korrelasjon beskriver hvor sterkt to variabler henger sammen.
        """

        # Filtrerer ut alle kolonner med numerisk datatype (float, int)
        numeriske_kolonner = self.df.select_dtypes(include='number')

        # Lager korrelasjonsmatrise – et tabellformat som viser samvariasjon mellom alle kombinasjoner
        korrelasjon = numeriske_kolonner.corr()

        plt.figure(figsize=(10, 6))

        # Tegner et fargekart (heatmap) med verdier annotert og farge etter styrke
        sns.heatmap(korrelasjon, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Korrelasjonsheatmap for miljødata")
        plt.tight_layout()
        plt.show()

    def tegn_interaktiv_variabelvelger(self):
        """
        Lager en interaktiv graf der brukeren kan velge én værvariabel av gangen fra en meny.
        """

        variabler = ['Temperatur (°C)', 'Lufttrykk (hPa)', 'Nedbør (mm)',
                     'Relativ fuktighet (%)', 'Skydekke (oktas)']

        fig = go.Figure()

        # Legger til én trace for hver variabel, men viser bare den første som standard
        for i, var in enumerate(variabler):
            fig.add_trace(go.Scatter(
                x=self.df['Dato'], y=self.df[var],
                mode='lines+markers',
                name=var,
                visible=(i == 0)  # Bare første linje vises, resten skjules
            ))

        # Lager knapper som lar brukeren velge hvilken variabel som vises
        buttons = [
            dict(label=var,
                 method='update',
                 args=[{'visible': [j == i for j in range(len(variabler))]},
                       {'title': f"{var} over tid"}])
            for i, var in enumerate(variabler)
        ]

        fig.update_layout(
            updatemenus=[dict(
                active=0,  # Første knapp valgt som standard
                buttons=buttons,
                x=0.1, xanchor="left",
                y=1.1, yanchor="top"
            )],
            title=f"{variabler[0]} over tid",
            xaxis_title="Dato",
            yaxis_title="Verdi",
            hovermode="x unified"
        )

        fig.show()

    def tegn_interaktiv_boblegraf(self):
        """
        Lager et interaktivt scatterplot (boblegraf) der:
        - X-akse er temperatur
        - Y-akse er lufttrykk
        - Farge viser relativ fuktighet
        - Størrelse på bobler viser nedbørsmengde
        """

        fig = px.scatter(
            self.df,
            x='Temperatur (°C)',
            y='Lufttrykk (hPa)',
            color='Relativ fuktighet (%)',
            size='Nedbør (mm)',
            hover_data=['Dato'],  # Viser dato ved hover
            color_continuous_scale='Viridis',
            title='Temperatur vs Lufttrykk – farget etter relativ fuktighet'
        )

        fig.update_layout(
            xaxis_title='Temperatur (°C)',
            yaxis_title='Lufttrykk (hPa)',
            coloraxis_colorbar=dict(title='Relativ fuktighet (%)')
        )

        fig.show()
