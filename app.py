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
    """)

    # Dictionary of user groups with descriptions
    user_groups = {
    "Recreational Users (Swimmers, Paddlers, Boaters)": """
        - **Purpose**: Understand if water quality conditions are safe for activities like swimming, kayaking, or boating.
        - **How to Use**: Check safety indicators and predictions to see if the water quality meets safe standards for recreational activities.
        - **Where to Go**: Go to the [Water Quality Trends](#) page and check the [current water quality dashboard](#).
    """,
    "Local Residents": """
        - **Purpose**: Track water quality trends to understand potential health risks and environmental changes in their community.
        - **How to Use**: Check historical and real-time data for changes in water quality that could affect health.
        - **Where to Go**: Go to the [Pollution Insights](#) page for pollutant tracking and trend analysis.
    """,
    "Environmental Conservation Groups": """
        - **Purpose**: Use water quality data to advocate for cleaner rivers, detect pollution patterns, and identify opportunities for intervention.
        - **How to Use**: Check pollution sources and use the trends for awareness campaigns.
        - **Where to Go**: Visit the [Pollution Insights](#) and [Water Quality Trends](#) pages for detailed analysis.
    """,
    "Agricultural and Irrigation Planners": """
        - **Purpose**: Ensure that river water quality meets standards for safe agricultural use, which can impact crop safety and irrigation strategies.
        - **How to Use**: Check pollutant levels and seasonal data for better irrigation planning.
        - **Where to Go**: Visit the [Pollution Insights](#) page for detailed pollutant data.
    """,
    "Scientists and Researchers": """
        - **Purpose**: Analyze long-term water quality data to conduct studies on pollution, ecosystem health, and climate impacts.
        - **How to Use**: Use long-term data to conduct research and build predictive models.
        - **Where to Go**: Check out the [Water Quality Trends](#) page for historical data and the [Forecast & Predictions](#) page for predictions.
    """,
    "Public Health Officials": """
        - **Purpose**: Monitor water quality as part of public health assessments, particularly regarding exposure risks from pollutants or pathogens.
        - **How to Use**: Monitor alerts and trends to issue public health advisories.
        - **Where to Go**: Go to the [Safety Indicators](#) page for health-related alerts.
    """,
    "Policy Makers and Urban Planners": """
        - **Purpose**: Use data to support water management policies, regulations, and development plans, aiming to reduce pollution and improve water access.
        - **How to Use**: Use historical and predictive data to develop and enforce water management policies.
        - **Where to Go**: Visit the [Forecast & Predictions](#) page for long-term forecasts and regulatory insights.
    """
}

    # Display user guide sections
    for group, description in user_groups.items():
        st.markdown(f"**{group}**")
        st.markdown(description)

    # Getting Started Guide Section
    st.header("Getting Started Guide")
    st.markdown("""
        Follow the steps below to begin exploring the water quality data and insights in Hydrovibe.
        1. *Select your user group* from the list above to understand how the app can serve your needs.
        2. *Navigate to the relevant pages* based on your interests:
            - *Water Quality Trends*: Check current and historical water quality data.
            - *Pollution Insights*: View trends and insights about pollution levels and their effects.
            - *Safety Indicators*: Check real-time water quality safety for recreational activities.
            - *Forecast & Predictions*: Get predictions for future water quality trends and events.
    """)

    st.write("Now, explore the app and make informed decisions about river water quality!")

# Other pages
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
    """)

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
    """)

def safety_indicators():
    st.title('Safety Indicators')
    st.markdown("""
        ### Insights & Recommendations:
        - Track safety levels based on water quality data, including algae blooms and toxins.
        - Check alerts for swimmers, fishers, and others engaging in water-related activities.
        
        #### Recommendations:
        - Ensure safety by staying updated on water quality alerts in your area.
        - For swimmers, be aware of toxins that could affect your health.
    """)

def forecast_predictions():
    st.title('Forecast & Predictions')
    st.markdown("""
        ### Insights & Recommendations:
        - Get forecasts of water quality and pollutant levels based on real-time data and historical trends.
        - Receive predictive insights into the future health of river ecosystems.
        
        #### Recommendations:
        - Use the forecast data to plan activities around the river and avoid areas with poor water quality.
        - Environmentalists can leverage predictions for long-term planning.
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

if __name__ == "__main__":
    main()
