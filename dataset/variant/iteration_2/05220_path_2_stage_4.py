import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
wind_energy = np.array([30, 35, 45, 60, 85, 120, 160, 210, 260, 320, 390])
hydro_energy = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, wind_energy, hydro_energy, 
             colors=['#FF4500', '#8A2BE2'], alpha=0.7)

ax.set_title("Energy Generation by Variants\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Output (GWh)', fontsize=14)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 1000)
ax.set_xticks(years)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()