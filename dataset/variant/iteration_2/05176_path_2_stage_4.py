import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

city_A_temps = [16.2, 16.5, 17.0, 17.3, 17.7, 18.1, 18.4, 18.7, 19.1, 19.5, 19.8, 20.2, 20.5]
city_C_temps = [10.5, 10.8, 11.2, 11.5, 11.9, 12.2, 12.6, 12.9, 13.3, 13.6, 14.0, 14.3, 14.7]

fig, ax = plt.subplots(figsize=(14, 8))

single_color = '#1f77b4'

ax.plot(years, city_A_temps, marker='o', linestyle='-', color=single_color, linewidth=2)
ax.plot(years, city_C_temps, marker='^', linestyle='-.', color=single_color, linewidth=2)

ax.set_xticks(years)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()