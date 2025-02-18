import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
solar_power = np.array([125, 140, 160, 180, 205, 230, 260, 290, 320, 355, 390])
wind_power = np.array([150, 170, 195, 220, 250, 280, 315, 350, 385, 420, 460])
hydropower = np.array([200, 210, 220, 230, 250, 270, 290, 310, 330, 350, 370])
geothermal = np.array([30, 33, 35, 38, 42, 45, 50, 55, 60, 65, 70])
biomass = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
CO2_reduction = np.array([100, 120, 140, 160, 185, 210, 240, 270, 300, 340, 380])
deforestation_prevented = np.array([50, 55, 63, 70, 80, 90, 100, 115, 130, 150, 170])

cumulative_wind = solar_power + wind_power
cumulative_hydropower = cumulative_wind + hydropower
cumulative_geothermal = cumulative_hydropower + geothermal
cumulative_biomass = cumulative_geothermal + biomass

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

ax1.fill_between(years, 0, solar_power, color='#FFD700', alpha=0.7)
ax1.fill_between(years, solar_power, cumulative_wind, color='#00BFFF', alpha=0.7)
ax1.fill_between(years, cumulative_wind, cumulative_hydropower, color='#008000', alpha=0.7)
ax1.fill_between(years, cumulative_hydropower, cumulative_geothermal, color='#FF6347', alpha=0.7)
ax1.fill_between(years, cumulative_geothermal, cumulative_biomass, color='#8B4513', alpha=0.7)

ax2.plot(years, CO2_reduction, color='blue', linewidth=2.5, marker='o')
ax2.plot(years, deforestation_prevented, color='green', linewidth=2.5, marker='s')

plt.tight_layout()
plt.show()