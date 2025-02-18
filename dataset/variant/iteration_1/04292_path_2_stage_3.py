import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

# Randomly shuffle the data within each service category while preserving the structure
services = {
    "App Delivery": [70, 5, 50, 60, 35, 65, 75, 55, 20, 10, 45],
    "Direct Delivery": [15, 25, 20, 16, 28, 30, 35, 40, 12, 23, 18],
    "Takeaway": [7, 30, 10, 45, 50, 5, 20, 55, 37, 25, 15]
}

stacked_data = np.array(list(services.values()))

fig, ax = plt.subplots(figsize=(14, 9))

colors = ['#76B041', '#FF9F40', '#4E91AF']

ax.stackplot(years, stacked_data, labels=services.keys(), colors=colors, alpha=0.8)

ax.set_title("Food Delivery Usage\n(2012-22)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("% Usage", fontsize=12)

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Services', fontsize=10, title_fontsize='12', frameon=True)

plt.xticks(rotation=45)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()