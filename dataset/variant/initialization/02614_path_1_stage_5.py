import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

asa_launches = [5, 6, 7, 10, 12, 15, 20, 18, 22, 24, 30, 35, 38, 40, 45, 50, 55, 58, 60, 65, 70]
asa_errors = [0.5, 0.6, 0.7, 0.8, 1, 1.2, 1.5, 1.7, 2, 2.2, 2.5, 2.7, 3, 3.1, 3.3, 3.5, 3.8, 4, 4.2, 4.5, 5]

cumulative_asa = np.cumsum(asa_launches)

# Sort the cumulative launches and corresponding years in ascending order
sorted_indices = np.argsort(cumulative_asa)
years_sorted = years[sorted_indices]
cumulative_asa_sorted = cumulative_asa[sorted_indices]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharex=False)

ax1.bar(years_sorted, cumulative_asa_sorted, width=0.6, label='ASA', color='g', alpha=0.7, edgecolor='black', hatch='/')

ax1.set_title('Cumulative Launches by Year (Sorted)', fontsize=14)
ax1.set_xlabel('Year')
ax1.set_ylabel('Cumulative Launches')
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(False)
ax1.set_xticks(years_sorted)
ax1.set_xticklabels(years_sorted, rotation=45, fontsize=8)

ax2.errorbar(years, asa_launches, yerr=asa_errors, label='ASA', fmt='s', color='b',
             capsize=6, linestyle='--', linewidth=1.5, alpha=0.9)

ax2.set_title('Annual Launch Frequencies with Errors', fontsize=14)
ax2.set_xlabel('Year')
ax2.set_ylabel('Launches')
ax2.legend(loc='lower right', fontsize=9)
ax2.grid(True, linestyle='-.', alpha=0.3)
ax2.axvline(x=2005, color='purple', linestyle='-.', linewidth=0.8, alpha=0.6)
ax2.annotate('Milestone', xy=(2005, 60), xytext=(2005, 67),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=8, ha='center')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, fontsize=8)
ax2.set_yticks(np.arange(0, 80, 10))
ax2.set_yticklabels(np.arange(0, 80, 10), fontsize=8)

plt.tight_layout()
plt.show()