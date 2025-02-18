import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

alpha_city_aqi = np.array([140, 135, 130, 125, 120, 115, 110, 105, 100, 95, 90, 85])
beta_town_aqi = np.array([150, 145, 140, 135, 130, 125, 120, 115, 110, 105, 100, 95])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, alpha_city_aqi, label='AlphaCity', color='blue', marker='o', linestyle='-', linewidth=2)
ax1.plot(months, beta_town_aqi, label='BetaTown', color='green', marker='s', linestyle='--', linewidth=2)

ax1.fill_between(months, alpha_city_aqi, color='blue', alpha=0.1)
ax1.fill_between(months, beta_town_aqi, color='green', alpha=0.1)

ax1.set_title('Yearly Air Quality Index Variations in 2023\nAlphaCity & BetaTown', fontsize=16, fontweight='bold')
ax1.set_xlabel('Months', fontsize=14)
ax1.set_ylabel('Air Quality Index (AQI)', fontsize=14)

ax1.axhline(y=50, color='grey', linewidth=1.5, linestyle='--')
ax1.axhline(y=100, color='gold', linewidth=1.5, linestyle='--')
ax1.axhline(y=150, color='orange', linewidth=1.5, linestyle='--')
ax1.axhline(y=200, color='red', linewidth=1.5, linestyle='--')
ax1.axhline(y=300, color='purple', linewidth=1.5, linestyle='--')

ax1.grid(True, linestyle='--', alpha=0.7)

for city, aqi, color in [('AlphaCity', alpha_city_aqi, 'blue'),
                         ('BetaTown', beta_town_aqi, 'green')]:
    max_aqi = aqi.max()
    min_aqi = aqi.min()
    ax1.annotate(f"High: {max_aqi}", 
                 (months[aqi.argmax()], max_aqi), 
                 textcoords="offset points", xytext=(-30, 10), fontsize=10, color=color)
    ax1.annotate(f"Low: {min_aqi}", 
                 (months[aqi.argmin()], min_aqi), 
                 textcoords="offset points", xytext=(-30, -20), fontsize=10, color=color)

ax2 = ax1.twinx()
alpha_improvement = (alpha_city_aqi[0] - alpha_city_aqi[-1]) / alpha_city_aqi[0] * 100
beta_improvement = (beta_town_aqi[0] - beta_town_aqi[-1]) / beta_town_aqi[0] * 100

improvements = np.array([alpha_improvement, beta_improvement])
cities = ['AlphaCity', 'BetaTown']
ax2.bar(cities, improvements, color=['blue', 'green'], alpha=0.5, width=0.4, label='Improvement %')
ax2.set_ylabel('AQI Improvement Percentage (%)', fontsize=12, color='darkslategray')

ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()