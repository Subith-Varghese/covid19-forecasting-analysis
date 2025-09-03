import pandas as pd

def clean_data(df):
    # Rename columns
    df.rename(columns={'Province/State': 'State', 'Country/Region': 'Country'}, inplace=True)
    
    # Drop 'State' column due to high missing values
    df.drop(columns=['State'], inplace=True)
    
    return df

def aggregate_country_data(df):
    country_sum = df.groupby('Country')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()
    return country_sum

def aggregate_daily_deaths(df):
    death_cases = df.groupby('Date')['Deaths'].sum().reset_index()
    death_cases.columns = ['ds', 'y']
    death_cases['ds'] = pd.to_datetime(death_cases['ds'])
    return death_cases
