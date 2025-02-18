import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

sf_temps = np.array([18, 13, 17, 11, 16, 14, 12, 18, 15, 12, 17, 11])
ny_temps = np.array([10, 27, 4, 0, 24, 13, 2, 22, 18, 7, 16, 26])
tk_temps = np.array([19, 26, 15, 14, 22, 27, 10, 6, 9, 5, 24, 19])
pa_temps = np.array([22, 5, 12, 9, 16, 21, 14, 19, 9, 18, 6, 6])
sy_temps = np.array([14, 23, 22, 19, 20, 16, 18, 13, 14, 16, 23, 22])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, sf_temps, color='tab:blue', marker='o', linestyle='-')
ax.plot(months, ny_temps, color='tab:blue', marker='o', linestyle='-')
ax.plot(months, tk_temps, color='tab:blue', marker='o', linestyle='-')
ax.plot(months, pa_temps, color='tab:blue', marker='o', linestyle='-')
ax.plot(months, sy_temps, color='tab:blue', marker='o', linestyle='-')

ax.set_title('Avg Monthly Temps 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Temp (°C)', fontsize=14)

plt.tight_layout()
plt.show()