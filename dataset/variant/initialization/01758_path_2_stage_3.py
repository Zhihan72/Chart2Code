import matplotlib.pyplot as plt
import numpy as np

percentages = [40, 25, 10, 15, 10]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#F3FF33']
explode = (0.1, 0.1, 0.2, 0, 0)  # Increased explode on the third slice

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

# Altered pie chart styles
ax.pie(
    percentages, 
    colors=colors, 
    startangle=110,  # Random start angle
    wedgeprops=dict(width=0.35, edgecolor='k', linewidth=3, linestyle='-', alpha=0.8),  # Changed edge color, linewidth, and added linestyle
    shadow=False,  # Removed shadow
    explode=explode
)

centre_circle = plt.Circle((0, 0), 0.65, fc='gray', edgecolor='gray', linewidth=2)  # Changed center circle's color and linewidth
ax.add_artist(centre_circle)

ax_inset = fig.add_axes([0.7, 0.55, 0.25, 0.35])  # Adjusted inset position
years = [2020, 2030, 2040, 2050]
solar_trend = [20, 30, 35, 40]
nuclear_trend = [15, 20, 23, 25]
ax_inset.plot(years, solar_trend, 'b--^', label='Solar')  # Changed line style and marker
ax_inset.plot(years, nuclear_trend, 'r-.*', label='Nuclear')  # Changed line style and marker
ax_inset.legend(loc='upper left', fontsize='small', frameon=False)  # Modified legend properties
ax_inset.set_xticks(years)
ax_inset.set_yticks([10, 20, 30, 40])
ax_inset.grid(True, linestyle=':', color='gray', alpha=0.7)  # Changed grid line style and color

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()