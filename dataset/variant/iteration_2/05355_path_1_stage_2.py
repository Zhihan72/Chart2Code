import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 53)

species_1_growth = 2 + 0.5 * weeks + 0.1 * np.sin(2 * np.pi * weeks / 10)
species_2_growth = 3 + 0.6 * weeks + 0.2 * np.cos(2 * np.pi * weeks / 15)
species_3_growth = 1.5 + 0.8 * weeks + 0.15 * np.sin(2 * np.pi * weeks / 8)

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(weeks, species_1_growth, marker='o', linestyle='-', color='#ff7f0e', linewidth=2)
ax.plot(weeks, species_2_growth, marker='s', linestyle='--', color='#2ca02c', linewidth=2)
ax.plot(weeks, species_3_growth, marker='^', linestyle=':', color='#1f77b4', linewidth=2)

ax.annotate('Rapid growth start', xy=(10, species_1_growth[9]), xytext=(15, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')
ax.annotate('Stable growth midpoint', xy=(26, species_2_growth[25]), xytext=(30, 34),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')

for i, week in enumerate(weeks):
    if i % 10 == 0:
        ax.text(week, species_1_growth[i] + 0.5, f'{species_1_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')
        ax.text(week, species_2_growth[i] + 0.5, f'{species_2_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')
        ax.text(week, species_3_growth[i] + 0.5, f'{species_3_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')

plt.title("Simulated Growth of Cloned Plant Species Over One Year on Mars\nWeekly Height Measurements", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Week of the Year', fontsize=12)
ax.set_ylabel('Height (cm)', fontsize=12)
plt.xticks(weeks[::4])

plt.show()