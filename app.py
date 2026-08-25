import streamlit as st
import plotly.express as px
import os

# Import components directly out of your repository tree!
from src.data.snowflake_io import SnowflakeDataPipeline
from src.models.forecasting import DemandForecaster
from src.models.pricing_strategy import PriceElasticityEngine
from src.models.marketing_mix import MarketingMixModel
from src.models.omnichannel import OmnichannelMarkovAttribution
from tests.test_data_validation import DataValidator
from src.pipeline.databricks_orchestration import run_production_pipeline

st.set_page_config(page_title="Enterprise Solutions Delivery Hub", layout="wide")

st.title("🛡️ Enterprise Decision Intelligence: Solutions, Delivery & Governance Hub")
st.caption("Production Pipeline Deployment Engine for CPG, Retail, and Healthcare Analytics")
st.write("---")

# Pull live numbers out of database module
df_raw = SnowflakeDataPipeline.extract_features()

# Structure the Streamlit Hub tabs
tab1, tab2, tab3 = st.tabs(["🔎 1. Solution & Scoping Matrix", "📊 2. Production Algorithmic Engines", "⚡ 3. Enterprise Infrastructure Deployments"])

# ================= TAB 1: SOLUTION SCOPING =================
with tab1:
    st.subheader("💡 Business Requirement Translation")
    
    # Read scope file directly from disk
    if os.path.exists("docs/client_scoping_v1.md"):
        with open("docs/client_scoping_v1.md", "r") as f:
            st.markdown(f.read())

# ================= TAB 2: ALGORITHMIC ENGINES =================
with tab2:
    st.subheader("⚙️ Multi-Engine Modeling Results")
    
    # Run tests module live
    st.markdown("##### 🧪 Active Pipeline Unit Health Checkups")
    for log in DataValidator.run_checks(df_raw):
        st.write(log)
    st.write("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Demand Forecasting Model Outputs")
        forecaster = DemandForecaster()
        forecasted_df = forecaster.fit_predict(df_raw)
        
        fig = px.line(forecasted_df, x="Date", y=["Sales", "Predicted_Sales"],
                      color_discrete_sequence=["#007A87", "#EF553B"])
        st.plotly_chart(fig, use_container_width=True)
        
        # Download button layer
        csv_data = forecasted_df.to_csv(index=False).encode('utf-8')
        st.download_button(label="💾 Download Calculated Predictions CSV", data=csv_data, file_name="predictions.csv", mime="text/csv")
        
    with c2:
        st.markdown("#### Price Elasticity Coefficient")
        elasticity = PriceElasticityEngine.calculate_elasticity(df_raw)
        st.metric("OLS Log-Log Coefficient", f"{elasticity:.3f}")
        
        st.markdown("#### Marketing Attribution Impacts (MMM)")
        st.json(MarketingMixModel.calculate_lift(df_raw))
        
        st.markdown("#### Omnichannel Customer Paths (Markov Chain)")
        st.json(OmnichannelMarkovAttribution.calculate_paths())

# ================= TAB 3: ENTERPRISE INFRASTRUCTURE =================
with tab3:
    st.subheader("💻 Cloud Environment Target Staging")
    stack = st.radio("Select Target Infrastructure Platform Engine:", ["Microsoft Fabric Engine", "Snowflake Snowpark Layer", "Databricks Workspace"])
    
    if st.button("🚀 Push Live Model Inferences to Production Cluster"):
        with st.spinner("Uploading artifacts..."):
            status_message = run_production_pipeline(stack)
            st.success(f"🎉 Deployment Complete: {status_message}")
