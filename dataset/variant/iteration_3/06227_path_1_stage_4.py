import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

san_francisco_temps = np.array([10, 12, 14, 15, 17, 18, 19, 19, 20, 18, 15, 12])
new_york_temps = np.array([0, 1, 5, 10, 16, 20, 24, 24, 20, 15, 10, 5])
miami_temps = np.array([20, 22, 24, 26, 28, 30, 32, 32, 30, 28, 25, 22])
seattle_temps = np.array([5, 6, 9, 12, 15, 18, 20, 21, 18, 13, 9, 5])
san_diego_temps = np.array([13, 14, 15, 17, 19, 21, 22, 22, 21, 19, 16, 14])
honolulu_temps = np.array([23, 23, 24, 25, 26, 27, 28, 29, 28, 27, 25, 24])

plt.figure(figsize=(14, 8))

plt.plot(months, san_francisco_temps, marker='v', linestyle='--', color='darkred', label='San Francisco')
plt.plot(months, new_york_temps, marker='>', linestyle=':', color='dodgerblue', label='New York')
plt.plot(months, miami_temps, marker='o', linestyle='-.', color='darkgreen', label='Miami')
plt.plot(months, seattle_temps, marker='<', linestyle='-', color='gold', label='Seattle')
plt.plot(months, san_diego_temps, marker='*', linestyle='-', color='magenta', label='San Diego')
plt.plot(months, honolulu_temps, marker='s', linestyle='--', color='purple', label='Honolulu')

plt.grid(True, linestyle='-', alpha=0.5)

plt.legend(loc='upper left', fontsize='small', shadow=True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()