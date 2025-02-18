import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

services = {
    "App Delivery": [5, 10, 20, 35, 45, 50, 55, 60, 65, 70, 75],
    "Direct Delivery": [40, 35, 30, 28, 25, 23, 20, 18, 16, 15, 12],
    "Takeaway": [55, 50, 45, 37, 30, 25, 20, 15, 10, 7, 5]
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