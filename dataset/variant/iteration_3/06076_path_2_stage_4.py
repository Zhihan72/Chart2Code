import matplotlib.pyplot as plt
import numpy as np

plantations = ['Greenleaf', 'Sunrise', 'Whispering', 'Mountain', 'Golden']
years = ['2018', '2019', '2020', '2021', '2022']

# Manually shuffled production data within the same dimensional structure
production_data = np.array([
    [1180, 1150, 1200, 1100, 1250],  # Greenleaf
    [980, 1020, 950, 1100, 1050],    # Sunrise
    [750, 810, 780, 850, 800],       # Whispering
    [1350, 1280, 1330, 1400, 1300],  # Mountain
    [1000, 920, 950, 890, 980]       # Golden
])

total_production = np.sum(production_data, axis=1)
average_production = np.mean(production_data, axis=1)

fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for total production
new_colors = ['#8e44ad', '#f39c12', '#d35400', '#c0392b', '#2980b9']
bars = ax1.barh(plantations, total_production, color=new_colors, height=0.6)

for bar in bars:
    width = bar.get_width()
    ax1.text(width + 10, bar.get_y() + bar.get_height()/2, f'{width} kg', va='center', fontsize=10, fontweight='bold')

ax1.set_title("Misty Valleys Tea Output (2018-22)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Total Output (kg)", fontsize=12)
ax1.set_xlim(0, 7000)

ax2 = ax1.twiny()
ax2.plot(average_production, plantations, color='navy', marker='o', linestyle='--')
ax2.set_xlabel('Avg Output (kg)', fontsize=12)
ax2.set_xlim(700, 1500)

plt.tight_layout()
plt.show()