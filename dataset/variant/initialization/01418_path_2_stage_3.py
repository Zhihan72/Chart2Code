import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2051)

# Original data sequences have been shuffled manually
exoplanet_surveys = [0, 130, 50, 240, 300, 420, 80, 490, 790, 710, 180, 1150, 240, 1350, 870, 2310, 1350, 360, 1050, 1570, 10, 2050, 2450, 1920, 1150, 960, 1050, 1460, 420, 1680, 300]

black_hole_probes = [0, 35, 190, 60, 90, 1250, 150, 680, 1040, 950, 1740, 39, 120, 1140, 520, 15, 2020, 390, 770, 2170, 2330, 860, 450, 1880, 5, 330, 1250, 1480, 230, 280, 1]

nebula_studies = [0, 1060, 2380, 20, 8, 2810, 410, 150, 1340, 1640, 2590, 45, 700, 2180, 930, 410, 1480, 1060, 1330, 3530, 200, 3040, 300, 75, 1190, 1700, 2590, 75, 1810, 1060, 38]

cosmic_radiation_monitoring = [0, 460, 105, 3250, 1720, 790, 2320, 3021, 65, 1540, 1370, 1910, 60, 3540, 30, 3270, 4571, 4016, 3269, 3010, 3200, 220, 1921, 2770, 12, 1570, 2770, 3260, 3210, 2340, 3540]

fig, ax = plt.subplots(figsize=(12, 7))

colors = ['#8c564b', '#ff7f0e', '#2ca02c', '#1f77b4']

ax.stackplot(years, exoplanet_surveys, black_hole_probes, nebula_studies, cosmic_radiation_monitoring,
             labels=['Exoplanet Surveys', 'Black Hole Probes', 'Nebula Studies', 'Cosmic Radiation Monitoring'],
             colors=colors, alpha=0.75)

ax.set_title("Galactic Exploration Missions Evolution (2020-2050)", fontsize=15, fontweight='bold', pad=18)
ax.set_xlabel("Year", fontsize=11)
ax.set_ylabel("Cumulative Exploration Hours", fontsize=11)

ax.set_xticks(years[::5])
ax.tick_params(axis='x', rotation=30)

ax.legend(loc='lower right', title="Categories", fontsize=9)

ax.grid(True, linestyle=':', alpha=0.4)

plt.tight_layout()

plt.show()