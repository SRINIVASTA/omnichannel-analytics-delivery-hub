import numpy as np
import statsmodels.api as sm

class PriceElasticityEngine:
    @staticmethod
    def calculate_elasticity(df):
        log_q = np.log(df["Sales"])
        log_p = np.log(df["Price"])
        X = sm.add_constant(log_p)
        model = sm.OLS(log_q, X).fit()
        return float(model.params.iloc[1])
