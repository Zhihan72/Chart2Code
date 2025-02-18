import matplotlib.pyplot as plt
import numpy as np

civilizations = ['Ancient Egypt', 'Chinese Han', 'Roman Empire', 'Ancient Greece', 'Maurya Empire']
years = np.arange(-500, 501, 100)

tech_advancements = {
    'Ancient Egypt': [25, 15, 27, 30, 35, 32, 40, 34, 17, 37, 20],
    'Chinese Han': [50, 20, 70, 40, 10, 60, 65, 55, 30, 15, 62],
    'Roman Empire': [150, 10, 50, 35, 90, 120, 140, 20, 105, 5, 70],
    'Ancient Greece': [28, 40, 35, 60, 22, 50, 15, 18, 10, 45, 55],
    'Maurya Empire': [8, 52, 40, 48, 25, 18, 50, 6, 55, 45, 30]
}

population_growth = {
    'Ancient Egypt': [4, 1.5, 4.2, 3.5, 1, 4.5, 3, 2, 1.2, 4.4, 2.5],
    'Chinese Han': [8.2, 3, 2.5, 7, 2, 7.5, 8.5, 6, 4, 8, 5],
    'Roman Empire': [10, 13, 1.5, 12, 3, 1, 13.5, 4.5, 1.5, 8, 6],
    'Ancient Greece': [3.4, 2.8, 3, 1.6, 1, 3.2, 2.5, 3.5, 1.1, 1.3, 2],
    'Maurya Empire': [6.5, 4.5, 8.5, 8, 3.5, 7.2, 3, 9, 5.5, 8.2, 4]
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