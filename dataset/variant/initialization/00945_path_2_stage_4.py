import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])

solar = np.array([90, 70, 130, 50, 110])
wind = np.array([85, 105, 40, 60, 95])
hydro = np.array([55, 60, 50, 65, 45])
bio = np.array([35, 30, 45, 25, 40])

colors = ['#8B4513', '#00A86B', '#1F78B4', '#FDB813']

fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(years, solar, color=colors[0], edgecolor='none', alpha=0.9)
ax.bar(years, wind, bottom=solar, color=colors[1], edgecolor='none', alpha=0.9)
ax.bar(years, hydro, bottom=solar + wind, color=colors[2], edgecolor='none', alpha=0.9)
ax.bar(years, bio, bottom=solar + wind + hydro, color=colors[3], edgecolor='none', alpha=0.9)

ax.set_title("Renewables in GreenVille (2018-22)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Contribution (M USD)", fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()