import matplotlib.pyplot as plt
import numpy as np

years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
internet_users = np.array([2.7, 2.9, 3.2, 3.5, 3.8, 4.2, 4.5, 4.8, 5.1, 5.3])
bandwidth_usage = np.array([6, 8, 11, 15, 20, 26, 34, 45, 60, 75])

fig, ax1 = plt.subplots(figsize=(10, 6))

# Changed the color of the first plot line
ax1.plot(years, internet_users, marker='o', linestyle='-', linewidth=2, color='darkorange')
for i, txt in enumerate(internet_users):
    ax1.annotate(f'{txt}B', (years[i], internet_users[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

ax2 = ax1.twinx()
# Changed the color of the second plot line
ax2.plot(years, bandwidth_usage, marker='s', linestyle='-', linewidth=2, color='purple')
for i, txt in enumerate(bandwidth_usage):
    ax2.annotate(f'{txt}EB', (years[i], bandwidth_usage[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.title("Web Revolution:\nInternet User Surge & Data Boom", fontsize=16, fontweight='bold')
ax1.set_xlabel("Calendar Year", fontsize=14)

# Updated colors in ylabel to match the new line colors
ax1.set_ylabel("Web Users (Billions)", fontsize=14, color='darkorange')
ax2.set_ylabel("Data Usage (Exabytes)", fontsize=14, color='purple')

ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 6.5, 0.5))
ax2.set_yticks(np.arange(0, 85, 10))

plt.tight_layout()
plt.show()