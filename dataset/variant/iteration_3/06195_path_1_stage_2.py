import matplotlib.pyplot as plt
import numpy as np

# Define regions and years
regions = ['Avalon', 'Mystica', 'Faerun', 'Narnia', 'Wonderland', 'Elvandar', 'Middle Earth']
years = [2018, 2019, 2020, 2021, 2022]

# Data: Magic Beans Production (in metric tons)
production_data = np.array([
    [12, 15, 14, 16, 18],  # Avalon
    [10, 11, 13, 17, 19],  # Mystica
    [13, 14, 16, 15, 17],  # Faerun
    [9, 13, 12, 14, 15],   # Narnia
    [14, 16, 18, 20, 22],  # Wonderland
    [11, 13, 14, 18, 21],  # Elvandar
    [8, 12, 15, 19, 20]    # Middle Earth
])

# Set the positions of the bars
bar_width = 0.12
x = np.arange(len(years))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each region
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

# Create a bar for each region
for i, region in enumerate(regions):
    ax.bar(x + i * bar_width, production_data[i], width=bar_width, color=colors[i])

# Customize the plot
ax.set_xticks(x + bar_width * 3)
ax.set_xticklabels(years)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add text annotations on each bar for better insight
for i in range(len(regions)):
    for j in range(len(years)):
        ax.text(x[j] + i * bar_width, production_data[i, j] + 0.3, str(production_data[i, j]), ha='center', va='bottom', fontsize=10)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()