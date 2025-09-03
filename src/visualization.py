import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px


def plot_top10_countries(df, output_dir = "outputs/plots"):
    os.makedirs(output_dir, exist_ok=True)
    
    top10_cols = ['Confirmed', 'Deaths', 'Recovered', 'Active']
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.flatten()
    
    for i, col in enumerate(top10_cols):
        top10 = df.nlargest(10, col)
        sns.barplot(x=top10['Country'], y=top10[col], ax=axes[i])
        axes[i].set_xlabel('Country')
        axes[i].set_ylabel(f'Count of {col}')
        axes[i].set_title(f'{col} in Top 10 Countries')
        axes[i].tick_params(axis='x', rotation=45)
        
    # Save each plot individually
    fig_name = os.path.join(output_dir, "top10_ Countries.png")
    fig.savefig(fig_name, bbox_inches='tight')
    
    plt.tight_layout()
    plt.show()

def plot_world_map_cases(df,output_dir = "outputs/plots"):
    top10_cols = ['Confirmed', 'Deaths', 'Recovered', 'Active']
    
    for col in top10_cols:
        fig = px.choropleth(df,
                            locations='Country',
                            locationmode='country names',
                            hover_name='Country',
                            color=col,
                            title=f'{col} Cases by Country',
                            color_continuous_scale='Viridis')
        
        # Save static PNG
        png_path = os.path.join(output_dir, f"world_map_{col.lower()}.png")        
        fig.write_image(png_path)

def plot_forecast(model, forecast, output_dir="outputs/plots"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Forecast plot
    fig1 = model.plot(forecast)
    plt.title('Forecasted Death Cases with Confidence Intervals')
    plt.xlabel('Date')
    plt.ylabel('Number of Death Cases')
    plt.tight_layout()
    
    # Save forecast plot
    forecast_plot_path = os.path.join(output_dir, "forecast_plot.png")
    fig1.savefig(forecast_plot_path, bbox_inches='tight')
    plt.show()
    
    # Components plot
    fig2 = model.plot_components(forecast)
    components_plot_path = os.path.join(output_dir, "forecast_components.png")
    fig2.savefig(components_plot_path, bbox_inches='tight')
    plt.show()

