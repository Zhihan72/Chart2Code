import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

swimmer_assist = np.array([50, 45, 60, 55, 65])
minor_injuries = np.array([20, 25, 15, 18, 22])
major_injuries = np.array([5, 4, 6, 7, 6])
rough_seas = np.array([15, 13, 18, 20, 17])
crowd_control = np.array([10, 9, 14, 13, 11])

rescue_data = np.vstack([swimmer_assist, minor_injuries, major_injuries, rough_seas, crowd_control])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, rescue_data, colors=['#1E90FF', '#32CD32', '#FFA500', '#B22222', '#9370DB'], alpha=0.75)

highlight_years = [2020]
for year in highlight_years:
    ax.axvline(x=year, color='black', linestyle='--', linewidth=1)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

for y, color in zip(rescue_data, ['#1E90FF', '#32CD32', '#FFA500', '#B22222', '#9370DB']):
    ax.plot(years, y, marker='o', markersize=6, color=color, linestyle='None', alpha=0.9)

plt.show()