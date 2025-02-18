import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1970, 2021, 5)

atlantic_exploration = [10, 15, 18, 25, 30, 40, 55, 65, 80, 90, 105]
pacific_exploration = [8, 12, 20, 30, 40, 55, 70, 85, 100, 115, 130]
indian_exploration = [5, 7, 10, 15, 20, 30, 45, 50, 60, 75, 85]
arctic_exploration = [3, 4, 7, 10, 12, 18, 25, 30, 40, 50, 60]

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, atlantic_exploration, pacific_exploration, indian_exploration, arctic_exploration,
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

ax.legend(frameon=False)

plt.xticks(years, rotation=45)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()