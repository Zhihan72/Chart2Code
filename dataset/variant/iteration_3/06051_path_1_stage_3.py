import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

alpha_city_aqi = np.array([120, 135, 115, 125, 85, 110, 95, 140, 130, 100, 90, 105])
beta_town_aqi = np.array([130, 145, 140, 95, 105, 100, 150, 125, 120, 135, 110, 115])
gamma_ville_aqi = np.array([140, 155, 130, 160, 115, 135, 145, 150, 125, 120, 110, 105])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, alpha_city_aqi, label='ZoneAlpha', color='blue', marker='o', linestyle='-', linewidth=2)
ax1.plot(months, beta_town_aqi, label='SectorBeta', color='blue', marker='s', linestyle='--', linewidth=2)
ax1.plot(months, gamma_ville_aqi, label='RegionGamma', color='blue', marker='^', linestyle=':', linewidth=2)

ax1.fill_between(months, alpha_city_aqi, color='blue', alpha=0.1)
ax1.fill_between(months, beta_town_aqi, color='blue', alpha=0.1)
ax1.fill_between(months, gamma_ville_aqi, color='blue', alpha=0.1)

ax1.set_title('2023 Air Index Trends\nZoneAlpha, SectorBeta & RegionGamma', fontsize=16, fontweight='bold')
ax1.set_xlabel('Monthly Breakdown', fontsize=14)
ax1.set_ylabel('AQI Measurement', fontsize=14)

ax1.axhline(y=50, color='grey', linewidth=1.5, linestyle='--')
ax1.axhline(y=100, color='gold', linewidth=1.5, linestyle='--')
ax1.axhline(y=150, color='orange', linewidth=1.5, linestyle='--')
ax1.axhline(y=200, color='red', linewidth=1.5, linestyle='--')
ax1.axhline(y=300, color='purple', linewidth=1.5, linestyle='--')

ax1.grid(True, linestyle='--', alpha=0.7)

for city, aqi in [('ZoneAlpha', alpha_city_aqi),
                  ('SectorBeta', beta_town_aqi),
                  ('RegionGamma', gamma_ville_aqi)]:
    max_aqi = aqi.max()
    min_aqi = aqi.min()
    ax1.annotate(f"Highest: {max_aqi}", 
                 (months[aqi.argmax()], max_aqi), 
                 textcoords="offset points", xytext=(-30, 10), fontsize=10, color='blue')
    ax1.annotate(f"Lowest: {min_aqi}", 
                 (months[aqi.argmin()], min_aqi), 
                 textcoords="offset points", xytext=(-30, -20), fontsize=10, color='blue')

alpha_improvement = (alpha_city_aqi[0] - alpha_city_aqi[-1]) / alpha_city_aqi[0] * 100
beta_improvement = (beta_town_aqi[0] - beta_town_aqi[-1]) / beta_town_aqi[0] * 100
gamma_improvement = (gamma_ville_aqi[0] - gamma_ville_aqi[-1]) / gamma_ville_aqi[0] * 100

improvements = np.array([alpha_improvement, beta_improvement, gamma_improvement])
cities = ['ZoneAlpha', 'SectorBeta', 'RegionGamma']
ax2 = ax1.twinx()
ax2.bar(cities, improvements, color='blue', alpha=0.5, width=0.4, label='Improvement Rate')
ax2.set_ylabel('Percentage Change in AQI (%)', fontsize=12, color='darkslategray')

ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()