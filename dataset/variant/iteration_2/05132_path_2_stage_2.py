import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

san_francisco_temps = np.array([17, 12, 14, 11, 16, 13, 18, 18, 15, 17, 12, 11])
new_york_temps = np.array([7, 2, 18, 0, 10, 24, 27, 26, 22, 13, 16, 4])
tokyo_temps = np.array([22, 5, 6, 10, 9, 15, 19, 27, 24, 19, 14, 6])
paris_temps = np.array([9, 6, 5, 12, 22, 19, 21, 6, 18, 14, 16, 9])
sydney_temps = np.array([20, 23, 22, 22, 16, 19, 14, 13, 16, 23, 18, 14])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, san_francisco_temps, label='San Francisco', color='navy', marker='o', linestyle='-')
ax.plot(months, new_york_temps, label='New York', color='maroon', marker='o', linestyle='-')
ax.plot(months, tokyo_temps, label='Tokyo', color='forestgreen', marker='o', linestyle='-')
ax.plot(months, paris_temps, label='Paris', color='firebrick', marker='o', linestyle='-')
ax.plot(months, sydney_temps, label='Sydney', color='darkgoldenrod', marker='o', linestyle='-')

ax.set_title('Average Monthly Temperatures for Five Major Cities in 2022', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

ax.legend(title='Cities', fontsize=12, title_fontsize=14, loc='upper right')
ax.grid(True, linestyle='--', alpha=0.7)

for (month, temp_san_francisco) in zip(months, san_francisco_temps):
    if temp_san_francisco in [11, 18]:
        ax.annotate(f'{temp_san_francisco}°C', xy=(month, temp_san_francisco), xytext=(5, -15), 
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', lw=1))

plt.tight_layout()
plt.show()