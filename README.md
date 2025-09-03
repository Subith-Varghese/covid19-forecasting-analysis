# COVID-19 Forecasting Project

## Project Overview

This project analyzes and forecasts COVID-19 trends globally using historical case data. It performs:

- Data cleaning & preprocessing
- Exploratory data analysis (EDA) to identify top affected countries
- Visualizations including bar plots and world maps
- Time series forecasting using Facebook Prophet to predict future deaths
- Output generation of plots, forecasts, and the trained model for further analysis

This pipeline allows data-driven insights into COVID-19 trends and future projections, useful for research, policy-making, or dashboards.

---
## Project Structure

```
covid_forecasting_project/
│
├── data/
│   ├── covid_19_clean_complete.csv      # Raw dataset
│   └── processed_data.csv               # Cleaned / aggregated dataset (optional)
│
├── notebooks/
│   └── covid_analysis_forecast.ipynb    # Jupyter notebook for EDA & modeling
│
├── src/
│   ├── data_processing.py               # Data cleaning & aggregation functions
│   ├── visualization.py                 # Plotting functions (bar plots, world map, forecast)
│   ├── forecasting.py                   # Prophet model functions
│   └── logger.py                        # Logging configuration
│
├── outputs/
│   ├── plots/                           # All generated plots
│   │   ├── top10_countries.png
│   │   ├── world_map_confirmed.png
│   │   ├── world_map_deaths.png
│   │   ├── world_map_recovered.png
│   │   ├── world_map_active.png
│   │   ├── forecast_plot.png
│   │   └── forecast_components.png
│   ├── forecasts.csv                     # Forecasted deaths
│   └── prophet_model.pkl                 # Trained Prophet model
│
├── main.py                               # Main script to run the project end-to-end
├── requirements.txt                      # Python dependencies
└── README.md                             # Project overview & instructions

```
---
## Project Workflow

The project workflow is modular and can be executed end-to-end by running main.py:

### 1. Load and clean data
- Raw dataset: data/covid_19_clean_complete.csv
- Cleaning includes renaming columns and dropping the State column (high missing values)

### 2. Aggregate country-level data
- Compute total confirmed, deaths, recovered, and active cases by country

### 3. Visualizations
- Top 10 countries bar plots (outputs/plots/top10_countries.png)
- World map of cases by category (Confirmed, Deaths, Recovered, Active)

### 4. Aggregate daily deaths
- Prepare time series data for forecasting (ds → date, y → daily deaths)

### 5. Prophet Model Forecasting
- Fit Facebook Prophet model on daily deaths
- Predict future deaths for the next 14 days
- Forecast output includes predicted deaths with confidence intervals

### 6. Save outputs
- Plots: outputs/plots/
- Forecast CSV: outputs/forecasts.csv
- Trained Prophet model: outputs/prophet_model.pkl

--- 

## ⚙️ Installation

```
# Clone the repository
git clone https://github.com/Subith-Varghese/covid19-forecasting-analysis.git

# Navigate to the project directory
cd covid19-forecasting-analysis

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the main script
python main.py

```

## Outputs:

- Check outputs/plots/ for visualizations
- Check outputs/forecasts.csv for forecasted deaths
- outputs/prophet_model.pkl can be loaded for future predictions
