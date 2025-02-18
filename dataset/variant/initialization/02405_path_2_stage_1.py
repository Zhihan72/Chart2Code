import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
solar = [5, 8, 15, 22, 30, 40, 52, 60, 68, 74, 80]
wind = [3, 5, 10, 16, 23, 35, 45, 55, 63, 70, 75]
geothermal = [1, 2, 3, 5, 7, 10, 15, 20, 25, 30, 35]

plt.figure(figsize=(12, 8))

# Applying a single consistent color 'forestgreen'
plt.plot(years, solar, marker='o', color='forestgreen', linestyle='-', linewidth=2, label='Solar Energy')
plt.plot(years, wind, marker='s', color='forestgreen', linestyle='-', linewidth=2, label='Wind Energy')
plt.plot(years, geothermal, marker='^', color='forestgreen', linestyle='-', linewidth=2, label='Geothermal Energy')

plt.annotate('Solar tax incentives', xy=(2014, solar[4]), xytext=(2014, solar[4] + 10),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, ha='right')
plt.annotate('Wind turbine breakthroughs', xy=(2016, wind[6]), xytext=(2016, wind[6] + 10),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, ha='right')
plt.annotate('Geothermal tech advancements', xy=(2018, geothermal[8]), xytext=(2018, geothermal[8] + 10),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, ha='right')

plt.title('Sustainable Energy Adoption\nFrom 2010 to 2020', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Adoption Rate (%)', fontsize=14)
plt.xticks(years)
plt.yticks(range(0, 101, 10))
plt.legend(loc='upper left', title='Energy Source')

plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()