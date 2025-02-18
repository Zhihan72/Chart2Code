import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
# Manually shuffled avg_screen_sizes while keeping the same dimensions
avg_screen_sizes = np.array([4.0, 3.7, 4.7, 5.5, 3.5, 6.4, 5.2, 6.1, 5.7, 4.5, 5.0])
# Manually modified notable models details, preserving structure
notable_models = {"Samsung S8": (2012, 5.8), "iPhone 4": (2017, 3.5), 
                  "iPhone 6": (2014, 4.7), "Samsung S3": (2010, 4.8), 
                  "iPhone 11": (2019, 6.1)}

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, avg_screen_sizes, color='green', marker='s', linestyle='--', linewidth=3)

for model, (year, size) in notable_models.items():
    ax.plot(year, size, color='blue', marker='D')

ax.set_xticks(years)
ax.set_yticks(np.arange(3.0, 7.0, 0.5))

ax.grid(True, linestyle='-', alpha=0.9)

plt.tight_layout()

plt.show()