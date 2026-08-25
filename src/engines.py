import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
import statsmodels.api as sm
from collections import defaultdict

class CoreDataScienceSuite:
    @staticmethod
    def generate_synthetic_data():
        """Generates real-time mock data arrays inside memory context."""
        np.random.seed(42)
        dates = pd.date_range(start="2026-01-01", periods=100)
        prices = np.random.uniform(19.99, 49.99, size=100)
        tv_spend = np.random.uniform(200, 1000, size=100)
        digital_spend = np.random.uniform(100, 800, size=100)
        
        # Structural economic formula: baseline minus price plus marketing boost
        sales = (600 - (10 * prices) + (0.2 * tv_spend) + (0.5 * digital_spend) + np.random.normal(0, 25, 100))
        sales = np.clip(sales, 10, None).astype(int)
        
        return pd.DataFrame({"Date": dates, "Price": prices, "TV_Spend": tv_spend, "Digital_Spend": digital_spend, "Sales": sales})

    @staticmethod
    def run_forecasting(df):
        """1. Forecasting via Random Forest Regressor Lag Models"""
        data = df.copy()
        data["Lag_1"] = data["Sales"].shift(1)
        data["Lag_2"] = data["Sales"].shift(2)
        data = data.dropna()
        
        X = data[["Lag_1", "Lag_2", "Price"]]
        y = data["Sales"]
        
        model = RandomForestRegressor(n_estimators=50, random_state=42)
        model.fit(X, y)
        data["Predicted_Sales"] = model.predict(X).astype(int)
        return data

    @staticmethod
    def run_pricing(df):
        """2. Pricing Strategy via Log-Log Elasticity Analytics"""
        log_q = np.log(df["Sales"])
        log_p = np.log(df["Price"])
        X = sm.add_constant(log_p)
        model = sm.OLS(log_q, X).fit()
        return float(model.params.iloc[1])

    @staticmethod
    def run_mmm(df):
        """3. Marketing Mix Modeling (MMM) via Non-Negative Ridge"""
        X = df[["TV_Spend", "Digital_Spend"]]
        y = df["Sales"]
        model = Ridge(alpha=1.0, positive=True)
        model.fit(X, y)
        return {"TV Channel Impact": float(model.coef_[0]), "Digital Channel Impact": float(model.coef_[1])}

    @staticmethod
    def run_omnichannel():
        """4. Omnichannel Pathing via Markov Chains transition state logic"""
        sample_journeys = [["Paid Ad", "Web Search", "In-Store Buy"], ["Web Search", "Bounce"], ["Paid Ad", "In-Store Buy"]]
        transitions = defaultdict(lambda: defaultdict(float))
        
        for journey in sample_journeys:
            for i in range(len(journey) - 1):
                transitions[journey[i]][journey[i+1]] += 1.0
                
        prob_map = {}
        for state, trans in transitions.items():
            total = sum(trans.values())
            prob_map[state] = {k: v / total for k, v in trans.items()}
        return prob_map
