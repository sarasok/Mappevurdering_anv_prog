# src/databehandling.py

import pandas as pd

class Databehandling:
    @staticmethod
    def resample_og_interpoler(df_luft):
        if "Dato" in df_luft.columns:
            df_luft.rename(columns={"Dato": "date"}, inplace=True)
        df_luft["date"] = pd.to_datetime(df_luft["date"])
        df_luft.set_index("date", inplace=True)
        df_luft_daily = df_luft.resample("D").mean()
        df_luft_fylt = df_luft_daily.interpolate(method="linear")

        print("Antall manglende verdier før interpolering:")
        print(df_luft_daily.isna().sum())
        print("\nAntall manglende verdier etter interpolering:")
        print(df_luft_fylt.isna().sum())

        return df_luft_daily, df_luft_fylt

    @staticmethod
    def les_og_forbered_data(fil_klima: str, fil_luft: str):
        # Les inn datasett
        df = pd.read_csv("../data/R_Sammenslaaing_uten_feil.csv")
        df_luft = pd.read_csv("../data/R_luftkvalitet.csv")
        # Konverter og sørg for at begge har kolonnen "date"
        df = df.rename(columns={"Dato": "date"})
        df["date"] = pd.to_datetime(df["date"])
        df_luft["date"] = pd.to_datetime(df_luft["date"])

        return df, df_luft




    @staticmethod
    def sjekk_manglende_data(df: pd.DataFrame, df_luft: pd.DataFrame):
        """Returnerer manglende verdier og antall rader."""
        return {
            "missing_df": df.isnull().sum(),
            "missing_df_luft": df_luft.isnull().sum(),
            "len_df": len(df),
            "len_df_luft": len(df_luft)
        }

    @staticmethod
    def fjern_iqr_outliers(serie):
        """
        Fjerner outliers fra en tidsserie basert på IQR-metoden.
        """
        Q1 = serie.quantile(0.25)
        Q3 = serie.quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        return serie[(serie >= lower_bound) & (serie <= upper_bound)]


    def finn_manglende_datoer(df: pd.DataFrame, df_luft: pd.DataFrame):
        """Finn datoer som mangler i ett av datasett."""
        mangler_i_luft = df[~df["date"].isin(df_luft["date"])]
        mangler_i_df = df_luft[~df_luft["date"].isin(df["date"])]
        return mangler_i_luft["date"].tolist(), mangler_i_df["date"].tolist()

    def fjern_outliers(df: pd.DataFrame, kolonne: str, øvre_grense: float):
        """Fjerner outliers basert på øvre grense."""
        return df[df[kolonne] <= øvre_grense]

    def slå_sammen_data(df: pd.DataFrame, df_luft: pd.DataFrame):
        """Slår sammen vær- og luftkvalitetsdata på dato."""
        return pd.merge(df, df_luft, on="date", how="inner")

    def tilbakestill_indeks(df: pd.DataFrame):
        """Tilbakestiller indeksen og returnerer DataFrame med 'date' som kolonne."""
        return df.reset_index()
