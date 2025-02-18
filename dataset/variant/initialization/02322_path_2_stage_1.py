import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

years = np.arange(2010, 2021)

north_america = np.array([15, 16, 18, 19, 21, 23, 24, 26, 28, 30, 32])
europe = np.array([20, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38])
asia = np.array([10, 11, 13, 14, 16, 18, 20, 22, 25, 27, 30])
latin_america = np.array([8, 9, 10, 12, 14, 16, 18, 20, 23, 25, 28])

percent_change_na = np.diff(north_america) / north_america[:-1] * 100
percent_change_eu = np.diff(europe) / europe[:-1] * 100
percent_change_asia = np.diff(asia) / asia[:-1] * 100
percent_change_la = np.diff(latin_america) / latin_america[:-1] * 100

fig, axs = plt.subplots(2, 1, figsize=(14, 10))

axs[0].plot(years, north_america, label='North America', marker='x', color='#3498db', linestyle='--', linewidth=3)
axs[0].plot(years, europe, label='Europe', marker='v', color='#e74c3c', linestyle='-', linewidth=1)
axs[0].plot(years, asia, label='Asia', marker='d', color='#2ecc71', linestyle=':', linewidth=2)
axs[0].plot(years, latin_america, label='Latin America', marker='p', color='#f1c40f', linestyle='-.', linewidth=1.5)

for region, color, data in zip(
    ['North America', 'Europe', 'Asia', 'Latin America'],
    ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f'],
    [north_america, europe, asia, latin_america]
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

axs[1].plot(years[1:], percent_change_na, label='North America % Change', marker='<', color='#3498db', linestyle='--', linewidth=2)
axs[1].plot(years[1:], percent_change_eu, label='Europe % Change', marker='>', color='#e74c3c', linestyle='-', linewidth=2)
axs[1].plot(years[1:], percent_change_asia, label='Asia % Change', marker='h', color='#2ecc71', linestyle=':', linewidth=2)
axs[1].plot(years[1:], percent_change_la, label='Latin America % Change', marker='H', color='#f1c40f', linestyle='-.', linewidth=2)

axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Year over Year % Change", fontsize=12)
axs[1].legend(loc='lower right', fontsize=9, edgecolor='black')
axs[1].grid(True, linestyle='-', linewidth=0.8, alpha=0.6)
axs[1].xaxis.set_major_locator(MaxNLocator(integer=True))

plt.tight_layout()
plt.show()