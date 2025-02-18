import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
average_temperatures = np.array([-10.5, -11.0, -9.8, -10.2, -11.3, -9.7, -10.5, -9.9, -10.1, -9.6])
temperature_std_dev = np.array([0.8, 1.1, 0.6, 0.9, 1.0, 0.7, 0.8, 1.2, 0.7, 0.9])

temp_indices = np.argsort(average_temperatures)
sorted_years_temp = years[temp_indices]
sorted_temperatures = average_temperatures[temp_indices]
sorted_temp_std_dev = temperature_std_dev[temp_indices]

fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(sorted_years_temp, sorted_temperatures, yerr=sorted_temp_std_dev, color='firebrick',
       ecolor='orangered', capsize=5, alpha=0.8)
ax.set_ylim(min(sorted_temperatures - sorted_temp_std_dev) - 1, 
            max(sorted_temperatures + sorted_temp_std_dev) + 1)
ax.grid(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()