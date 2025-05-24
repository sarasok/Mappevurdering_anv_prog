# src/analyse.py

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib


def tren_modell(df, features, target):
    """Trener en lineær regresjonsmodell."""
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    modell = LinearRegression()
    modell.fit(X_train_scaled, y_train)

    y_pred = modell.predict(X_test_scaled)
    metrics = {
        "mse": mean_squared_error(y_test, y_pred),
        "r2": r2_score(y_test, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
    }

    return modell, scaler, metrics, X_test, y_test, y_pred


def lagre_modell(modell, scaler, modell_fil="modell.pkl", scaler_fil="scaler.pkl"):
    joblib.dump(modell, modell_fil)
    joblib.dump(scaler, scaler_fil)


def bør_ta_med_paraply(skydekke, fuktighet):
    """Gir en anbefaling basert på predikert skydekke og fuktighet."""
    if skydekke > 6 and fuktighet > 80:
        return "Ta med paraply!"
    elif skydekke > 4:
        return "Kanskje grått, men ikke sikkert du trenger paraply."
    else:
        return "Ingen grunn til paraply, nyt sola!"
