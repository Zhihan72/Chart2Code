import matplotlib.pyplot as plt
import numpy as np

# Define regions and years
regions = ['North', 'South']
years = ['2019', '2020', '2021', '2022']

# Annual solar power generation data (GWh) for each region
north_generation = np.array([20, 25, 30, 35])
south_generation = np.array([25, 30, 35, 40])

# Diverging data
north_diverging = north_generation
south_diverging = -south_generation

colors = ['#3498db', '#e74c3c']

# Create the figure and axes
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(years))

# Plot diverging bars
ax.barh(x, north_diverging, color=colors[0], label='North', edgecolor='black')
ax.barh(x, south_diverging, color=colors[1], label='South', edgecolor='black')

# Set labels and title
ax.set_xlabel('Solar Power Generation (GWh)', fontsize=12)
ax.set_title('Diverging Solar Power Generation by Region', fontsize=16, fontweight='bold')
ax.set_yticks(x)
ax.set_yticklabels(years)
ax.legend(loc='upper right')

# Annotating each bar
for i, (n, s) in enumerate(zip(north_diverging, south_diverging)):
    ax.text(n + 1, i, f'{n} GWh', va='center', fontsize=10)
    ax.text(s - 1, i, f'{-s} GWh', va='center', fontsize=10, ha='right')

ax.axvline(0, color='grey', linewidth=0.8)

# Display the plot
plt.show()