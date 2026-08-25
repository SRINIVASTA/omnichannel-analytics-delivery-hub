import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class DemandForecaster:
    def __init__(self, n_estimators=50):
        self.model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)

    def fit_predict(self, df):
        data = df.copy()
        data["Lag_1"] = data["Sales"].shift(1)
        data["Lag_2"] = data["Sales"].shift(2)
        data = data.dropna()
        
        X = data[["Lag_1", "Lag_2", "Price"]]
        y = data["Sales"]
        self.model.fit(X, y)
        data["Predicted_Sales"] = self.model.predict(X).astype(int)
        return data
