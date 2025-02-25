import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

north_america = np.array([4, 3.5, 3, 5, 6.2, 4.2, 5.5, 6, 5.8, 4.8])
south_america = np.array([1.5, 1.2, 2.4, 1.4, 1.8, 2, 2.2, 1, 2.6, 1.7])
europe = np.array([9, 8.5, 7.5, 11, 10, 10.5, 9, 9.5, 8, 7])
asia = np.array([7.5, 5.5, 8.7, 6.5, 6, 7, 9, 8, 8.3, 5])
africa = np.array([0.6, 1.3, 0.7, 0.8, 1.2, 1.9, 1, 0.5, 1.5, 1.7])
oceania = np.array([0.65, 0.35, 0.4, 0.7, 0.3, 0.5, 0.6, 0.48, 0.55, 0.45])

tourism_data = np.vstack([north_america, south_america, europe, asia, africa, oceania])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#8c564b', '#d62728', '#1f77b4', '#9467bd', '#2ca02c', '#ff7f0e']

ax.stackplot(years, tourism_data, colors=colors, alpha=0.75)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 13, 2))
ax.xaxis.grid(True, linestyle='-.', linewidth=0.7, alpha=0.6)

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.show()