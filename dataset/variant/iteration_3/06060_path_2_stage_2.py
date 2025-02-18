import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

metropolis_speeds = np.array([5, 7, 10, 14, 20, 25, 30, 40, 55, 70, 85])
atlantis_speeds = np.array([6, 8, 12, 17, 22, 28, 35, 45, 60, 75, 90])
avalon_speeds = np.array([4, 6, 9, 13, 18, 23, 29, 38, 50, 65, 80])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(years, metropolis_speeds, color='orange', marker='o', linestyle='-', linewidth=2)
ax.plot(years, atlantis_speeds, color='cyan', marker='s', linestyle='--', linewidth=2)
ax.plot(years, avalon_speeds, color='magenta', marker='^', linestyle='-.', linewidth=2)

# Remove annotations from the plot
# Removed the annotation code here

ax.axvline(x=2019, color='brown', linestyle=':', linewidth=1)
ax.axvline(x=2021, color='brown', linestyle=':', linewidth=1)

# Removed axis labels and title
# ax.set_title("Decade-long Evolution of Internet Speeds in Three Cities", fontsize=18, fontweight='bold', ha='center')
# ax.set_xlabel("Year", fontsize=14)
# ax.set_ylabel("Internet Speed (Mbps)", fontsize=14)

# Removed group labels and legend
# ax.legend(title='Cities', fontsize=12, title_fontsize=14, loc='upper left')

ax.set_xticks(years)
ax.set_xticklabels([''] * len(years))  # Remove text from x-tick labels

ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()