import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2010, 2023)

# Hypothetical temperature data in Celsius for three different cities over the years
city_A_temps = [16.2, 16.5, 17.0, 17.3, 17.7, 18.1, 18.4, 18.7, 19.1, 19.5, 19.8, 20.2, 20.5]  # City A
city_B_temps = [14.0, 14.4, 14.7, 15.1, 15.4, 15.8, 16.1, 16.4, 16.8, 17.1, 17.5, 17.8, 18.2]  # City B
city_C_temps = [10.5, 10.8, 11.2, 11.5, 11.9, 12.2, 12.6, 12.9, 13.3, 13.6, 14.0, 14.3, 14.7]  # City C

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot temperatures for three cities with different styles
ax.plot(years, city_A_temps, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='City A')
ax.plot(years, city_B_temps, marker='s', linestyle='--', color='#ff7f0e', linewidth=2, label='City B')
ax.plot(years, city_C_temps, marker='^', linestyle='-.', color='#2ca02c', linewidth=2, label='City C')

# Customize the title and axis labels
ax.set_title('Rising Temperatures in FantasyCities\nTracking Climate Change Over a Decade', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Temperature (°C)', fontsize=12)

# Customize x-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add a legend
ax.legend(title='Cities', loc='upper left', fontsize=10)

# Annotate key milestones
annotations = {
    2015: ("Mid-Decade Warning", city_A_temps[5]),
    2018: ("Rapid Spike", city_B_temps[8]),
    2022: ("Significant Increase", city_C_temps[12]),
}

for year, (text, y_value) in annotations.items():
    ax.annotate(text, xy=(year, y_value), xytext=(year, y_value + 1),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5), fontsize=10, color='black', ha='center')

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()