import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2025)

# Manually altering some entries in the data groups to preserve the original dimensional structure
solar_power = np.array([10, 25, 15, 18, 40, 35, 70, 60, 60, 100, 130, 140, 165, 220, 215, 240, 275, 300, 340, 400, 410, 480, 550, 570, 652])
wind_power = np.array([50, 8, 12, 30, 30, 65, 55, 60, 110, 160, 200, 250, 340, 310, 390, 460, 520, 500, 700, 800, 850, 950, 1100, 1130, 1200])
hydro_power = np.array([180, 187, 185, 188, 190, 198, 195, 195, 205, 210, 219, 223, 225, 225, 238, 240, 245, 240, 250, 260, 263, 271, 275, 278, 280])
geothermal = np.array([30, 34, 34, 37, 42, 45, 53, 55, 68, 70, 75, 95, 85, 115, 110, 125, 138, 140, 120, 155, 160, 163, 175, 172, 168])
bioenergy = np.array([52, 52, 63, 58, 63, 73, 75, 85, 90, 92, 115, 125, 140, 130, 143, 150, 148, 155, 175, 170, 200, 195, 205, 203, 210])

energy_data = np.vstack([solar_power, wind_power, hydro_power, geothermal, bioenergy])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#add8e6', '#9acd32', '#ffcccb', '#69b3a2', '#ffa500']

ax.stackplot(years, energy_data, labels=['Bio', 'Geo', 'Hydro', 'Wind', 'Solar'], colors=colors, alpha=0.8)

ax.set_title('Trends in Green Energy (2000-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, color='darkblue')
ax.set_ylabel('Adoption Level', fontsize=12, color='brown')

ax.legend(loc='lower right', fontsize=9, title='Energy Types', frameon=True)
ax.grid(linestyle=':', alpha=0.4, color='green')

plt.xticks(years, rotation=30)
plt.yticks(np.arange(0, 1301, 100), fontsize=9)

ax.annotate('Solar Spike', xy=(2010, 100), xytext=(2005, 250),
            arrowprops=dict(facecolor='red', arrowstyle='-[', lw=1.5), fontsize=9, color='purple')

ax.annotate('Wind Growth', xy=(2015, 250), xytext=(2010, 600),
            arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3', color='orange', lw=1.5),
            fontsize=9, color='darkgreen')

description_box = dict(boxstyle='round', facecolor='wheat', alpha=0.4)
description = ("Shift in clean energy uptake is clear globally.\n"
               "Technology and policy advancements fuel the growth.")
ax.text(0.02, 0.95, description, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=description_box)

plt.tight_layout()
plt.show()