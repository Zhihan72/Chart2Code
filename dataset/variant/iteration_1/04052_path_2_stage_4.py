import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
soccer_subs = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180]
basketball_subs = [30, 32, 35, 38, 42, 45, 48, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100, 110, 120, 130, 140]
esports_subs = [5, 10, 15, 20, 28, 35, 40, 50, 60, 70, 85, 100, 115, 130, 145, 160, 175, 190, 210, 230, 250]

fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# New colors have been set for the plots
ax.plot(years, soccer_subs, marker='o', linestyle='-', linewidth=2, color='#2ca02c')  # New color: green
ax.plot(years, basketball_subs, marker='x', linestyle='--', linewidth=2, color='#9467bd')  # New color: purple
ax.plot(years, esports_subs, marker='^', linestyle=':', linewidth=2, color='#8c564b')  # New color: brown

plt.tight_layout()

plt.show()