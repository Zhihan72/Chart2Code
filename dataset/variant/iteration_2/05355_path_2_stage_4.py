import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 53)

species_1_growth = np.array([2, 2.5, 3, 4, 5.5, 6.5, 7, 7.5, 8, 7.7, 9, 12, 14, 13, 12.5, 12, 12.8, 10.5, 11, 14, 15.3, 16, 17, 18.5, 20, 21.2, 22.5, 23, 22.1, 23, 27, 25, 27, 26, 26.5, 27, 27.5, 30, 30, 32, 33, 33.5, 36, 36.3, 38, 38.2, 39.5, 41, 42, 43, 42, 44])
species_2_growth = np.array([3, 3.6, 8, 7, 10, 11.2, 10.8, 11.5, 12, 14, 14.8, 13, 16, 16.5, 15, 18.5, 19, 19.5, 17, 20, 22, 23, 23.5, 25, 26, 20.5, 27, 29, 28.5, 30, 31, 34, 35, 38, 39, 37, 38.2, 41, 40, 42, 44, 43, 46, 46.3, 45, 47, 49, 50, 49, 51, 52, 53])
species_3_growth = np.array([3, 4, 9.5, 10, 13.7, 15, 17, 17.5, 19, 20.1, 20.5, 21, 23, 24, 25, 22, 24.5, 22.7, 20, 27, 28.5, 30, 32, 34, 34.8, 37, 29, 40, 41, 41.5, 43, 45, 46.5, 44, 45.5, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58.5, 59, 60, 61, 61.5, 62, 64])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(weeks, species_1_growth, marker='o', linestyle='-', color='#377eb8', linewidth=2)
ax.plot(weeks, species_2_growth, marker='s', linestyle='--', color='#4daf4a', linewidth=2)
ax.plot(weeks, species_3_growth, marker='^', linestyle=':', color='#984ea3', linewidth=2)

ax.annotate('Rapid start', xy=(10, species_1_growth[9]), xytext=(15, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')
ax.annotate('Midpoint', xy=(26, species_2_growth[25]), xytext=(30, 34),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')

for i, week in enumerate(weeks):
    if i % 10 == 0:
        ax.text(week, species_1_growth[i] + 0.5, f'{species_1_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')
        ax.text(week, species_2_growth[i] + 0.5, f'{species_2_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')
        ax.text(week, species_3_growth[i] + 0.5, f'{species_3_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')

plt.title("Yearly Growth on Mars", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Week', fontsize=12)
ax.set_ylabel('Height', fontsize=12)
plt.xticks(weeks[::4], rotation=45)
plt.tight_layout()

plt.show()