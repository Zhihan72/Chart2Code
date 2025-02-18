import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2000, 2021)

# Satellite launches per year for AetherSpace Agency (ASA)
asa_launches = [5, 6, 7, 10, 12, 15, 20, 18, 22, 24, 30, 35, 38, 40, 45, 50, 55, 58, 60, 65, 70]
asa_errors = [0.5, 0.6, 0.7, 0.8, 1, 1.2, 1.5, 1.7, 2, 2.2, 2.5, 2.7, 3, 3.1, 3.3, 3.5, 3.8, 4, 4.2, 4.5, 5]

# Calculate cumulative launches for AetherSpace Agency (ASA)
cumulative_asa = np.cumsum(asa_launches)

# Plot setup with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharex=True)

# Bar chart for cumulative launches
ax1.bar(years, cumulative_asa, width=0.4, label='AetherSpace Agency (ASA)', color='r', alpha=0.6)

# Add title, labels, and grid for the first subplot
ax1.set_title('Cumulative Satellite Launches by Year', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Cumulative Launches', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Line chart with error bars
ax2.errorbar(years, asa_launches, yerr=asa_errors, label='AetherSpace Agency (ASA)', fmt='-o',
             color='r', capsize=4, linestyle='-', linewidth=2, alpha=0.8)

# Add title, labels, and grid for the second subplot
ax2.set_title('Annual Satellite Launch Frequencies\nwith Technology Error Margins (2000-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Satellite Launches', fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.axvline(x=2005, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
ax2.axvline(x=2015, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
ax2.annotate('Tech Milestone', xy=(2005, 60), xytext=(2005, 65),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')
ax2.annotate('Tech Milestone', xy=(2015, 60), xytext=(2015, 65),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.set_yticks(np.arange(0, 80, 5))

# Adjust layout for clarity
plt.tight_layout()

# Show the plot
plt.show()