import matplotlib.pyplot as plt
import numpy as np

species = ['Oak Trees', 'Pine Trees', 'Maple Trees', 'Deer Population', 'Bird Population']

years = np.array([2020, 2021, 2022, 2023, 2024])

oak_growth = np.array([100, 120, 140, 160, 180])
pine_growth = np.array([90, 105, 130, 150, 170])
maple_growth = np.array([80, 95, 115, 135, 155])
deer_growth = np.array([50, 60, 70, 85, 95])
bird_growth = np.array([200, 220, 260, 300, 340])

fig, ax = plt.subplots(figsize=(12, 8))

# Shuffle colors for each data group or type
ax.plot(years, oak_growth, marker='p', linestyle='-', color='#FFA500', linewidth=3, label='Oak Trees')
ax.plot(years, pine_growth, marker='x', linestyle=':', color='#00FF00', linewidth=2, label='Pine Trees')
ax.plot(years, maple_growth, marker='h', linestyle='--', color='#FF4500', linewidth=2, label='Maple Trees')
ax.plot(years, deer_growth, marker='v', linestyle='-.', color='#1E90FF', linewidth=2.5, label='Deer Population')
ax.plot(years, bird_growth, marker='x', linestyle='-', color='#8A2BE2', linewidth=1.5, label='Bird Population')

ax.set_title('Ecosystem Balance: Annual Growth Rates (2020-2024)', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Growth Rate (Arbitrary Units)', fontsize=12)

# Grid adjustments
ax.grid(True, linestyle='-', linewidth=0.75, alpha=0.5)

# Legend adjustments
ax.legend(title='Species', fontsize=10, title_fontsize='13', loc='lower right', frameon=False)

# Annotations with new colors
for growth, label, color in zip([oak_growth, pine_growth, maple_growth, deer_growth, bird_growth], 
                                ['Oak Trees', 'Pine Trees', 'Maple Trees', 'Deer Population', 'Bird Population'], 
                                ['#FFA500', '#00FF00', '#FF4500', '#1E90FF', '#8A2BE2']):
    ax.annotate(f'{growth[-1]}',
                xy=(years[-1], growth[-1]),
                xytext=(-10, 5),
                textcoords='offset points',
                fontsize=10,
                color=color,
                arrowprops=dict(arrowstyle='->', lw=1))

plt.tight_layout()
plt.show()