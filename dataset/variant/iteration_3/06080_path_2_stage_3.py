import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1990, 2021)
avg_temp = np.array([12.3, 12.1, 12.6, 13.0, 13.1, 12.9, 13.5, 13.8, 14.0, 
                     14.2, 13.7, 13.5, 13.9, 14.3, 14.5, 14.8, 15.2, 15.1, 
                     15.6, 15.7, 16.0, 16.2, 16.4, 16.5, 16.9, 17.0, 17.1, 
                     17.3, 17.5, 17.8, 18.0])

fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'tab:blue'
ax1.set_title('City Climate (1990-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Temp (°C)', fontsize=14, color=color)
ax1.plot(years, avg_temp, color=color, linestyle='-', linewidth=2, marker='o', label='Temp')
ax1.tick_params(axis='y', labelcolor=color)

ax1.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()