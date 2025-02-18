import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2051)

exoplanet_surveys = [0, 10, 25, 50, 80, 130, 180, 240, 300, 360, 420, 490, 560, 640, 710, 790, 870, 960, 1050, 1150, 1250, 1350, 1460, 1570, 1680, 1800, 1920, 2050, 2180, 2310, 2450]
black_hole_probes = [0, 5, 15, 35, 60, 90, 120, 150, 190, 230, 280, 330, 390, 450, 520, 600, 680, 770, 860, 950, 1040, 1140, 1250, 1360, 1480, 1610, 1740, 1880, 2020, 2170, 2330]
nebula_studies = [0, 8, 20, 45, 75, 110, 150, 200, 260, 330, 410, 500, 600, 700, 810, 930, 1060, 1190, 1330, 1480, 1640, 1810, 1990, 2180, 2380, 2590, 2810, 3040, 3280, 3530, 3790]
cosmic_radiation_monitoring = [0, 12, 30, 65, 105, 160, 220, 290, 370, 460, 560, 670, 790, 920, 1060, 1210, 1370, 1540, 1720, 1910, 2110, 2320, 2540, 2770, 3010, 3260, 3520, 3790, 4070, 4360, 4660]

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, exoplanet_surveys, black_hole_probes, nebula_studies, cosmic_radiation_monitoring,
             labels=['Exoplanet Surveys', 'Black Hole Probes', 'Nebula Studies', 'Cosmic Radiation Monitoring'],
             colors=['#1f77b4', '#8c564b', '#2ca02c', '#ff7f0e'], alpha=0.75)

ax.set_title("Galactic Exploration Missions Evolution (2020-2050)", fontsize=15, fontweight='bold', pad=18)
ax.set_xlabel("Year", fontsize=11)
ax.set_ylabel("Cumulative Exploration Hours", fontsize=11)

ax.set_xticks(years[::5])
ax.tick_params(axis='x', rotation=30)

ax.legend(loc='lower right', title="Categories", fontsize=9)

ax.grid(True, linestyle=':', alpha=0.4)

plt.tight_layout()

plt.show()