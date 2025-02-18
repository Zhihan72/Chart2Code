import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are investigating the global market share of various clean energy sources for 2023.
title = "Global Market Share of Clean Energy Sources in 2023"
subtitle = "A Comparative Breakdown"

# Data Source: Hypothetical percentages determined based on estimated market sizes.
clean_energy_sources = [
    'Solar Power',
    'Wind Energy',
    'Hydropower',
    'Biomass Energy',
    'Geothermal Energy',
    'Tidal Energy'
]

market_share = [35, 25, 20, 10, 7, 3]  # Expressed in % terms

# Colors for each energy source for better visual distinction
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Explode the 'Solar Power' slice to highlight it
explode = (0.1, 0, 0, 0, 0, 0)

# Function to create the pie chart
def create_pie(chart_title, sources, market_share, colors, explode):
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(
        market_share, labels=sources, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='w')
    )
    
    # Customize text properties
    for text in texts:
        text.set_fontsize(9)
        text.set_color('darkblue')

    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_color('darkred')
    
    # Adding a circle at the center to transform pie chart into a donut chart
    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='k')
    fig.gca().add_artist(centre_circle)
    
    ax.set_title(chart_title, fontsize=14, fontweight='bold', pad=20)

    # Position the legend to avoid overlap with the pie chart
    ax.legend(wedges, sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

    # Ensure the plot is well adjusted
    plt.tight_layout()

    # Display the plot
    plt.show()

# Create subplots to include a comparison chart
def create_comparison_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

    # Data for comparison chart
    energy_types = ['Renewable', 'Non-Renewable']
    energy_percentages = [55, 45]  # Hypothetical numbers

    # Pie chart for clean energy sources
    wedges, texts, autotexts = ax1.pie(
        market_share, labels=clean_energy_sources, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='w')
    )
    
    for text in texts:
        text.set_fontsize(9)
        text.set_color('darkblue')

    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_color('darkred')
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='k')
    fig.gca().add_artist(centre_circle)

    ax1.set_title("Clean Energy Sources", fontsize=12, fontweight='bold', pad=20)

    # Pie chart for renewable vs non-renewable energy
    wedges, texts, autotexts = ax2.pie(
        energy_percentages, labels=energy_types, autopct='%1.1f%%', startangle=140,
        colors=['#66b3ff', '#ff6666'], explode=(0.1, 0), shadow=True, wedgeprops=dict(edgecolor='w')
    )
    
    for text in texts:
        text.set_fontsize(10)
        text.set_color('black')

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color('white')

    centre_circle_2 = plt.Circle((0, 0), 0.70, fc='white', edgecolor='k')
    fig.gca().add_artist(centre_circle_2)
    
    ax2.set_title("Renewable vs Non-Renewable", fontsize=12, fontweight='bold', pad=20)

    # Adjust layout to make sure both subplots fit properly
    plt.tight_layout()

    # Set overall title
    plt.suptitle(f"{title}\n{subtitle}", fontsize=16, fontweight='bold', y=1.05)

    # Display the combined plot
    plt.show()

# Run the functions to create the plots
create_pie(title, clean_energy_sources, market_share, colors, explode)
create_comparison_chart()