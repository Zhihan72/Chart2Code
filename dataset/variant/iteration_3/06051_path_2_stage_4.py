import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

alpha_city_aqi = np.array([140, 135, 130, 125, 120, 115, 110, 105, 100, 95, 90, 85])
beta_town_aqi = np.array([150, 145, 140, 135, 130, 125, 120, 115, 110, 105, 100, 95])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the AQI values
ax1.plot(months, alpha_city_aqi, color='blue', marker='o', linestyle='-', linewidth=2)
ax1.plot(months, beta_town_aqi, color='blue', marker='s', linestyle='--', linewidth=2)

# Removing filled areas
ax1.fill_between(months, alpha_city_aqi, color='blue', alpha=0)
ax1.fill_between(months, beta_town_aqi, color='blue', alpha=0)

# Air quality index reference lines
ax1.axhline(y=50, color='grey', linewidth=1.5, linestyle='--')
ax1.axhline(y=100, color='gold', linewidth=1.5, linestyle='--')
ax1.axhline(y=150, color='orange', linewidth=1.5, linestyle='--')
ax1.axhline(y=200, color='red', linewidth=1.5, linestyle='--')
ax1.axhline(y=300, color='purple', linewidth=1.5, linestyle='--')

# Removed grid
# ax1.grid(True, linestyle='--', alpha=0.7)

ax2 = ax1.twinx()
alpha_improvement = (alpha_city_aqi[0] - alpha_city_aqi[-1]) / alpha_city_aqi[0] * 100
beta_improvement = (beta_town_aqi[0] - beta_town_aqi[-1]) / beta_town_aqi[0] * 100

improvements = np.array([alpha_improvement, beta_improvement])
cities = ['AlphaCity', 'BetaTown']
ax2.bar(cities, improvements, color='blue', alpha=0.5, width=0.4)

plt.tight_layout()
plt.show()