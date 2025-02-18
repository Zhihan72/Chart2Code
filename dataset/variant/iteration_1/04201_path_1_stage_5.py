import matplotlib.pyplot as plt
import numpy as np

brightness_bins = ['0-2', '2-4', '4-6', '6-8', '8-10']
stars_jun = [20, 30, 55, 40, 25]
stars_dec = [25, 35, 45, 50, 30]
stars_sep = [30, 40, 60, 45, 35]
stars_mar = [15, 25, 50, 35, 20]

fig, axs = plt.subplots(1, 4, figsize=(18, 6), sharey=True)

axs[0].bar(brightness_bins, stars_jun, color='lightcoral')

axs[1].bar(brightness_bins, stars_dec, color='lightgreen')

axs[2].bar(brightness_bins, stars_sep, color='lightblue')

axs[3].bar(brightness_bins, stars_mar, color='lightyellow')

plt.tight_layout()

plt.show()