# src/visualisering.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class PollutionVisualizer:
    @staticmethod
    def plot_interpolation(df_original, df_filled, kolonne, start_dato, slutt_dato):
        original = df_original.loc[start_dato:slutt_dato]
        interpolert = df_filled.loc[start_dato:slutt_dato]

        mangler = df_original[kolonne].isna()
        interpolerte_datoer = df_original[mangler].loc[start_dato:slutt_dato].index

        plt.figure(figsize=(10, 5))

        plt.plot(original.index, original[kolonne], label="Før interpolering", color='red', marker='o', alpha=0.6)
        plt.plot(interpolert.index, interpolert[kolonne], label="Etter interpolering", linestyle=':', color='steelblue', linewidth=2)
        plt.scatter(interpolerte_datoer, df_filled.loc[interpolerte_datoer, kolonne],
                    color='green', label="Interpolerte verdier", zorder=5)
        plt.title(f"Interpolering i '{kolonne}' fra {start_dato} til {slutt_dato}")
        plt.xlabel("Dato")
        plt.ylabel(kolonne.upper())
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_ukentlig_no2(weekly_no2, weekly_no2_clean):
        import matplotlib.pyplot as plt

        plt.figure(figsize=(14, 6))
        plt.plot(weekly_no2, label="Med hull", linestyle="--", alpha=0.6)
        plt.plot(weekly_no2_clean, label="Interpolert og renset", color="orange", linewidth=2)

        plt.title("Interpolasjon og rensing av NO2-data på ukesnivå")
        plt.xlabel("Uke")
        plt.ylabel("NO2 (µg/m³)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    @staticmethod
    def plot_no2_ukentlig_barplot(weekly_no2_clean):
        tick_labels = weekly_no2_clean.index.to_period("W").strftime("Uke %W\n%Y")

        figur_no2, akse_no2 = plt.subplots(figsize=(14, 6))
        weekly_no2_clean.plot(kind="bar", color="skyblue", ax=akse_no2)

        akse_no2.set_title("Gjennomsnittlig NO₂ per uke (uten uteliggere)")
        akse_no2.set_ylabel("NO₂ (µg/m³)")
        akse_no2.set_xlabel("Uke")
        akse_no2.set_xticks(range(0, len(weekly_no2_clean), 6))
        akse_no2.set_xticklabels(tick_labels[::6], rotation=0, ha='center')

        figur_no2.tight_layout()
        plt.show()



    @staticmethod
    def vis_korrelasjonsmatrise(df: pd.DataFrame):
        """Viser korrelasjonsmatrise for numeriske variabler."""
        numeric_df = df.select_dtypes(include=["number"])
        corr_matrix = numeric_df.corr()

        plt.figure(figsize=(10, 6))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Korrelasjon mellom vær og luftkvalitetsvariabler", fontsize=15, weight='bold')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plott_skydekke_fuktighet(df: pd.DataFrame):
        """Lager linjediagram med dobbel y-akse for skydekke og fuktighet."""
        df["Skydekke_smooth"] = df["Skydekke (oktas)"].rolling(window=7).mean()
        df["Fuktighet_smooth"] = df["Relativ fuktighet (%)"].rolling(window=7).mean()

        sns.set(style="whitegrid")
        fig, ax1 = plt.subplots(figsize=(14, 6))

        line1 = sns.lineplot(data=df, x="date", y="Fuktighet_smooth", ax=ax1, color="forestgreen")
        ax1.set_ylabel("Relativ fuktighet (%)", color="forestgreen")
        ax1.tick_params(axis='y', labelcolor="forestgreen")

        ax2 = ax1.twinx()
        line2 = sns.lineplot(data=df, x="date", y="Skydekke_smooth", ax=ax2, color="navy")
        ax2.set_ylabel("Skydekke (oktas)", color="navy")
        ax2.tick_params(axis='y', labelcolor="navy")

        ax1.legend(["Relativ fuktighet"], loc="upper left")
        ax2.legend(["Skydekke"], loc="upper right")

        plt.title("Skydekke og relativ luftfuktighet i 2024 (glattet)", fontsize=14)
        fig.tight_layout()
        plt.show()
