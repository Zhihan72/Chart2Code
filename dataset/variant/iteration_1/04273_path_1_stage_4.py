import matplotlib.pyplot as plt
import numpy as np

years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])

avg_temperature = np.array([15.2, 15.4, 15.6, 15.9, 16.0, 16.2, 16.4])
avg_precipitation = np.array([1100, 1120, 1090, 1150, 1180, 1200, 1225])
co2_levels = np.array([350, 360, 370, 380, 390, 400, 410])

fig, axs = plt.subplots(1, 3, figsize=(18, 5), constrained_layout=True)

# Temperature Trend
axs[0].plot(years, avg_temperature, color='purple', marker='o', linestyle='-', linewidth=2)

# Precipitation Trend
axs[1].plot(years, avg_precipitation, color='orange', marker='s', linestyle='-', linewidth=2)

# CO2 Levels Trend
axs[2].plot(years, co2_levels, color='brown', marker='^', linestyle='-', linewidth=2)

plt.show()