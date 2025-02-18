import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
solar = [20, 25, 30, 40, 50, 65, 80, 100, 130, 160]
wind = [50, 55, 60, 80, 100, 120, 150, 180, 210, 240]
hydro = [100, 100, 110, 115, 120, 125, 130, 135, 140, 145]
bio = [30, 35, 40, 50, 55, 65, 75, 85, 95, 100]

energy_data = np.vstack([solar, wind, hydro, bio])

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, energy_data, labels=['Sol', 'Wnd', 'Hdr', 'Bio'],
             colors=['#ffd700', '#00bfff', '#228b22', '#d2691e'], alpha=0.8)

ax.set_title('Ren Energy Use 2010-19', fontsize=14, fontweight='bold')
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Energy (PJ)', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5)

ax.legend(loc='upper left', title='Sources', fontsize=10, title_fontsize='13')

plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()