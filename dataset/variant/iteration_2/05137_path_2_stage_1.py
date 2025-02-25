import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

solar = np.array([5, 8, 15, 20, 30, 45, 60, 80, 100, 130, 170, 220, 280, 350, 430, 520, 620, 730, 850, 980, 1120])
wind = np.array([10, 15, 25, 35, 50, 70, 95, 120, 150, 185, 225, 270, 320, 375, 435, 500, 570, 645, 725, 810, 900])
hydro = np.array([20, 22, 25, 30, 35, 41, 48, 56, 65, 75, 86, 98, 111, 125, 140, 156, 173, 191, 210, 230, 251])
biomass = np.array([2, 3, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95, 109, 124, 140, 157, 175, 194])
geothermal = np.array([1, 1.5, 2, 3, 4, 5.5, 7, 9, 11, 14, 17, 21, 25, 30, 35, 41, 47, 54, 61, 69, 77])

plt.figure(figsize=(20, 12))
plt.stackplot(years, solar, wind, hydro, biomass, geothermal, 
              labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'],
              colors=['#ffbb33', '#29b6f6', '#66bb6a', '#8d6e63', '#ef5350'], alpha=0.8)

plt.title("Renewable Energy Adoption in Eco-friendly City (2010 - 2030)", 
          fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Installed Capacity (MW)", fontsize=14)

# Randomly altered legend position and removed title
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fontsize=12)

# Randomly changed grid line style and color
plt.grid(linestyle='-.', linewidth=0.8, color='grey')

plt.annotate('Solar Energy Boom', xy=(2020, 30), xytext=(2015, 300),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, backgroundcolor='w')
plt.annotate('Steady Growth in Wind Energy', xy=(2015, 75), xytext=(2010, 500),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, backgroundcolor='w')

plt.tight_layout()

fig, ax = plt.subplots(figsize=(20, 6))
solar_growth_rate = np.gradient(solar[:-1], years[:-1]) / solar[:-1] * 100  
# Changed the marker type and line style
ax.plot(years[:-1], solar_growth_rate, marker='o', linestyle='-', color='#ffbb33', label='Solar Energy Growth Rate', linewidth=2.5)
ax.axvline(2020, color='gray', linestyle='-', lw=1.5, label='Key Year: 2020')
ax.set_title("Annual Growth Rate of Solar Energy Capacity", fontsize=18, pad=15, weight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Growth Rate (%)", fontsize=14)
ax.legend(loc='lower right', fontsize=12)

plt.tight_layout()
plt.show()