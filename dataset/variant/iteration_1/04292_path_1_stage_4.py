import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

services = {
    "Digital App Dispatch": [5, 50, 20, 35, 55, 45, 60, 55, 70, 65, 75],
    "In-House Restaurant Delivery": [40, 25, 35, 30, 28, 23, 18, 20, 15, 16, 12],
    "Pickup Service": [55, 30, 50, 45, 37, 25, 15, 20, 7, 10, 5]
}

stacked_data = np.array(list(services.values()))

fig, ax = plt.subplots(figsize=(14, 9))

# Update color scheme
colors = ['#bcbd22', '#17becf', '#e377c2']

# Randomly modify line styles
ax.stackplot(years, stacked_data, labels=services.keys(), alpha=0.8, colors=colors, linestyle='-.')

# Update titles and labels with new styles
ax.set_title("Trends in Food Dispatch Preferences (2012-2022)", fontsize=18, fontweight='light', style='italic')
ax.set_xlabel("Timeline", fontsize=14, fontstyle='italic')
ax.set_ylabel("Market Fraction (%)", fontsize=14, fontstyle='italic')

# Modify legend placement and appearance
ax.legend(loc='lower right', title='Service Types', fontsize=11, title_fontsize='13', frameon=False)

# Adjust x-axis ticks rotation
plt.xticks(rotation=30)

# Remove grid lines
# ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add marker types to the stackplot
ax.stackplot(years, stacked_data, step='mid', labels=services.keys(), alpha=0.4, colors=colors)

plt.tight_layout()

plt.show()