import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

dissolved_oxygen = [7.5, 7.2, 6.9, 6.7, 6.5, 6.2, 6.0, 5.8, 5.6, 5.5, 5.2]
ph_level = [7.0, 6.9, 6.8, 6.7, 6.5, 6.4, 6.3, 6.1, 6.0, 6.0, 5.9]
nitrate_concentration = [5, 5.5, 6, 6.2, 6.5, 7, 7.3, 7.5, 8, 8.2, 8.5]
water_temperature = [15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20]

fig, ax1 = plt.subplots(figsize=(14, 7))
ax2 = ax1.twinx()

ax1.plot(years, dissolved_oxygen, color='green', marker='x', linestyle='-', linewidth=1.5)
ax1.plot(years, ph_level, color='blue', marker='*', linestyle='-.', linewidth=1.5)
ax1.plot(years, water_temperature, color='purple', marker='o', linestyle='-', linewidth=1.5)
ax2.plot(years, nitrate_concentration, color='red', marker='d', linestyle='--', linewidth=1.5)

ax1.tick_params(axis='y', colors='green')
ax2.tick_params(axis='y', colors='red')
ax1.grid(visible=True, which='major', linestyle='-', linewidth=0.5, color='lightgrey', alpha=0.7)
fig.tight_layout()

plt.show()