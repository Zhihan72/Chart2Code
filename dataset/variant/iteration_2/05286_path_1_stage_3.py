import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2025)

solar_power = np.array([10, 12, 15, 18, 25, 35, 45, 60, 80, 100, 120, 140, 165, 190, 215, 240, 275, 300, 340, 400, 450, 500, 550, 600, 650])
wind_power = np.array([5, 8, 12, 20, 30, 45, 55, 80, 110, 150, 200, 250, 300, 350, 400, 460, 520, 600, 700, 800, 900, 1000, 1100, 1150, 1200])
hydro_power = np.array([180, 182, 185, 188, 190, 195, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 275, 280])
geothermal = np.array([30, 32, 34, 37, 40, 45, 50, 55, 60, 70, 80, 90, 95, 100, 110, 120, 130, 140, 150, 155, 160, 165, 170, 172, 175])
bioenergy = np.array([50, 52, 55, 58, 63, 70, 75, 80, 90, 100, 110, 125, 130, 135, 140, 145, 150, 155, 170, 180, 190, 195, 200, 205, 210])

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