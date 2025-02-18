import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
nasa_missions = np.array([15, 16, 15, 17, 16, 18, 19, 21, 18, 19, 22])
spacex_missions = np.array([1, 2, 3, 4, 5, 7, 10, 12, 14, 18, 22])
esa_missions = np.array([10, 11, 11, 13, 12, 14, 13, 16, 15, 14, 15])
roscosmos_missions = np.array([12, 13, 12, 14, 15, 14, 13, 14, 15, 16, 16])

data = np.vstack([nasa_missions, spacex_missions, esa_missions, roscosmos_missions])

fig, ax = plt.subplots(figsize=(14, 9))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax.stackplot(years, data, colors=colors, alpha=0.8)

# Removing annotations, labels, and legends
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 71, 10))
ax.set_ylim(0, 70)
ax.grid(linestyle='--', alpha=0.5)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()