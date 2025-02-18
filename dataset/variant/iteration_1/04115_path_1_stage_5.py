import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2035)

moon_landings = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
mars_landings = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 16))

new_colors = ['#4B0082', '#008B8B']

ax1.stackplot(years, moon_landings, mars_landings, 
              colors=new_colors, alpha=0.8)
ax1.set_title("Galactic Quest Expeditions\nTriumphant Touchdowns (2020-2035)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Chronology", fontsize=14)
ax1.set_ylabel("Tally of Descents", fontsize=14)
ax1.set_xticks(years[::1])
ax1.tick_params(axis='x', rotation=45)

moon_growth_rate = np.gradient(moon_landings) / moon_landings * 100
mars_growth_rate = np.gradient(mars_landings) / mars_landings * 100

ax2.plot(years, moon_growth_rate, color=new_colors[0], marker='o')
ax2.plot(years, mars_growth_rate, color=new_colors[1], marker='o')
ax2.set_title("Annual Leap of Victorious Landings\n(2020-2035)", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Chronology", fontsize=14)
ax2.set_ylabel("Increment Rate (%)", fontsize=14)
ax2.set_xticks(years[::1])
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()