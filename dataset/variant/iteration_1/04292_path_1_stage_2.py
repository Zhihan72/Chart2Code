import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

services = {
    "Digital App Dispatch": [5, 10, 20, 35, 45, 50, 55, 60, 65, 70, 75],
    "In-House Restaurant Delivery": [40, 35, 30, 28, 25, 23, 20, 18, 16, 15, 12],
    "Pickup Service": [55, 50, 45, 37, 30, 25, 20, 15, 10, 7, 5]
}

stacked_data = np.array(list(services.values()))

fig, ax = plt.subplots(figsize=(14, 9))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # New set of colors

ax.stackplot(years, stacked_data, labels=services.keys(), alpha=0.8, colors=colors)

ax.set_title("Trends in Food Dispatch Preferences (2012-2022)", fontsize=16, fontweight='bold')
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("Market Fraction (%)", fontsize=12)

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Service Types', fontsize=10, title_fontsize='12', frameon=True)

plt.xticks(rotation=45)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()

plt.show()