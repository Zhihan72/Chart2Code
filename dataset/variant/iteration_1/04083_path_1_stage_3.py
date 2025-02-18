import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
civilizations = ['Ancient Egypt', 'Chinese Han', 'Roman Empire', 'Ancient Greece', 'Maurya Empire']
years = np.arange(-500, 501, 100)

tech_advancements = {
    'Ancient Egypt': [15, 17, 25, 20, 27, 32, 30, 34, 40, 37, 35],
    'Chinese Han': [10, 55, 20, 60, 40, 50, 15, 30, 65, 62, 70],
    'Roman Empire': [5, 140, 20, 35, 90, 70, 10, 105, 50, 120, 150],
    'Ancient Greece': [10, 15, 18, 28, 22, 45, 35, 40, 50, 55, 60],
    'Maurya Empire': [8, 52, 18, 50, 45, 40, 48, 25, 55, 30, 12]
}

population_growth = {
    'Ancient Egypt': [1.2, 1.5, 2, 4, 2.5, 1, 3, 3.5, 4.2, 4.4, 4.5],
    'Chinese Han': [2, 7.5, 3, 4, 8.5, 6, 7, 5, 8.2, 2.5, 8],
    'Roman Empire': [1, 1.5, 10, 8, 4.5, 6, 13.5, 3, 12, 13, 2],
    'Ancient Greece': [3.4, 1.3, 1.1, 1, 2, 2.5, 2.8, 3, 1.6, 3.5, 3.2],
    'Maurya Empire': [3, 6.5, 8, 9, 4, 5.5, 7.2, 8, 8.2, 8.5, 3.5]
}

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Plot for technological advancements
for civ, advancements in tech_advancements.items():
    axs[0].plot(years, advancements, marker='o')

axs[0].grid(True, linestyle='--', alpha=0.7)

# Plot for population growth
for civ, population in population_growth.items():
    axs[1].plot(years, population, marker='x', linestyle='dashed')

axs[1].grid(True, linestyle='--', alpha=0.7)

# Annotations for the first subplot
annotations = [
    (-400, 35, "Pyramid Building"),
    (0, 70, "Invention of Paper"),
    (100, 150, "Roman Engineering Peak"),
    (200, 60, "Greek Philosophy Flourish"),
    (500, 55, "Maurya Golden Era")
]

for (x, y, text) in annotations:
    axs[0].annotate(text, xy=(x, y), xytext=(x+50, y+10),
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.8),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', color='black'))

plt.tight_layout()
plt.show()