import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Dataset, Reader
import pickle
from PIL import Image

# Set up the homepage
def homepage():
    st.title('Welcome to HydroVibe')
    st.markdown("""
        *HydroVibe* is your ultimate tool for monitoring water quality in rivers, providing insights and predictions
        to ensure safety and ecological preservation. Whether you're a swimmer, fisherman, environmentalist, or policy maker,
        this app provides real-time data and future predictions on water quality and pollution levels.

        ### User Guide:
        This app serves multiple user groups. Find your profile below and explore the insights that benefit you:
        
        - *Swimmers*: Stay safe by checking water quality forecasts and pollution alerts.
        - *Fishers*: Plan your fishing trips with insights on water health, safety conditions, and pollution trends.
        - *Environmental Managers*: Analyze water health, pollution sources, and trends, with recommendations to improve water quality.
        - *Government & Policy Makers*: Access regulatory insights and track water quality policies over time.
        - *Tourists & Outdoor Enthusiasts*: Make informed decisions about water-related activities by checking local water conditions.
        - *Researchers & Students*: Dive deep into water quality data, pollution analysis, and environmental impact studies.
        
        ### Getting Started Guide:
        - Start by exploring the homepage for general insights.
        - Navigate to the Water Quality Trends page for real-time data on river health.
        - Use the Pollution Insights page to learn about pollutant sources and forecasts.
        - Visit the Safety Indicators page for alerts on water quality risks.
        - Use the Forecast & Predictions page for water quality forecasts based on current data.

        [Go to Water Quality Trends](#)
        [Go to Pollution Insights](#)
        [Go to Safety Indicators](#)
        [Go to Forecast & Predictions](#)
    """)

# Water Quality Trends Page
def water_quality_trends():
    st.title('Water Quality Trends')
    st.markdown("""
        ### Insights & Recommendations:
        - View historical and real-time data on water quality across various locations.
        - Visualize temporal patterns and seasonal shifts in water quality.
        - Analyze the impact of rainfall, pollution, and human activity on water quality.
        
        #### Recommendations:
        - Pay attention to high pollution areas.
        - Use this page to track improvements or deteriorations in water quality.
        - Compare current data to historical trends for long-term predictions.

        [Go back to Homepage](#)
    """)

# Pollution Insights Page
def pollution_insights():
    st.title('Pollution Insights')
    st.markdown("""
        ### Insights & Recommendations:
        - Understand the sources of pollution affecting the river's health.
        - Visualize pollutants by type and location, and their impact on the ecosystem.
        - Get predictions on pollutant levels and learn ways to mitigate risks.
        
        #### Recommendations:
        - For environmental managers, monitor trends to predict future risks.
        - For local authorities, use the data to develop strategies for pollution control.

        [Go back to Homepage](#)
    """)

# Safety Indicators Page
def safety_indicators():
    st.title('Safety Indicators')
    st.markdown("""
        ### Insights & Recommendations:
        - Track safety levels based on water quality data, including algae blooms and toxins.
        - Check alerts for swimmers, fishers, and others engaging in water-related activities.
        
        #### Recommendations:
        - Ensure safety by staying updated on water quality alerts in your area.
        - For swimmers, be aware of toxins that could affect your health.

        [Go back to Homepage](#)
    """)

# Forecast & Predictions Page
def forecast_predictions():
    st.title('Forecast & Predictions')
    st.markdown("""
        ### Insights & Recommendations:
        - Get forecasts of water quality and pollutant levels based on real-time data and historical trends.
        - Receive predictive insights into the future health of river ecosystems.
        
        #### Recommendations:
        - Use the forecast data to plan activities around the river and avoid areas with poor water quality.
        - Environmentalists can leverage predictions for long-term planning.

        [Go back to Homepage](#)
    """)

# Main function to display all pages
def main():
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Water Quality Trends", "Pollution Insights", "Safety Indicators", "Forecast & Predictions"])

    if page == "Homepage":
        homepage()
    elif page == "Water Quality Trends":
        water_quality_trends()
    elif page == "Pollution Insights":
        pollution_insights()
    elif page == "Safety Indicators":
        safety_indicators()
    elif page == "Forecast & Predictions":
        forecast_predictions()

if _name_ == "_main_":
    main()