import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

sf_temps = np.array([14, 19, 12, 15, 10, 18, 17, 19, 20, 12, 15, 18])
ny_temps = np.array([5, 10, 0, 24, 1, 16, 20, 24, 15, 5, 10, 20])
mia_temps = np.array([30, 22, 32, 20, 28, 24, 22, 25, 32, 26, 28, 24])
sea_temps = np.array([9, 21, 6, 5, 12, 15, 18, 13, 9, 20, 5, 18])
sd_temps = np.array([14, 19, 21, 13, 21, 19, 16, 22, 22, 15, 17, 14])

plt.figure(figsize=(14, 8))

plt.plot(months, sf_temps, marker='o', linestyle='-', color='cyan')
plt.plot(months, ny_temps, marker='s', linestyle='-', color='magenta')
plt.plot(months, mia_temps, marker='^', linestyle='-', color='yellow')
plt.plot(months, sea_temps, marker='D', linestyle='-', color='brown')
plt.plot(months, sd_temps, marker='x', linestyle='-', color='pink')

plt.title('Monthly Temp Trends in Coastal Cities', fontsize=18, fontweight='bold')
plt.xlabel('Mnth', fontsize=14)
plt.ylabel('Avg Temp (°C)', fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()