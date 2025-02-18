import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Shuffled temperature data while preserving the dimensional structure
san_francisco_temps = np.array([14, 19, 12, 15, 10, 18, 17, 19, 20, 12, 15, 18])
new_york_temps = np.array([5, 10, 0, 24, 1, 16, 20, 24, 15, 5, 10, 20])
miami_temps = np.array([30, 22, 32, 20, 28, 24, 22, 25, 32, 26, 28, 24])
seattle_temps = np.array([9, 21, 6, 5, 12, 15, 18, 13, 9, 20, 5, 18])
san_diego_temps = np.array([14, 19, 21, 13, 21, 19, 16, 22, 22, 15, 17, 14])

plt.figure(figsize=(14, 8))

plt.plot(months, san_francisco_temps, marker='o', linestyle='-', label='San Francisco', color='orange')
plt.plot(months, new_york_temps, marker='s', linestyle='-', label='New York', color='blue')
plt.plot(months, miami_temps, marker='^', linestyle='-', label='Miami', color='green')
plt.plot(months, seattle_temps, marker='D', linestyle='-', label='Seattle', color='purple')
plt.plot(months, san_diego_temps, marker='x', linestyle='-', label='San Diego', color='red')

plt.title('Monthly Temperature Trends in Coastal Cities\nAn Analysis of 2022', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Cities', title_fontsize=12, fontsize=10, loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()