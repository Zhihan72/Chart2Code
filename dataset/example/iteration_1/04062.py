import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the yearly production volumes of different fruit types (Apples, Bananas, Oranges) 
# in a fictional farm "Green Acres" over the last 5 years.

# Define the years
years = np.arange(2018, 2023)

# Production volumes in metric tons for the farm 'Green Acres' (artificial data)
apples_production = [120, 130, 135, 140, 150]
bananas_production = [90, 95, 100, 105, 110]
oranges_production = [110, 115, 120, 125, 130]

# Bar width
bar_width = 0.25

# Position of bars on the x-axis
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create bars for Apples, Bananas, and Oranges
bars1 = ax.bar(r1, apples_production, color='red', width=bar_width, edgecolor='grey', label='Apples')
bars2 = ax.bar(r2, bananas_production, color='yellow', width=bar_width, edgecolor='grey', label='Bananas')
bars3 = ax.bar(r3, oranges_production, color='orange', width=bar_width, edgecolor='grey', label='Oranges')

# Add data labels above the bars
def add_labels(bars, ax):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=11)

add_labels(bars1, ax)
add_labels(bars2, ax)
add_labels(bars3, ax)

# Title and labels
ax.set_title("Annual Fruit Production at Green Acres Farm\n(2018-2022)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Production Volume (Metric Tons)", fontsize=14)
ax.set_xticks([r + bar_width for r in range(len(years))])
ax.set_xticklabels(years)
ax.legend()

# Grid lines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Show the plot
plt.show()