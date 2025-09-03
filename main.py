import pandas as pd
from src.data_processing import clean_data, aggregate_country_data, aggregate_daily_deaths
from src.visualization import plot_top10_countries,plot_world_map_cases,plot_forecast
from src.forecasting import build_prophet_model, forecast
import os
from src.logger import logger
import joblib


def main():
    # 1. Load & Clean Data
    data_path = "data/covid_19_clean_complete.csv"
    df = pd.read_csv(data_path)
    df = clean_data(df)
    logger.info("Data loaded and cleaned successfully!")
    
    # 2. Aggregate Country Data
    country_sum = aggregate_country_data(df)
    logger.info("Country-level aggregation done!")
    
    # 3. Plot Top 10 Countries
    plot_top10_countries(country_sum, output_dir="outputs/plots")
    logger.info("Top 10 country plots saved in outputs/plots/")
    
    # 4. Plot World Map of Cases
    plot_world_map_cases(df,output_dir = "outputs/plots")
    logger.info("World map plots saved in outputs/plots/")

    # 5. Aggregate Daily Deaths
    daily_deaths = aggregate_daily_deaths(df)
    logger.info("Daily deaths aggregated for forecasting.")
    
    # 6. Build & Fit Prophet Model
    model = build_prophet_model(daily_deaths)
    logger.info("Prophet model built and fitted.")
    
    # 7. Create Future Dates & Forecast
    forecast_df = forecast(model, periods=14, freq='D')
    logger.info("Forecast completed!")
    
    # 8. Plot Forecast
    # ---------------------------
    plot_forecast(model, forecast_df, output_dir="outputs/plots")
    logger.info("Forecast plots saved in outputs/plots/")
    
    # 9. Save model
    model_path = "outputs/prophet_model.pkl"
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

    # 10. Save Forecast
    base_dir = "outputs"
    os.makedirs(base_dir, exist_ok=True)
    save_path = os.path.join(base_dir, "forecasts.csv")
    forecast_df.to_csv(save_path, index=False)
    logger.info("Forecast saved to outputs/forecasts.csv")
    
if __name__ == "__main__":
    main()
