import matplotlib.pyplot as plt
import numpy as np

# Backstory: Fetching valuable insights from the coffee market in different countries, focusing on average consumption per person and its economic impact.
# Data has been collected based on surveys and market analysis.

# Countries and corresponding average coffee consumption in kilograms per capita per year
countries = ['Brewland', 'Latteville', 'Espressonia', 'Mocha Town', 'Cappuccinia']
coffee_consumption = [8, 10, 5, 7, 11]  # kg per person per year

# Economic impact in terms of billions of dollars per year
economic_impact = [4.5, 5.2, 2.1, 3.1, 6.0]  # billion dollars

# Set positions and width for the bars
x_pos = np.arange(len(countries))
width = 0.35

# Create the figure and a set of two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle('Coffee Consumption and Economic Impact in Notable Coffee-Loving Countries', fontsize=18, fontweight='bold', y=0.98)

# Bar chart for coffee consumption
bars1 = ax1.bar(x_pos - width/2, coffee_consumption, width, color='#8B4513', edgecolor='black', linewidth=1.2, label='Consumption (kg/person)')

# Bar chart for economic impact
bars2 = ax2.bar(x_pos + width/2, economic_impact, width, color='#D2691E', edgecolor='black', linewidth=1.2, label='Economic Impact (B USD)')

# Annotate bars with values for the first chart
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval} kg', ha='center', va='bottom', fontsize=10)

# Annotate bars with values for the second chart
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval} B', ha='center', va='bottom', fontsize=10)

# Set titles and labels for the first subplot
ax1.set_title('Annual Coffee Consumption', fontsize=14, fontweight='bold', pad=10)
ax1.set_xlabel('Countries', fontsize=12)
ax1.set_ylabel('Coffee Consumption (kg/person)', fontsize=12)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(countries, fontsize=11, rotation=30, ha='right')
ax1.set_ylim(0, 12)

# Set titles and labels for the second subplot
ax2.set_title('Economic Impact of Coffee Market', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Countries', fontsize=12)
ax2.set_ylabel('Economic Impact (Billion USD)', fontsize=12)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(countries, fontsize=11, rotation=30, ha='right')
ax2.set_ylim(0, 7)

# Add grid lines for better visual reference
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adding legends
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper left', fontsize=10)

# Adjust layout to prevent overlapping elements
plt.tight_layout(pad=2.0, rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()