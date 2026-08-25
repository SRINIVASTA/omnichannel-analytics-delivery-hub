import numpy as np
import pandas as pd

class SnowflakeDataPipeline:
    @staticmethod
    def extract_features():
        """Simulates production extraction directly out of data warehouse tables."""
        np.random.seed(42)
        dates = pd.date_range(start="2026-01-01", periods=100)
        prices = np.random.uniform(19.99, 49.99, size=100)
        tv_spend = np.random.uniform(200, 1000, size=100)
        digital_spend = np.random.uniform(100, 800, size=100)
        
        sales = (600 - (10 * prices) + (0.2 * tv_spend) + (0.5 * digital_spend) + np.random.normal(0, 25, 100))
        sales = np.clip(sales, 10, None).astype(int)
        
        return pd.DataFrame({"Date": dates, "Price": prices, "TV_Spend": tv_spend, "Digital_Spend": digital_spend, "Sales": sales})
