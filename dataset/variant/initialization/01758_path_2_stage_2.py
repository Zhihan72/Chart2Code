import matplotlib.pyplot as plt
import numpy as np

percentages = [40, 25, 10, 15, 10]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#F3FF33']

explode = (0.1, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

ax.pie(
    percentages, 
    colors=colors, 
    startangle=140, 
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2, alpha=0.9),
    shadow=True,
    explode=explode
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='white', linewidth=1.5)
ax.add_artist(centre_circle)

ax_inset = fig.add_axes([0.72, 0.6, 0.2, 0.3])
years = [2020, 2030, 2040, 2050]
solar_trend = [20, 30, 35, 40]
nuclear_trend = [15, 20, 23, 25]
ax_inset.plot(years, solar_trend, color='#FF5733', marker='o')
ax_inset.plot(years, nuclear_trend, color='#33FF57', marker='o')
ax_inset.set_xticks(years)
ax_inset.set_yticks([10, 20, 30, 40])
ax_inset.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()