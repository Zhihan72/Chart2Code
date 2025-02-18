import matplotlib.pyplot as plt
import numpy as np

percentages = [10, 25, 40, 10, 15]  # shuffled
colors = ['#1E90FF', '#32CD32', '#FFD700', '#8B0000', '#FFA500']  # shuffled
explode = (0, 0, 0.1, 0.1, 0)

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, *_ = ax.pie(
    percentages, 
    colors=colors, 
    startangle=140, 
    pctdistance=0.85,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2, alpha=0.9),
    shadow=True
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='white', linewidth=1.5)
ax.add_artist(centre_circle)

ax_inset = fig.add_axes([0.72, 0.6, 0.2, 0.3])
years = [2020, 2030, 2040, 2050]
solar_trend = [40, 30, 35, 20]  # shuffled
nuclear_trend = [20, 25, 15, 23]  # shuffled
ax_inset.plot(years, solar_trend, color='#FFD700', marker='o')
ax_inset.plot(years, nuclear_trend, color='#8B0000', marker='o')
ax_inset.set_xticks(years)
ax_inset.set_yticks([10, 20, 30, 40])
ax_inset.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()