# 🛡️ Enterprise Decision Intelligence: Solutions, Delivery & Governance Hub
### Production Pipeline Deployment Engine for CPG, Retail, and Healthcare Analytics
🚀 **Live Application URL:** *[https://omnichannel-analytics-delivery-app-7txetkya8hvkzrwbqgknan.streamlit.app/]*

---

## 💼 Core Business & Job Specification Overview
This repository contains an interactive, production-ready portfolio framework built to address the core delivery requirements of a **Manager of Data Science (Solution and Delivery)**. The framework demonstrates end-to-end management of complex analytics projects: translating loose client briefs into rigorous mathematical models, checking data health, and scaling deployments across multi-cloud enterprise architectures.

### 🌟 Interactive Product Capabilities Demonstrated:
1. **Solution & Scoping Matrix:** Translates open-ended business issues into precise predictive metrics.
2. **Production Algorithmic Engines:** Simulates forecasting, pricing elasticity, and marketing mix tracking.
3. **Enterprise Infrastructure Deployments:** A simulator demonstrating architectural integration with major cloud backends.
4. **Client Advisory Slide-Deck:** Translates statistical metrics into actionable business strategies for leadership.

---

## 📂 Repository Tree Structure
The system uses a clean, production-grade monorepo design, separating configuration arrays, statistical modules, data layers, and documentation maps:

```text
omnichannel-analytics-delivery-hub/
├── .streamlit/
│   └── config.toml           # Corporate UI theme settings (Dark accent UI)
├── config/
│   └── config.yaml           # Global parameters (Lags, Estimators, Learning rules)
├── docs/
│   └── client_scoping_v1.md  # Client translation brief markdown mapping
├── src/
│   ├── __init__.py
│   ├── data/
│   │   └── snowflake_io.py   # Secure data ingestion pipeline & translation layer
│   ├── models/
│   │   ├── forecasting.py    # Time-series Demand Forecaster (Random Forest Lag model)
│   │   ├── pricing_strategy.py# Log-Log Elasticity Optimization engine (OLS Regression)
│   │   ├── marketing_mix.py  # Marketing Mix Modeling engine (Positive Ridge Regression)
│   │   └── omnichannel.py   # Behavioral Journey Pathing engine (Markov Chain transition arrays)
│   └── pipeline/
│       └── databricks_orchestration.py # Core backend pipeline processing simulator
├── tests/
│   └── test_data_validation.py # Unit tests evaluating schema structural bounds
├── app.py                    # Main Multi-Tab Web App UI Orchestrator
└── requirements.txt          # Production-grade open-source package dependencies
```

---

## 📊 Live Business Data & Mathematical Insights
The core models are validated using a real 20-week retail commercial dataset (`real_business_sales.csv`), generating real-time statistical insights:

### 🔎 Automated Pipeline Unit Health Checkups (`tests/`)
Before any math functions execute, the `DataValidator` script evaluates incoming records to shield the models from data corruption:
* **Check 1: Matrix Shape Verification:** Verified column dimensionality and integrity maps.
* **Check 2: Boundary Analysis:** Confirmed ingestion metrics match expected tracking bounds.
* **Check 3: Negative Inversion Guard:** Confirmed zero impossible negative counts are fed into tensors.

### 🏷️ Pricing Sensitivity Optimization Engine (Elasticity: `-2.206`)
* **Mathematical Method:** Ordinary Least Squares (OLS) Log-Log linear model.
* **Business Translation:** An elasticity score of **-2.21** indicates that demand is highly price-sensitive. For every 10% price increase, sales volume falls by **22.1%**.
* **Strategic Directive:** Avoid broad price increases. Instead, execute targeted markdowns to quickly clear excess inventory.

### 📺 Marketing Mix Modeling Attribution (MMM Multipliers)
* **Mathematical Method:** Positive-constrained Ridge Regression tracking media spend against total sales conversions.
* **Calculated Lift Matrix:** `Digital Ad Multiplier: 0.998` | `TV Ad Multiplier: 0.069`
* **Strategic Directive:** Reallocate 35% of underperforming traditional TV capital directly into active digital channels to maximize multi-channel return on ad spend (ROAS).

### 🔄 Omnichannel Behavioral Journey Paths
* **Mathematical Method:** Finite Discrete State-Transition Probability Arrays via Markov Chains.
* **Calculated Pathing:** Customers landing on a *Paid Ad* face a split 50% probability of either looking up a *Web Search* or executing a direct physical *In-Store Buy*. 

---

## ⚡ Enterprise Architecture Cloud Deployments (Showcase Mode)
To demonstrate production-readiness without leaking sensitive credentials or cloud keys, the deployment tab functions as a decoupled **high-fidelity MLOps simulator**.

Selecting an option triggers a mock deployment pipeline, mimicking data staging workflows for three major enterprise platforms:
1. **Microsoft Fabric (OneLake Delta Lake Engine Staging):** Formats files into Parquet/Delta structures for enterprise business intelligence reports.
2. **Snowflake (Snowpark Architecture Layers):** Converts Python models into warehouse procedures using high-throughput Snowpark nodes.
3. **Databricks (Unity Catalog Managed Inferences):** Tracks pipeline runs, feature sets, and metrics using an MLflow tracking service.

*On click, the system performs validation runs and responds with a standard **`200 OK` API success log**, confirming the model pipeline is stable and ready to deploy.*

---

## ⚙️ Environment Setup & Installation Instructions

If you wish to clone this architecture and execute it locally on your computer rather than using the live Streamlit Web Portal:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd omnichannel-analytics-delivery-hub
   ```
2. **Install dependency packages:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the offline Streamlit application server:**
   ```bash
   streamlit run app.py
   ```
