import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_capacity = [1, 2, 3, 5, 7, 10, 15, 21, 28, 36, 45]
wind_capacity = [3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68]
colors = ['#FFB74D', '#4FC3F7']
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.35
indices = np.arange(len(years))

bars1 = ax.bar(indices - bar_width/2, solar_capacity, bar_width, color=colors[0], edgecolor='green', linestyle='-', label='Solar')
bars2 = ax.bar(indices + bar_width/2, wind_capacity, bar_width, color=colors[1], edgecolor='red', linestyle='--', label='Wind')

ax.set_title('Growth in Renewable Energy Capacity\n2010-2020', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14, fontstyle='italic')
ax.set_ylabel('Capacity (GW)', fontsize=14, fontstyle='italic')
ax.set_xticks(indices)
ax.set_xticklabels(years, rotation=30, fontsize=10)
ax.legend(loc='upper left', fontsize=12, shadow=True)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)

plt.grid(True, linestyle=':', linewidth=0.5, axis='y')
plt.tight_layout()
plt.show()