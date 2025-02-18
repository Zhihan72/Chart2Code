import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 53)

species_1_growth = 2 + 0.5 * weeks + 0.1 * np.sin(2 * np.pi * weeks / 10)
species_3_growth = 1.5 + 0.8 * weeks + 0.15 * np.sin(2 * np.pi * weeks / 8)

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(weeks, species_1_growth, marker='o', linestyle='-', color='#ff7f0e', linewidth=2)
ax.plot(weeks, species_3_growth, marker='^', linestyle=':', color='#1f77b4', linewidth=2)

ax.annotate('Intense growth phase start', xy=(10, species_1_growth[9]), xytext=(15, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')

for i, week in enumerate(weeks):
    if i % 10 == 0:
        ax.text(week, species_1_growth[i] + 0.5, f'Plant A: {species_1_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')
        ax.text(week, species_3_growth[i] + 0.5, f'Sample C: {species_3_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')

plt.title("Annual Height Growth Patterns of Martian Plant Specimens\nMeasured Heights Weekly", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Weekly Intervals', fontsize=12)
ax.set_ylabel('Growth Height (cm)', fontsize=12)
plt.xticks(weeks[::4])

plt.show()