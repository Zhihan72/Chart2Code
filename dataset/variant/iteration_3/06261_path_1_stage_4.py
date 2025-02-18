import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2021, 2022, 2023, 2024])
oak_growth = np.array([100, 120, 140, 160, 180])
pine_growth = np.array([90, 105, 130, 150, 170])
maple_growth = np.array([80, 95, 115, 135, 155])
bird_growth = np.array([200, 220, 260, 300, 340])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, oak_growth, marker='o', linestyle='-', color='#1E90FF', linewidth=2)
ax.plot(years, pine_growth, marker='s', linestyle='--', color='#8A2BE2', linewidth=2)
ax.plot(years, maple_growth, marker='^', linestyle='-.', color='#FF4500', linewidth=2)
ax.plot(years, bird_growth, marker='*', linestyle='-', color='#FFA500', linewidth=2)

ax.set_title('Forest Life Dynamics: Yearly Expansion of Select Species (2020-2024)', fontsize=16, fontweight='bold')
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Rate of Growth (Units)', fontsize=12)

ax.set_xticks(years)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()
plt.show()