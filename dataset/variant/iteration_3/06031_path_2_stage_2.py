import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

pm25_concentration = np.array([34, 39, 36, 37, 41, 40, 44, 41, 39, 37, 36])
asthma_cases = np.array([122, 128, 124, 137, 138, 145, 162, 153, 148, 132, 127])

errors_pm25 = np.array([2 for _ in range(len(years))])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Randomly altered labels and title
ax1.errorbar(years, pm25_concentration, yerr=errors_pm25, label='Air Quality (µg/m³)', fmt='-o', capsize=5, color='tab:blue', alpha=0.8)
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Particles in Air (µg/m³)', fontsize=14, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.plot(years, asthma_cases, label='Respiratory Incidents (thousands)', linestyle='--', marker='s', color='tab:red', alpha=0.8)
ax2.set_ylabel('Health Cases (thousands)', fontsize=14, color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title("Pollution & Health Over Time (2010-2020)", fontsize=16, fontweight='bold', wrap=True)

ax1.grid(True, linestyle='--', alpha=0.7)

ax1.legend(loc='upper left', bbox_to_anchor=(0.01, 0.95), fontsize=12)
ax2.legend(loc='upper right', bbox_to_anchor=(0.99, 0.95), fontsize=12)

plt.tight_layout()

plt.show()