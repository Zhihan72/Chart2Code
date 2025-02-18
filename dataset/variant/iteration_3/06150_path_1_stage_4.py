import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2024)
bandwidth = [5, 8, 12, 18, 28, 40, 55, 70, 85, 100, 120, 150, 170, 200]

# Remove one or more data points for the corresponding years.
# Let's say we are removing data for the years 2016 and 2017
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2018, 2019, 2020, 2021, 2022, 2023])
bandwidth = [5, 8, 12, 18, 28, 40, 70, 85, 100, 120, 150, 170]

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(years, bandwidth, color='darkgreen', marker='s', linestyle='--', linewidth=3, markersize=10)

ax.set_xticks(years)
ax.set_xlim(2009, 2023)
ax.set_ylim(0, 220)
ax.yaxis.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()