import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

# Randomly altered internet speeds for Metropolis, Atlantis, and Avalon
metropolis_speeds = np.array([7, 5, 14, 10, 25, 20, 30, 55, 40, 85, 70])
atlantis_speeds = np.array([8, 6, 17, 12, 28, 22, 35, 60, 45, 90, 75])
avalon_speeds = np.array([6, 4, 13, 9, 20, 18, 29, 50, 38, 80, 65])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(years, metropolis_speeds, color='blue', marker='o', linestyle='-', linewidth=2, label='Metropolis')
ax.plot(years, atlantis_speeds, color='green', marker='s', linestyle='--', linewidth=2, label='Atlantis')
ax.plot(years, avalon_speeds, color='red', marker='^', linestyle='-.', linewidth=2, label='Avalon')

ax.annotate('5G Introduction', xy=(2019, 40), xytext=(2016, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
ax.annotate('Fiber Optic Rollout', xy=(2021, 75), xytext=(2018, 80),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

ax.axvline(x=2019, color='purple', linestyle=':', linewidth=1)
ax.axvline(x=2021, color='purple', linestyle=':', linewidth=1)

ax.set_title("Decade-long Evolution of Internet Speeds in Three Cities", fontsize=18, fontweight='bold', ha='center')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Internet Speed (Mbps)", fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years], rotation=45)

ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Cities', fontsize=12, title_fontsize=14, loc='upper left')

plt.tight_layout()
plt.show()