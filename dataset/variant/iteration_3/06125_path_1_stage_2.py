import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Noachis', 'Hellas', 'Solis', 'Tharsis', 'Amazonis', 'Elysium', 'Planum', 'Arcadia', 'Acidalia', 'Arabia', 'Elysium II', 'Thaumasia'])
mars_day = np.linspace(1, 12, num=12)

north_temp = np.array([-60, -50, -45, -30, -35, -40, -55, -65, -70, -75, -80, -85])
south_temp = np.array([-65, -55, -50, -35, -40, -45, -60, -70, -75, -80, -85, -90])
equator_temp = np.array([-50, -45, -40, -30, -32, -35, -42, -50, -55, -60, -65, -70])
highlands_temp = np.array([-70, -60, -55, -40, -45, -50, -65, -75, -80, -85, -90, -95])
lowlands_temp = np.array([-55, -45, -40, -25, -30, -35, -50, -60, -65, -70, -75, -80])

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffle colors by changing color assignment for each data group
ax.plot(mars_day, north_temp, marker='o', color='m', label='Northern Hemisphere', linewidth=2)
ax.plot(mars_day, south_temp, marker='s', color='g', label='Southern Hemisphere', linewidth=2)
ax.plot(mars_day, equator_temp, marker='^', color='c', label='Equatorial Region', linewidth=2)
ax.plot(mars_day, highlands_temp, marker='D', color='r', label='Highlands', linewidth=2)
ax.plot(mars_day, lowlands_temp, marker='x', color='b', label='Lowlands', linewidth=2)

ax.set_title("Seasonal Temperature Variations on Mars", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Martian Months", fontsize=12)
ax.set_ylabel("Surface Temperature (°C)", fontsize=12)

ax.set_xticks(mars_day)
ax.set_xticklabels(months, rotation=45, ha='right')
ax.set_yticks(np.arange(-95, -20, 5))
ax.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(loc='upper right', fontsize=12, title='Mars Zones', title_fontsize='13', frameon=True)

ax.annotate('Warmest point\n(Northern Hemisphere)', xy=(4, -30), xytext=(6, -25),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')
ax.annotate('Coldest point\n(Southern Hemisphere)', xy=(12, -90), xytext=(10, -85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')

plt.tight_layout()
plt.show()