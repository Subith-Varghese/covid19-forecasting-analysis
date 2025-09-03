from prophet import Prophet
import pandas as pd
import os

def build_prophet_model(df, interval_width= 0.95):
    model = Prophet(interval_width=interval_width)
    model.fit(df)
    return model

def forecast(model, periods = 14, freq = 'D'):
    #Create Future Dates & Forecast
    future_dates = model.make_future_dataframe(periods=periods, freq=freq)
    forecast_df = model.predict(future_dates)
    
    # Convert forecasted values to integers
    forecast_df[['Predicted Deaths (yhat)', 'Lower Bound (yhat_lower)', 'Upper Bound (yhat_upper)']] = forecast_df[['yhat', 'yhat_lower', 'yhat_upper']].astype(int)
    return forecast_df
