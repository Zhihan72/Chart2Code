import matplotlib.pyplot as plt
import numpy as np

percentages = [15, 25, 40, 10, 10]  # shuffled
colors = ['#32CD32', '#FFD700', '#1E90FF', '#FFA500', '#8B0000']  # shuffled
explode = (0, 0.1, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

wedges, *_ = ax.pie(
    percentages, 
    colors=colors, 
    startangle=100,  # Changed angle
    pctdistance=0.75,  # Changed distance
    explode=explode,
    wedgeprops=dict(width=0.4, edgecolor='grey', linewidth=1, alpha=0.8),  # Changed style
    shadow=False  # Removed shadow
)

centre_circle = plt.Circle((0, 0), 0.65, fc='lightgrey', edgecolor='grey', linewidth=1)  # Changed style
ax.add_artist(centre_circle)

ax_inset = fig.add_axes([0.68, 0.55, 0.25, 0.35])  # Changed position and size
years = [2020, 2030, 2040, 2050]
solar_trend = [30, 35, 20, 40]  # shuffled
nuclear_trend = [23, 15, 25, 20]  # shuffled
ax_inset.plot(years, solar_trend, color='#FFA500', marker='s', linestyle='-.')  # Changed marker and line style
ax_inset.plot(years, nuclear_trend, color='#32CD32', marker='^', linestyle=':')  # Changed marker and line style
ax_inset.set_xticks(years)
ax_inset.set_yticks([10, 20, 30, 40])
ax_inset.grid(True, linestyle=':', alpha=0.5)  # Changed grid style

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()