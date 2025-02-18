import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

pm25_concentration = np.array([34, 39, 36, 37, 41, 40, 44, 41, 39, 37, 36])
asthma_cases = np.array([122, 128, 124, 137, 138, 145, 162, 153, 148, 132, 127])

errors_pm25 = np.array([2 for _ in range(len(years))])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.errorbar(years, pm25_concentration, yerr=errors_pm25, label='Air Quality (µg/m³)', fmt=':^', capsize=7, color='tab:purple', alpha=0.9)
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Particles in Air (µg/m³)', fontsize=14, color='tab:purple')
ax1.tick_params(axis='y', labelcolor='tab:purple')

ax2 = ax1.twinx()
ax2.plot(years, asthma_cases, label='Respiratory Incidents (thousands)', linestyle='-.', marker='x', color='tab:orange', alpha=0.9)
ax2.set_ylabel('Health Cases (thousands)', fontsize=14, color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title("Pollution & Health Over Time (2010-2020)", fontsize=16, fontweight='bold', wrap=True)

ax1.grid(True, linestyle=':', alpha=0.6)

ax1.legend(loc='upper right', bbox_to_anchor=(0.01, 0.95), fontsize=11)
ax2.legend(loc='lower right', bbox_to_anchor=(0.99, 0.05), fontsize=11)

plt.tight_layout()

plt.show()