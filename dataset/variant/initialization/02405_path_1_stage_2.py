import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

solar = [74, 8, 35, 80, 22, 5, 60, 68, 40, 52, 30]
wind = [70, 10, 23, 5, 3, 75, 45, 35, 63, 16, 55]
geothermal = [20, 1, 15, 25, 10, 35, 5, 30, 7, 3, 2]

plt.figure(figsize=(12, 8))

# Shuffled color assignment
plt.plot(years, solar, marker='o', color='skyblue', linestyle='-', linewidth=2, label='Solar Energy')
plt.plot(years, wind, marker='s', color='lightcoral', linestyle='-', linewidth=2, label='Wind Energy')
plt.plot(years, geothermal, marker='^', color='gold', linestyle='-', linewidth=2, label='Geothermal Energy')

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