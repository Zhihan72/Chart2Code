import matplotlib.pyplot as plt
import numpy as np

# Plantations and tea production data in kg for 2018-2022
plantations = ['Greenleaf', 'Sunrise', 'Whispering', 'Mountain', 'Golden']
years = ['2018', '2019', '2020', '2021', '2022']

production_data = np.array([
    [1100, 1150, 1200, 1180, 1250],
    [950, 1020, 980, 1050, 1100],
    [750, 780, 800, 810, 850],
    [1300, 1280, 1330, 1350, 1400],
    [890, 920, 950, 980, 1000]
])

total_production = np.sum(production_data, axis=1)
average_production = np.mean(production_data, axis=1)

fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for total production
colors = ['#4c7b7b', '#6a9e9e', '#84bab8', '#a1cfde', '#d2e3e4']
bars = ax1.barh(plantations, total_production, color=colors, edgecolor='black', height=0.6)

for bar in bars:
    width = bar.get_width()
    ax1.text(width + 10, bar.get_y() + bar.get_height()/2, f'{width} kg', va='center', fontsize=10, fontweight='bold')

# Set titles and labels
ax1.set_title("Misty Valleys Tea Output (2018-22)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Total Output (kg)", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 7000)

ax2 = ax1.twiny()
ax2.plot(average_production, plantations, color='navy', marker='o', linestyle='--', label='Avg Output (kg)')
ax2.set_xlabel('Avg Output (kg)', fontsize=12)
ax2.set_xlim(700, 1500)

ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()