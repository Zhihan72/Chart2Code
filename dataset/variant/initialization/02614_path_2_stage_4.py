import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Shuffled data for ASA and CVE launches
asa_launches = [12, 45, 58, 15, 38, 8, 22, 60, 65, 10, 55, 24, 35, 50, 18, 70, 40, 7, 6, 30, 5]
cve_launches = [20, 14, 48, 68, 3, 5, 25, 30, 16, 60, 4, 33, 45, 38, 6, 8, 11, 4, 55, 35, 50]

# Shuffled error margins for ASA and CVE launches
asa_errors = [2.2, 3, 3.5, 2.7, 0.5, 3.8, 0.6, 1, 1.2, 3.1, 4.2, 5, 3.3, 0.7, 4, 3.3, 4.5, 1.7, 3.5, 0.8, 2.5]
cve_errors = [4.6, 0.5, 2.3, 3.6, 5, 1, 2.5, 3.2, 1.3, 3.4, 2, 0.4, 0.6, 0.5, 4.1, 1.7, 3, 1.5, 1.8, 2.8, 3.9]

# Update cumulative sums based on shuffled launch data
cumulative_asa = np.cumsum(asa_launches)
cumulative_cve = np.cumsum(cve_launches)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

ax1.barh(years - 0.2, asa_launches, xerr=asa_errors, label='AetherSpace Agency (ASA)', color='g', alpha=0.8, capsize=5)
ax1.barh(years + 0.2, cve_launches, xerr=cve_errors, label='CosmicVoyage Enterprises (CVE)', color='b', alpha=0.8, capsize=5)
ax1.set_title('Annual Satellite Launch Frequencies\nwith Technology Error Margins (2000-2020)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Year', fontsize=12)
ax1.set_xlabel('Satellite Launches', fontsize=12)
ax1.legend(title='Space Agencies', loc='lower right', fontsize=10)
ax1.grid(True, linestyle='-', linewidth='0.7', alpha=0.3)
ax1.axhline(y=2005, color='gray', linestyle='-.', linewidth=1.2, alpha=0.6)
ax1.axhline(y=2015, color='gray', linestyle='-.', linewidth=1.2, alpha=0.6)
ax1.annotate('Tech Milestone', xy=(60, 2005), xytext=(65, 2005),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, va='center')
ax1.annotate('Tech Milestone', xy=(60, 2015), xytext=(65, 2015),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, va='center')
ax1.set_yticks(years)
ax1.set_yticklabels(years)

ax2.barh(years - 0.2, cumulative_asa, height=0.4, label='AetherSpace Agency (ASA)', color='m', alpha=0.8)
ax2.barh(years + 0.2, cumulative_cve, height=0.4, label='CosmicVoyage Enterprises (CVE)', color='y', alpha=0.8)
ax2.set_title('Cumulative Satellite Launches by Year', fontsize=14, fontweight='bold')
ax2.set_ylabel('Year', fontsize=12)
ax2.set_xlabel('Cumulative Launches', fontsize=12)
ax2.legend(title='Space Agencies', loc='lower right', fontsize=10)
ax2.grid(True, linestyle=':', linewidth='0.7', alpha=0.5)
ax2.set_yticks(years)
ax2.set_yticklabels(years)

plt.tight_layout()
plt.show()