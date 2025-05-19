import pandas as pd  # For databehandling
import matplotlib.pyplot as plt  # For plotting
import seaborn as sns  # For visuelt ryddige grafer
import plotly.graph_objects as go
import plotly.express as px  # For rask og interaktiv visualisering

class VærDataPlotter:
    def __init__(self, filsti):
        self.df = pd.read_csv(filsti)
        self.df['Dato'] = pd.to_datetime(self.df['Dato'])
        sns.set_theme(style="whitegrid")

    def tegn_temp_lufttrykk_matplotlib(self):
        """
        Linjediagram med temperatur og lufttrykk over tid (matplotlib/seaborn).
        """
        fig, ax1 = plt.subplots(figsize=(12, 6))

        sns.lineplot(data=self.df, x='Dato', y='Temperatur (°C)', ax=ax1,
                     label="Temperatur (°C)", color='tab:red')
        ax1.set_ylabel("Temperatur (°C)", color='tab:red')
        ax1.tick_params(axis='y', labelcolor='tab:red')

        ax2 = ax1.twinx()
        sns.lineplot(data=self.df, x='Dato', y='Lufttrykk (hPa)', ax=ax2,
                     label="Lufttrykk (hPa)", color='tab:blue')
        ax2.set_ylabel("Lufttrykk (hPa)", color='tab:blue')
        ax2.tick_params(axis='y', labelcolor='tab:blue')

        plt.title("Temperatur og Lufttrykk over tid")
        fig.autofmt_xdate()
        fig.tight_layout()
        plt.show()

    def tegn_nedbør_skydekke_sma(self):
        """
        Plotter 7-dagers glidende gjennomsnitt for nedbør og skydekke.
        """
        self.df['Nedbør SMA'] = self.df['Nedbør (mm)'].rolling(window=7).mean()
        self.df['Skydekke SMA'] = self.df['Skydekke (oktas)'].rolling(window=7).mean()

        fig, ax1 = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=self.df, x='Dato', y='Nedbør SMA', ax=ax1,
                     color='skyblue', label="Nedbør (7-dagers snitt)")
        ax1.set_ylabel("Nedbør (mm)", color='skyblue')
        ax1.tick_params(axis='y', labelcolor='skyblue')

        ax2 = ax1.twinx()
        sns.lineplot(data=self.df, x='Dato', y='Skydekke SMA', ax=ax2,
                     color='gray', label="Skydekke (7-dagers snitt)", linewidth=2)
        ax2.set_ylabel("Skydekke (oktas)", color='gray')
        ax2.tick_params(axis='y', labelcolor='gray')

        plt.title("Glidende gjennomsnitt: Nedbør og Skydekke over tid")
        fig.autofmt_xdate()
        fig.tight_layout()
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')
        plt.show()

    def tegn_temp_vs_fuktighet(self):
        """
        Scatterplot med regresjonslinje mellom temperatur og relativ fuktighet.
        """
        plt.figure(figsize=(8, 6))
        sns.regplot(data=self.df, x='Temperatur (°C)', y='Relativ fuktighet (%)',
                    scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})

        plt.title("Sammenheng mellom temperatur og relativ fuktighet")
        plt.xlabel("Temperatur (°C)")
        plt.ylabel("Relativ fuktighet (%)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def tegn_interaktiv_temp_lufttrykk_plotly(self):
        """
        Interaktiv linjegraf med temperatur og lufttrykk med to y-akser (Plotly).
        """
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=self.df['Dato'], y=self.df['Temperatur (°C)'],
            mode='lines+markers', name='Temperatur (°C)',
            line=dict(color='red')
        ))

        fig.add_trace(go.Scatter(
            x=self.df['Dato'], y=self.df['Lufttrykk (hPa)'],
            mode='lines+markers', name='Lufttrykk (hPa)',
            line=dict(color='blue'), yaxis='y2'
        ))

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
            hovermode="x unified"
        )

        fig.show()

    def tegn_korrelasjonsheatmap(self):
        """
        Lager et heatmap som viser korrelasjon mellom alle numeriske variabler.
        """
        numeriske_kolonner = self.df.select_dtypes(include='number')
        korrelasjon = numeriske_kolonner.corr()

        plt.figure(figsize=(10, 6))
        sns.heatmap(korrelasjon, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Korrelasjonsheatmap for miljødata")
        plt.tight_layout()
        plt.show()

    def tegn_interaktiv_variabelvelger(self):
        """
        Lager en interaktiv dropdown-figur for å vise én værvariabel om gangen.
        """
        variabler = ['Temperatur (°C)', 'Lufttrykk (hPa)', 'Nedbør (mm)',
                     'Relativ fuktighet (%)', 'Skydekke (oktas)']

        fig = go.Figure()

        for i, var in enumerate(variabler):
            fig.add_trace(go.Scatter(
                x=self.df['Dato'], y=self.df[var],
                mode='lines+markers',
                name=var,
                visible=(i == 0)
            ))

        buttons = [
            dict(label=var,
                 method='update',
                 args=[{'visible': [j == i for j in range(len(variabler))]},
                       {'title': f"{var} over tid"}])
            for i, var in enumerate(variabler)
        ]

        fig.update_layout(
            updatemenus=[dict(
                active=0,
                buttons=buttons,
                x=0.1,
                xanchor="left",
                y=1.1,
                yanchor="top"
            )],
            title=f"{variabler[0]} over tid",
            xaxis_title="Dato",
            yaxis_title="Verdi",
            hovermode="x unified"
        )

        fig.show()

    def tegn_interaktiv_boblegraf(self):
        """
        Lager et interaktivt scatterplot med farge og størrelse basert på flere variabler.
        """
        fig = px.scatter(
            self.df,
            x='Temperatur (°C)',
            y='Lufttrykk (hPa)',
            color='Relativ fuktighet (%)',
            size='Nedbør (mm)',
            hover_data=['Dato'],
            color_continuous_scale='Viridis',
            title='Temperatur vs Lufttrykk – farget etter relativ fuktighet'
        )

        fig.update_layout(
            xaxis_title='Temperatur (°C)',
            yaxis_title='Lufttrykk (hPa)',
            coloraxis_colorbar=dict(title='Relativ fuktighet (%)')
        )

        fig.show()
