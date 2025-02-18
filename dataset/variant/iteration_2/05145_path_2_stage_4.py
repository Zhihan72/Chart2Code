import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

fps_viewership = [2, 5, 8, 10, 13, 19, 35, 42, 50, 62, 75]
moba_viewership = [1, 3, 7, 14, 22, 30, 45, 55, 68, 80, 95]

fig, ax1 = plt.subplots(figsize=(14, 9))

single_color = 'blue'
ax1.plot(years, fps_viewership, color=single_color, linestyle='-', linewidth=2, marker='o')
ax1.plot(years, moba_viewership, color=single_color, linestyle='--', linewidth=2, marker='s')

highlight_years = [2013, 2015, 2018]
for year in highlight_years:
    ax1.axvline(x=year, color='black', linestyle='--', linewidth=1, alpha=0.8)

plt.tight_layout()
plt.show()