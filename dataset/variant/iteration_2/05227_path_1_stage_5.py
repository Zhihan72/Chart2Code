import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
startups_founded = [50, 55, 60, 85, 120, 135, 150, 170, 200, 220]

sorted_indices = np.argsort(startups_founded)
years_sorted = years[sorted_indices]
startups_founded_sorted = np.array(startups_founded)[sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 6))  # Adjust the figure size for a single subplot

ax1.bar(years_sorted, startups_founded_sorted, color='blue')
ax1.set_xlim(2011, 2022)

plt.tight_layout(pad=3.0)

plt.show()