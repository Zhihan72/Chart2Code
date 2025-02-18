import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)
public_transport = np.array([30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50])
cycling = np.array([6, 7, 8, 9, 12, 14, 13, 15, 21, 20, 24])
walking = np.array([11, 10, 13, 14, 13, 16, 14, 18, 17, 20, 22])
electric_vehicles = np.array([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])
conventional_vehicles = np.array([51, 48, 41, 37, 33, 26, 23, 11, 2, 1, 0])

fig, ax = plt.subplots(figsize=(14, 9))
bar_width = 0.15  # Width for each bar

# Assigning colors to each category and plotting them with an offset to create a grouped bar chart
ax.bar(years - 2*bar_width, public_transport, width=bar_width, color='#cc66ff', label='Public Transport')
ax.bar(years - bar_width, cycling, width=bar_width, color='#ff6666', label='Cycling')
ax.bar(years, walking, width=bar_width, color='#4d88ff', label='Walking')
ax.bar(years + bar_width, electric_vehicles, width=bar_width, color='#66c266', label='Electric Vehicles')
ax.bar(years + 2*bar_width, conventional_vehicles, width=bar_width, color='#ff9933', label='Conventional Vehicles')

ax.set_title("Urban Transport Modes (2012-2022)", fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("%", fontsize=12)
ax.set_xticks(years)
ax.set_yticks(range(0, 101, 10))
ax.set_ylim(0, 100)

ax.legend()

for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()