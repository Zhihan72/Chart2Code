import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the increase in Internet speeds across three cities over the past decade.
# Title: "Decade-long Evolution of Internet Speeds in Three Cities"
# Cities: Metropolis, Atlantis, Avalon
# Years: 2012-2022

years = np.arange(2012, 2023)

# Internet speeds (in Mbps) for Metropolis, Atlantis, and Avalon
metropolis_speeds = np.array([5, 7, 10, 14, 20, 25, 30, 40, 55, 70, 85])
atlantis_speeds = np.array([6, 8, 12, 17, 22, 28, 35, 45, 60, 75, 90])
avalon_speeds = np.array([4, 6, 9, 13, 18, 23, 29, 38, 50, 65, 80])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 7))

# Plot each city's internet speed
ax.plot(years, metropolis_speeds, color='blue', marker='o', linestyle='-', linewidth=2, label='Metropolis')
ax.plot(years, atlantis_speeds, color='green', marker='s', linestyle='--', linewidth=2, label='Atlantis')
ax.plot(years, avalon_speeds, color='red', marker='^', linestyle='-.', linewidth=2, label='Avalon')

# Annotating significant changes in speeds
ax.annotate('5G Introduction', xy=(2019, 40), xytext=(2016, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
ax.annotate('Fiber Optic Rollout', xy=(2021, 75), xytext=(2018, 80),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Highlighting the years when major improvements happened
ax.axvline(x=2019, color='purple', linestyle=':', linewidth=1)
ax.axvline(x=2021, color='purple', linestyle=':', linewidth=1)

# Adding title and labels
ax.set_title("Decade-long Evolution of Internet Speeds in Three Cities", fontsize=18, fontweight='bold', ha='center')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Internet Speed (Mbps)", fontsize=14)

# Customize x-ticks
ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years], rotation=45)

# Adding grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Cities', fontsize=12, title_fontsize=14, loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()