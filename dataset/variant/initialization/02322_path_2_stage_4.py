import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

years = np.arange(2010, 2021)

north_america = np.array([15, 16, 18, 19, 21, 23, 24, 26, 28, 30, 32])
europe = np.array([20, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38])
latin_america = np.array([8, 9, 10, 12, 14, 16, 18, 20, 23, 25, 28])

percent_change_na = np.diff(north_america) / north_america[:-1] * 100
percent_change_eu = np.diff(europe) / europe[:-1] * 100
percent_change_la = np.diff(latin_america) / latin_america[:-1] * 100

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

colors = ['#8e44ad', '#27ae60', '#2980b9']

axs[0].plot(years, north_america, label='North America', marker='x', color=colors[0], linestyle='--', linewidth=3)
axs[0].plot(years, europe, label='Europe', marker='v', color=colors[1], linestyle='-', linewidth=1)
axs[0].plot(years, latin_america, label='Latin America', marker='p', color=colors[2], linestyle='-.', linewidth=1.5)

for region, color, data in zip(
    ['North America', 'Europe', 'Latin America'],
    colors,
    [north_america, europe, latin_america]
):
    turning_point_index = np.argmax(np.diff(data))
    axs[0].annotate(f"{data[turning_point_index + 1]}M",
                    (years[turning_point_index + 1], data[turning_point_index + 1]),
                    textcoords="offset points", xytext=(10,-10), ha='right', color=color)

axs[0].set_title("Evolution of Global Adventure Tourism (2010-2020)", fontsize=14, fontweight='bold')
axs[0].set_ylabel("Number of Adventure Tourists (Millions)", fontsize=12)
axs[0].legend(loc='center', fontsize=9, edgecolor='black')
axs[0].grid(True, linestyle='-', linewidth=0.8, alpha=0.6)
axs[0].xaxis.set_major_locator(MaxNLocator(integer=True))

axs[1].plot(years[1:], percent_change_na, label='North America % Change', marker='<', color=colors[0], linestyle='--', linewidth=2)
axs[1].plot(years[1:], percent_change_eu, label='Europe % Change', marker='>', color=colors[1], linestyle='-', linewidth=2)
axs[1].plot(years[1:], percent_change_la, label='Latin America % Change', marker='H', color=colors[2], linestyle='-.', linewidth=2)

axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Year over Year % Change", fontsize=12)
axs[1].legend(loc='lower right', fontsize=9, edgecolor='black')
axs[1].grid(True, linestyle='-', linewidth=0.8, alpha=0.6)
axs[1].xaxis.set_major_locator(MaxNLocator(integer=True))

plt.tight_layout()
plt.show()