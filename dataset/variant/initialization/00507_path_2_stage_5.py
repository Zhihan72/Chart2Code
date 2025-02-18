import matplotlib.pyplot as plt
import numpy as np

# Data definition
years = ['2021', '2020', '2023', '2022']  # Randomly altered order of years
solar_energy = [250, 200, 350, 300]  # Randomly altered order of solar energy data
wind_energy = [180, 150, 260, 220]  # Randomly altered order of wind energy data

# Shuffle the assigned colors for each data group
colors = ['#87ceeb', '#ffd700']  # Switched the colors

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.3
index = np.arange(len(years))

ax.bar(index, solar_energy, color=colors[0], width=bar_width, align='center')
ax.bar(index + bar_width, wind_energy, color=colors[1], width=bar_width, align='center')

ax.set_xticks(index + 0.5 * bar_width)
ax.set_xticklabels(years)

ax.set_xlabel('Time Period', fontsize=12)
ax.set_ylabel('Energy Output (Gigawatt Hours)', fontsize=12)

plt.title('Energy Production Comparison', fontsize=14)

plt.tight_layout()
plt.show()