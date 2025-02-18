import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Data preparation
years = np.arange(2010, 2021)
solar_power = np.array([30, 45, 70, 100, 150, 225, 320, 430, 560, 700, 850])
total_power = solar_power  # With wind removed, total_power is the same as solar_power
solar_percentage = (solar_power / total_power) * 100  # With wind removed, solar is 100%

fig, ax = plt.subplots(figsize=(14, 8))

# Define new color scheme
new_color = '#1f77b4'  # A common matplotlib color for a change

# Plot solar power with gradient-like effect by adjusting alpha
for i in range(len(years) - 1):
    ax.plot(years[i:i + 2], solar_power[i:i + 2], marker='o', linestyle='-', color=new_color, linewidth=2, alpha=(i + 1) / len(years))

# Titles and labels
ax.set_title('The Rise of Renewable Energy:\nSolar Power Trends (2010-2020)', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (TWh)', fontsize=12)

# Customize the x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 901, 100))

# Add a legend
ax.legend(['Solar Power'], title='Energy Source', loc='upper left')

# Annotate each data point with its value
for i, y_solar in enumerate(solar_power):
    ax.text(years[i], y_solar + 20, f'{y_solar}', ha='center', fontsize=9, color=new_color)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.7)

# Inset plot: Percentage share of solar (only solar)
ax_inset = inset_axes(ax, width="30%", height="30%", loc='lower right', borderpad=2)
ax_inset.plot(years, solar_percentage, color=new_color, linewidth=1.5, label='Solar %')
ax_inset.set_title('Share of Total (%)', fontsize=10)
ax_inset.set_xticks([2010, 2015, 2020])
ax_inset.set_yticks([100])  # Only solar is present, so percentage is always 100
ax_inset.grid(True, linestyle='--', alpha=0.5)
ax_inset.legend(fontsize=8, loc='upper left')

plt.tight_layout()
plt.show()