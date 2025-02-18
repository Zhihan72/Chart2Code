import matplotlib.pyplot as plt
import numpy as np

# Data: Years and corresponding values for internet users and bandwidth usage
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
internet_users = np.array([2.7, 2.9, 3.2, 3.5, 3.8, 4.2, 4.5, 4.8, 5.1, 5.3])  # in billions
bandwidth_usage = np.array([6, 8, 11, 15, 20, 26, 34, 45, 60, 75])  # in exabytes per month

# Plotting the data on line chart
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot internet users
ax1.plot(years, internet_users, marker='o', linestyle='-', linewidth=2, color='green', label='Internet Users (Billions)')
for i, txt in enumerate(internet_users):
    ax1.annotate(f'{txt}B', (years[i], internet_users[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

# Twin axis for bandwidth usage
ax2 = ax1.twinx()
ax2.plot(years, bandwidth_usage, marker='s', linestyle='-', linewidth=2, color='blue', label='Bandwidth Usage (Exabytes/Month)')
for i, txt in enumerate(bandwidth_usage):
    ax2.annotate(f'{txt}EB', (years[i], bandwidth_usage[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

# Setting titles and labels
plt.title("Digital Evolution:\nA Decade of Internet Growth and Bandwidth Consumption", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Internet Users (Billions)", fontsize=14, color='green')
ax2.set_ylabel("Bandwidth Usage (Exabytes/Month)", fontsize=14, color='blue')

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Grids for readability
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Ticks for both axes
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 6.5, 0.5))
ax2.set_yticks(np.arange(0, 85, 10))

# Layout adjustments
plt.tight_layout()

# Show plot
plt.show()