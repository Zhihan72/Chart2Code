import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

metropolis_speeds = np.array([5, 7, 10, 14, 20, 25, 30, 40, 55, 70, 85])
atlantis_speeds = np.array([6, 8, 12, 17, 22, 28, 35, 45, 60, 75, 90])
avalon_speeds = np.array([4, 6, 9, 13, 18, 23, 29, 38, 50, 65, 80])

fig, ax = plt.subplots(figsize=(14, 7))

# Changed colors for each city's internet speed plot
ax.plot(years, metropolis_speeds, color='orange', marker='o', linestyle='-', linewidth=2, label='Metropolis')
ax.plot(years, atlantis_speeds, color='cyan', marker='s', linestyle='--', linewidth=2, label='Atlantis')
ax.plot(years, avalon_speeds, color='magenta', marker='^', linestyle='-.', linewidth=2, label='Avalon')

ax.annotate('5G Introduction', xy=(2019, 40), xytext=(2016, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
ax.annotate('Fiber Optic Rollout', xy=(2021, 75), xytext=(2018, 80),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Updated line colors for major improvements
ax.axvline(x=2019, color='brown', linestyle=':', linewidth=1)
ax.axvline(x=2021, color='brown', linestyle=':', linewidth=1)

ax.set_title("Decade-long Evolution of Internet Speeds in Three Cities", fontsize=18, fontweight='bold', ha='center')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Internet Speed (Mbps)", fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years], rotation=45)

ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Cities', fontsize=12, title_fontsize=14, loc='upper left')

plt.tight_layout()
plt.show()