import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

years = np.arange(2010, 2021)

north_america = np.array([15, 16, 18, 19, 21, 23, 24, 26, 28, 30, 32])
europe = np.array([20, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38])
asia = np.array([10, 11, 13, 14, 16, 18, 20, 22, 25, 27, 30])
latin_america = np.array([8, 9, 10, 12, 14, 16, 18, 20, 23, 25, 28])
oceania = np.array([5, 6, 7, 8, 9, 11, 13, 15, 17, 20, 22])

percent_change_na = np.diff(north_america) / north_america[:-1] * 100
percent_change_eu = np.diff(europe) / europe[:-1] * 100
percent_change_asia = np.diff(asia) / asia[:-1] * 100
percent_change_la = np.diff(latin_america) / latin_america[:-1] * 100
percent_change_oceania = np.diff(oceania) / oceania[:-1] * 100

# Consistent color for simplicity
consistent_color = '#3498db'

# Shuffle the textual elements within the provided listing
titles = [
    "Global Trends in Adventure Tourism",
    "Number of Adventure Tourists Change (%)",
    "Y-o-Y % Growth in Tourism",
    "(Million) Tourists Across Regions",
    "Trends from the Past Decade"
]

axis_labels = [
    "Time (Year)", 
    "Million Tourists", 
    "Yearly Change (%)", 
    "YoY Growth", 
    "Tourist Count (Million)"
]

group_labels = ['N. America', 'EU', 'Asia', 'LatAm', 'Oceania']

fig, axs = plt.subplots(2, 1, figsize=(14, 10))

# Randomly shuffle titles, labels, group for demonstration
axs[0].plot(years[1:], percent_change_na, marker='o', color=consistent_color, linestyle='-', linewidth=2)
axs[0].plot(years[1:], percent_change_eu, marker='s', color=consistent_color, linestyle='--', linewidth=2)
axs[0].plot(years[1:], percent_change_asia, marker='^', color=consistent_color, linestyle='-.', linewidth=2)
axs[0].plot(years[1:], percent_change_la, marker='d', color=consistent_color, linestyle=':', linewidth=2)
axs[0].plot(years[1:], percent_change_oceania, marker='x', color=consistent_color, linestyle='-', linewidth=2)

axs[0].set_xlabel(axis_labels[0], fontsize=12)
axs[0].set_ylabel(axis_labels[2], fontsize=12)
axs[0].xaxis.set_major_locator(MaxNLocator(integer=True))

axs[1].plot(years, north_america, marker='o', color=consistent_color, linestyle='-', linewidth=2, label=group_labels[0])
axs[1].plot(years, europe, marker='s', color=consistent_color, linestyle='--', linewidth=2, label=group_labels[1])
axs[1].plot(years, asia, marker='^', color=consistent_color, linestyle='-.', linewidth=2, label=group_labels[2])
axs[1].plot(years, latin_america, marker='d', color=consistent_color, linestyle=':', linewidth=2, label=group_labels[3])
axs[1].plot(years, oceania, marker='x', color=consistent_color, linestyle='-', linewidth=2, label=group_labels[4])

for region, data in zip(
    group_labels, 
    [north_america, europe, asia, latin_america, oceania]
):
    turning_point_index = np.argmax(np.diff(data))
    axs[1].annotate(f"{data[turning_point_index + 1]}M",
                    (years[turning_point_index + 1], data[turning_point_index + 1]),
                    textcoords="offset points", xytext=(-15,10), ha='center', color=consistent_color)

axs[1].set_title(titles[1], fontsize=14, fontweight='bold')
axs[1].set_ylabel(axis_labels[1], fontsize=12)
axs[1].xaxis.set_major_locator(MaxNLocator(integer=True))
axs[1].legend()

plt.tight_layout()
plt.show()