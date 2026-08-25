import streamlit as st

def get_translation_matrix():
    return {
        "Forecasting": {
            "vague": "We don't know how much inventory to stock next quarter.",
            "math": "Estimate conditional distribution P(Y_t+h | Y_:t, X_:t) across supply chain endpoints.",
            "impact": "Reduces storage overhead costs by 14-18% while avoiding stockouts."
        },
        "Pricing Strategy": {
            "vague": "How will changing our pricing affect our bottom line profit?",
            "math": "Estimate Price Elasticity of Demand (dQ/dP * P/Q) via Log-Log Regression analysis.",
            "impact": "Identifies margin-expansion options across highly inelastic product groups."
        },
        "Marketing Mix (MMM)": {
            "vague": "Which marketing channels are actually driving our revenue conversions?",
            "math": "Deconstruct target revenue variable Y into channel coefficients β_i with custom Geometric Adstock Decay.",
            "impact": "Reallocates underperforming ad spend into high-conversion digital tracks."
        },
        "Omnichannel Paths": {
            "vague": "How do our online advertisements directly affect physical offline store visits?",
            "math": "Map pathing transition arrays through discrete multi-state customer journeys using Markov Chains.",
            "impact": "Attributes cross-channel touchpoint values instead of basic last-click bias."
        }
    }

def render_client_deck():
    st.markdown("### 📢 Manager Executive Deck: Presenting to Stakeholders")
    slide = st.radio("Select Presentation Slide:", ["1. The Problem Space", "2. Algorithmic Trade-offs", "3. Strategic Business Value"])
    
    if slide == "1. The Problem Space":
        st.markdown("""
        #### Phase 1: Scoping & Governance
        * **Client Vulnerability:** Siloed channel spending leading to missing margin opportunities.
        * **Our Objective:** Deploy a unified optimization engine to coordinate marketing, pricing, and logistics.
        """)
    elif slide == "2. Algorithmic Trade-offs":
        st.markdown("""
        #### Model Governance Framework
        * **Pros (Parametric Models):** Highly interpretable; direct causality mapping for executive sign-offs (e.g., Elasticity & MMM coefficients).
        * **Cons (Non-Parametric Models):** Tree-based models capture complex nonlinear trends cleanly but function as black boxes (e.g., Demand Forecasting).
        """)
    elif slide == "3. Strategic Business Value":
        st.markdown("""
        #### Hard Financial ROI Targets
        * **Inventory Savings:** Over US\$240k saved yearly in unnecessary warehouse holding fees.
        * **Margin Growth:** 3.4% net margin gain by executing targeted strategic price markdowns.
        """)
