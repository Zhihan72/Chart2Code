import matplotlib.pyplot as plt
import numpy as np

percentages = [15, 25, 40, 10, 10]
new_colors = ['#FF6347', '#4682B4', '#9ACD32', '#FF69B4', '#8A2BE2']
explode = (0, 0.1, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

wedges, *_ = ax.pie(
    percentages, 
    colors=new_colors, 
    startangle=100,
    pctdistance=0.75,
    explode=explode,
    wedgeprops=dict(width=0.4, edgecolor='grey', linewidth=1, alpha=0.8),
    shadow=False
)

centre_circle = plt.Circle((0, 0), 0.65, fc='lightgrey', edgecolor='grey', linewidth=1)
ax.add_artist(centre_circle)

ax_inset = fig.add_axes([0.68, 0.55, 0.25, 0.35])
years = [2020, 2030, 2040, 2050]
solar_trend = [30, 35, 20, 40]
nuclear_trend = [23, 15, 25, 20]
ax_inset.plot(years, solar_trend, color='#FF69B4', marker='s', linestyle='-.')
ax_inset.plot(years, nuclear_trend, color='#FF6347', marker='^', linestyle=':')
ax_inset.set_xticks(years)
ax_inset.set_yticks([10, 20, 30, 40])
ax_inset.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()