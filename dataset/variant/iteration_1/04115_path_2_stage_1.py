import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2020, 2035)

# Define the number of successful landings
moon_landings = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
mars_landings = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
venus_landings = np.array([1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Subplot 1: Stacked Area Chart for Landings
ax1.stackplot(years, moon_landings, mars_landings, venus_landings,
              labels=['Moon', 'Mars', 'Venus'],
              colors=['#FFD700', '#FF6347', '#1E90FF'], alpha=0.8)
ax1.set_title("Solar System Exploration Missions\nSuccessful Landings (2020-2035)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Number of Landings", fontsize=14)
ax1.set_xticks(years[::1])
ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left', title="Celestial Bodies", fontsize=12, bbox_to_anchor=(1, 1))
ax1.grid(True, linestyle='--', alpha=0.6)

# Subplot 2: Line Plot for Yearly Growth Rate
moon_growth_rate = np.gradient(moon_landings) / moon_landings * 100
mars_growth_rate = np.gradient(mars_landings) / mars_landings * 100
venus_growth_rate = np.gradient(venus_landings) / venus_landings * 100

ax2.plot(years, moon_growth_rate, label='Moon', color='#FFD700', marker='o')
ax2.plot(years, mars_growth_rate, label='Mars', color='#FF6347', marker='o')
ax2.plot(years, venus_growth_rate, label='Venus', color='#1E90FF', marker='o')
ax2.set_title("Yearly Growth Rate of Successful Landings\n(2020-2035)", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Year", fontsize=14)
ax2.set_ylabel("Growth Rate (%)", fontsize=14)
ax2.set_xticks(years[::1])
ax2.tick_params(axis='x', rotation=45)
ax2.legend(loc='upper left', title="Celestial Bodies", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()