import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
solar = np.array([50, 70, 100, 150, 210, 300, 420, 550, 700, 850, 1000])
wind = np.array([30, 50, 80, 120, 160, 200, 250, 310, 350, 400, 450])
hydro = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150])

total_consumption = solar + wind + hydro
solar_share = (solar / total_consumption) * 100
wind_share = (wind / total_consumption) * 100
hydro_share = (hydro / total_consumption) * 100

fig, axs = plt.subplots(2, 1, figsize=(10, 12))

axs[0].stackplot(years, solar, wind, hydro, colors=['#32CD32', '#8B4513', '#FFD700'], alpha=0.85)
axs[0].legend(loc='upper right')
axs[0].grid(True, linestyle='-.', alpha=0.5)
axs[0].set_xticks(years)
axs[0].set_xlim(2015, 2025)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)

axs[1].plot(years, solar_share, color='#32CD32', marker='x')
axs[1].plot(years, wind_share, color='#8B4513', marker='v')
axs[1].plot(years, hydro_share, color='#FFD700', marker='p')
axs[1].legend(loc='lower left')
axs[1].grid(True, linestyle=':', alpha=0.9)
axs[1].set_xticks(years)
axs[1].set_xlim(2015, 2025)
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.show()