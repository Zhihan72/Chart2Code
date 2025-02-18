import matplotlib.pyplot as plt
import numpy as np

cities = ['Londres', 'SaoPaulo', 'Tokyo', 'Beijing', 'Sidney', 'NovaYork', 'Paris', 'Berlin', 'Mumbai', 'Cairo']
coffee_consumption = [250, 300, 200, 280, 240, 220, 160, 180, 210, 220]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#33FF57', '#3357FF', '#F333FF', '#FF5733', '#FF33C4', '#33FFC4', '#FF3364', '#33F3FF', '#FF9633', '#3367FF']

# Creating horizontal bars
bars = ax.barh(cities, coffee_consumption, color=colors, edgecolor='black')

for bar, consumption in zip(bars, coffee_consumption):
    xval = bar.get_width()
    ax.text(xval + 10, bar.get_y() + bar.get_height()/2, f'{consumption}', va='center', fontsize=10, fontweight='bold', color='black')

# Update title and labels to reflect horizontal layout
ax.set_title('Monthly Coffee Consumption by City', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Monthly Coffee Portions', fontsize=12, labelpad=10)
ax.set_ylabel('Cities', fontsize=12, labelpad=10)

ax.xaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.7)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()