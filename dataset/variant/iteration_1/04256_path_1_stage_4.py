import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

residential_population = [1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.3, 2.5, 2.9, 3.1]
green_space = [50, 55, 60, 70, 75, 80, 85, 90, 95, 100]
public_transport_usage = [100, 110, 120, 150, 160, 170, 175, 180, 185, 190]
average_commute_time = [40, 38, 37, 35, 33, 32, 30, 29, 28, 27]

fig, ax = plt.subplots(figsize=(14, 8))

color = 'b'  

ax.plot(years, residential_population, marker='o', color=color)
ax.plot(years, green_space, marker='s', color=color)
ax.plot(years, public_transport_usage, marker='^', color=color)
ax.plot(years, average_commute_time, marker='x', color=color)

plt.xticks(years, fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()