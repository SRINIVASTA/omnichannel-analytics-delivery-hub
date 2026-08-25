from sklearn.linear_model import Ridge

class MarketingMixModel:
    @staticmethod
    def calculate_lift(df):
        X = df[["TV_Spend", "Digital_Spend"]]
        y = df["Sales"]
        model = Ridge(alpha=1.0, positive=True)
        model.fit(X, y)
        return {"TV Ad Multiplier": float(model.coef_[0]), "Digital Ad Multiplier": float(model.coef_[1])}
