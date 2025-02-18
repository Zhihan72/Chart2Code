import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

residential_population = [1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.3, 2.5, 2.9, 3.1]
green_space = [50, 55, 60, 70, 75, 80, 85, 90, 95, 100]
public_transport_usage = [100, 110, 120, 150, 160, 170, 175, 180, 185, 190]
average_commute_time = [40, 38, 37, 35, 33, 32, 30, 29, 28, 27]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, residential_population, marker='v', color='red', linestyle='-')
ax.plot(years, green_space, marker='d', color='green', linestyle='-.')
ax.plot(years, public_transport_usage, marker='h', color='purple', linestyle=':')
ax.plot(years, average_commute_time, marker='*', color='orange', linestyle='--')

plt.xticks(years, rotation=45)
plt.grid(True, linestyle='-', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()