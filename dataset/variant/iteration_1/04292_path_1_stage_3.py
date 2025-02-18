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

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

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