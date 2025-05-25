import numpy as np
import matplotlib.pyplot as plt
import joblib

# Importer verktøy fra scikit-learn (sklearn) som brukes i maskinlæringsprosessen
from sklearn.linear_model import LinearRegression # Selve maskinlæringsmodellen
from sklearn.metrics import mean_squared_error, r2_score # For å måle hvor god modellen er
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Definer en klasse som skal trene og bruke en prediktiv modell for skydekke
class SkydekkePredictor:
    def __init__(self, df):
        # Tar inn datasettet og lager plass for modell og standardisering
        self.df = df
        self.model = LinearRegression() # velger å bruke en lineær regresjonsmodell
        self.scaler = StandardScaler() # bruker standardisering for å gjøre variablene sammenlignbare

    def forbered_data(self):
        # Velger ut input-variablene og målet vi vil predikere
        X = self.df[["Temperatur (°C)", "Lufttrykk (hPa)", "Relativ fuktighet (%)"]]
        y = self.df["Skydekke (oktas)"]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def tren_og_evaluer(self):
        # Forbered data og del opp i tren/test
        X_train, X_test, y_train, y_test = self.forbered_data()

        # Standardiser input-variablene (mean = 0, std = 1)
        # Dette hjelper modellen å trene jevnere og gir bedre resultater
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Tren modellen på treningsdata
        self.model.fit(X_train_scaled, y_train)
        # Bruk modellen til å forutsi verdier basert på testdataene
        y_pred = self.model.predict(X_test_scaled)

        # Beregn tre vanlige ytelsesmål:
        mse = mean_squared_error(y_test, y_pred) # Gjennomsnittlig kvadratisk feil
        r2 = r2_score(y_test, y_pred) # Forklaringsgrad 
        rmse = np.sqrt(mse) # Kvadratroten av MSE – lettere å forstå siden den er på samme skala

        print(f"MSE: {mse:.2f}")
        print(f"R²: {r2:.2f}")
        print(f"RMSE: {rmse:.2f}")

        # Vis graf som sammenligner predikert og faktisk skydekke
        self.visualiser(y_test, y_pred)

        return self.model, self.scaler

    # Lager en graf som viser faktisk vs. predikert skydekke
    # Dette gjør det lettere å se om modellen treffer godt eller bommer
    def visualiser(self, y_test, y_pred):
        plt.figure(figsize=(10, 5))
        plt.plot(y_test.values, label="Faktisk", marker='o') # Faktiske verdier
        plt.plot(y_pred, label="Predikert", marker='x') # Modellens forutsigelser
        plt.title("Faktisk vs. Predikert Skydekke")
        plt.xlabel("Observasjoner")
        plt.ylabel("Skydekke (oktas)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def lagre_modell(self, modell_path="modell_skydekke.pkl", scaler_path="scaler_skydekke.pkl"):
        # Lagrer både den trente modellen og standardiseringen til filer
        # Slik kan vi bruke modellen senere uten å måtte trene den på nytt
        joblib.dump(self.model, modell_path)
        joblib.dump(self.scaler, scaler_path)
