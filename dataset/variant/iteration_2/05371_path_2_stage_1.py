import matplotlib.pyplot as plt
import numpy as np

# Years of data collection
years = np.arange(2010, 2021)

# Renewable energy capacity (in GW) for Solar and Wind only
solar_capacity = [1, 2, 3, 5, 7, 10, 15, 21, 28, 36, 45]
wind_capacity = [3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68]

# Colors for each type of energy
colors = ['#FFB74D', '#4FC3F7']

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars
bar_width = 0.35  # Adjust width since we have only two groups now
indices = np.arange(len(years))

bars1 = ax.bar(indices - bar_width/2, solar_capacity, bar_width, color=colors[0], edgecolor='black', label='Solar')
bars2 = ax.bar(indices + bar_width/2, wind_capacity, bar_width, color=colors[1], edgecolor='black', label='Wind')

# Customize the plot with titles and labels
ax.set_title('Growth in Renewable Energy Capacity\n2010-2020', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Capacity (GW)', fontsize=14)
ax.set_xticks(indices)
ax.set_xticklabels(years, rotation=45)
ax.legend()

# Adding text labels on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)

# Adjust layout to make room for y-labels
plt.tight_layout()

# Show the plot
plt.show()