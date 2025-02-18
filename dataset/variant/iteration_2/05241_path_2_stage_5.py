import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

# Original data
solar_power_original = np.array([125, 140, 160, 180, 205, 230, 260, 290, 320, 355, 390])
wind_power_original = np.array([150, 170, 195, 220, 250, 280, 315, 350, 385, 420, 460])
hydropower_original = np.array([200, 210, 220, 230, 250, 270, 290, 310, 330, 350, 370])
geothermal_original = np.array([30, 33, 35, 38, 42, 45, 50, 55, 60, 65, 70])
biomass_original = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

# Randomly altered data (shuffled within each array)
# This should be done manually, keeping the dimensional structure intact.
solar_power = np.array([160, 125, 230, 205, 355, 180, 260, 390, 140, 320, 290])
wind_power = np.array([460, 385, 150, 315, 250, 170, 350, 195, 220, 420, 280])
hydropower = np.array([310, 270, 230, 250, 370, 330, 200, 220, 350, 290, 210])
geothermal = np.array([70, 50, 42, 30, 38, 55, 33, 60, 65, 35, 45])
biomass = np.array([45, 70, 55, 35, 25, 30, 65, 50, 60, 40, 20])

CO2_reduction = np.array([100, 120, 140, 160, 185, 210, 240, 270, 300, 340, 380])
deforestation_prevented = np.array([50, 55, 63, 70, 80, 90, 100, 115, 130, 150, 170])

cumulative_wind = solar_power + wind_power
cumulative_hydropower = cumulative_wind + hydropower
cumulative_geothermal = cumulative_hydropower + geothermal
cumulative_biomass = cumulative_geothermal + biomass

fig, (ax2, ax1) = plt.subplots(2, 1, figsize=(14, 10))

ax2.plot(years, CO2_reduction, color='crimson', linewidth=1.5, marker='^')
ax2.plot(years, deforestation_prevented, color='teal', linewidth=1.5, marker='D')
ax2.grid(False)

ax1.fill_between(years, 0, solar_power, color='#4682B4', alpha=0.5)
ax1.fill_between(years, solar_power, cumulative_wind, color='#32CD32', alpha=0.5)
ax1.fill_between(years, cumulative_wind, cumulative_hydropower, color='#FFA500', alpha=0.5)
ax1.fill_between(years, cumulative_hydropower, cumulative_geothermal, color='#800080', alpha=0.5)
ax1.fill_between(years, cumulative_geothermal, cumulative_biomass, color='#FF1493', alpha=0.5)
ax1.grid(False)

plt.tight_layout()
plt.show()