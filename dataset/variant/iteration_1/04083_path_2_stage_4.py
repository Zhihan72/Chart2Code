import matplotlib.pyplot as plt
import numpy as np

civilizations = ['Ancient Egypt', 'Chinese Han', 'Roman Empire', 'Ancient Greece', 'Maurya Empire']
years = np.arange(-500, 501, 100)

tech_advancements = {
    'Ancient Egypt': [15, 17, 20, 25, 27, 30, 32, 34, 35, 37, 40],
    'Chinese Han': [10, 15, 20, 30, 40, 50, 55, 60, 62, 65, 70],
    'Roman Empire': [5, 10, 20, 35, 50, 70, 90, 105, 120, 140, 150],
    'Ancient Greece': [10, 15, 18, 22, 28, 35, 40, 45, 50, 55, 60],
    'Maurya Empire': [8, 12, 18, 25, 30, 40, 45, 48, 50, 52, 55]
}

population_growth = {
    'Ancient Egypt': [1, 1.2, 1.5, 2, 2.5, 3, 3.5, 4, 4.2, 4.4, 4.5],
    'Chinese Han': [2, 2.5, 3, 4, 5, 6, 7, 7.5, 8, 8.2, 8.5],
    'Roman Empire': [1, 1.5, 2, 3, 4.5, 6, 8, 10, 12, 13, 13.5],
    'Ancient Greece': [1, 1.1, 1.3, 1.6, 2, 2.5, 2.8, 3, 3.2, 3.4, 3.5],
    'Maurya Empire': [3, 3.5, 4, 4.5, 5.5, 6.5, 7.2, 8, 8.2, 8.5, 9]
}

fig, axs = plt.subplots(2, 1, figsize=(14, 10))

colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
markers = ['D', '^', 's', 'p', 'h']
line_styles = ['-', '--', '-.', ':', '-']

for i, population in enumerate(population_growth.values()):
    axs[0].plot(years, population, marker=markers[i], linestyle=line_styles[i], color=colors[i])

axs[0].grid(True, linestyle=':', linewidth=1)

for i, advancements in enumerate(tech_advancements.values()):
    axs[1].plot(years, advancements, marker=markers[i], linestyle=line_styles[i], color=colors[i])

axs[1].grid(False)

plt.tight_layout()
plt.show()