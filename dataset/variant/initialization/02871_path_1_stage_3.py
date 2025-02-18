import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1900, 2000, 10)

romance = np.array([30, 25, 20, 15, 10, 12, 18, 20, 22, 25])
war = np.array([5, 8, 15, 25, 30, 35, 25, 15, 10, 5])
sci_fi = np.array([1, 2, 4, 8, 10, 12, 15, 18, 22, 25])

theme_data = np.vstack([romance, war, sci_fi])

plt.figure(figsize=(14, 8))

colors = ['#FF6347', '#7FFF00', '#D2691E']

plt.stackplot(decades, theme_data, colors=colors, alpha=0.8)

plt.grid(visible=True, color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

for i, theme in enumerate(theme_data):
    plt.plot(decades, np.cumsum(theme_data, axis=0)[i], marker='o', markersize=5, color=colors[i])

plt.xticks(decades, rotation=45)

plt.tight_layout()

plt.show()