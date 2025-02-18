import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

asa_launches = [5, 6, 7, 10, 12, 15, 20, 18, 22, 24, 30, 35, 38, 40, 45, 50, 55, 58, 60, 65, 70]
cve_launches = [3, 4, 5, 6, 8, 11, 15, 14, 16, 20, 25, 30, 33, 35, 38, 45, 48, 50, 55, 60, 68]

asa_errors = [0.5, 0.6, 0.7, 0.8, 1, 1.2, 1.5, 1.7, 2, 2.2, 2.5, 2.7, 3, 3.1, 3.3, 3.5, 3.8, 4, 4.2, 4.5, 5]
cve_errors = [0.4, 0.5, 0.5, 0.6, 0.8, 1, 1.3, 1.5, 1.7, 2, 2.3, 2.5, 2.8, 3, 3.2, 3.4, 3.6, 3.9, 4.1, 4.3, 4.6]

cumulative_asa = np.cumsum(asa_launches)
cumulative_cve = np.cumsum(cve_launches)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# First subplot alterations
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

# Second subplot alterations
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