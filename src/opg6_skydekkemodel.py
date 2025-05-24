import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import matplotlib.pyplot as plt

class SkydekkePredictor:
    def __init__(self, df):
        self.df = df
        self.model = LinearRegression()
        self.scaler = StandardScaler()

    def forbered_data(self):
        X = self.df[["Temperatur (°C)", "Lufttrykk (hPa)", "Relativ fuktighet (%)"]]
        y = self.df["Skydekke (oktas)"]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def tren_og_evaluer(self):
        X_train, X_test, y_train, y_test = self.forbered_data()

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        self.model.fit(X_train_scaled, y_train)
        y_pred = self.model.predict(X_test_scaled)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mse)

        print(f"MSE: {mse:.2f}")
        print(f"R²: {r2:.2f}")
        print(f"RMSE: {rmse:.2f}")

        self.visualiser(y_test, y_pred)

        return self.model, self.scaler

    def visualiser(self, y_test, y_pred):
        plt.figure(figsize=(10, 5))
        plt.plot(y_test.values, label="Faktisk", marker='o')
        plt.plot(y_pred, label="Predikert", marker='x')
        plt.title("Faktisk vs. Predikert Skydekke")
        plt.xlabel("Observasjoner")
        plt.ylabel("Skydekke (oktas)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def lagre_modell(self, modell_path="modell_skydekke.pkl", scaler_path="scaler_skydekke.pkl"):
        joblib.dump(self.model, modell_path)
        joblib.dump(self.scaler, scaler_path)
