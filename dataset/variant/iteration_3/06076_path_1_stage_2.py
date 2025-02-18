import matplotlib.pyplot as plt
import numpy as np

# Tea plantations and their production data
plantations = ['Greenleaf', 'Sunrise', 'Whispering', 'Mountain', 'Golden']
years = ['2018', '2019', '2020', '2021', '2022']

# Randomly altered production data while keeping the original dimensional structure
production_data = np.array([
    [1150, 1100, 1250, 1200, 1180],  # Altered
    [1050, 950, 1100, 980, 1020],    # Altered
    [800, 780, 810, 850, 750],       # Altered
    [1350, 1330, 1300, 1280, 1400],  # Altered
    [920, 890, 1000, 950, 980]       # Altered
])

total_production = np.sum(production_data, axis=1)
average_production = np.mean(production_data, axis=1)

fig, ax1 = plt.subplots(figsize=(14, 8))

colors = ['#4c7b7b', '#6a9e9e', '#84bab8', '#a1cfde', '#d2e3e4']
bars = ax1.barh(plantations, total_production, color=colors, edgecolor='black', height=0.6)

for bar in bars:
    width = bar.get_width()
    ax1.text(width + 10, bar.get_y() + bar.get_height()/2, f'{width} kg', va='center', fontsize=10, fontweight='bold')

ax1.set_title("Tea Production (2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Total (kg)", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 7000)

ax2 = ax1.twiny()
ax2.plot(average_production, plantations, color='navy', marker='o', linestyle='--', label='Avg (kg)')
ax2.set_xlabel('Avg (kg)', fontsize=12)
ax2.set_xlim(700, 1500)

ax2.legend(loc='upper right', fontsize=10)
plt.tight_layout()
plt.show()