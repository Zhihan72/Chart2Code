import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
solar = np.array([50, 70, 100, 150, 210, 300, 420, 550, 700, 850, 1000])
hydro = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150])
battery_storage = np.array([0, 5, 15, 30, 60, 120, 200, 310, 440, 580, 720])

fig = plt.figure(figsize=(8, 7))
plt.stackplot(years, solar, hydro, battery_storage, colors=['#8E44AD', '#3498DB', '#E74C3C'], alpha=0.85)
plt.legend(loc='upper right', frameon=False)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(years)
plt.xlim(2015, 2025)
plt.ylim(0, 2500)

plt.tight_layout()
plt.show()