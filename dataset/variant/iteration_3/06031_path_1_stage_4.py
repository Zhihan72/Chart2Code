import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
pm25_concentration = np.array([35, 38, 37, 36, 39, 41, 43, 42, 40, 38, 35])
asthma_cases = np.array([120, 130, 125, 135, 140, 150, 160, 155, 145, 135, 125])
respiratory_visits = np.array([80, 85, 82, 88, 90, 95, 100, 98, 92, 89, 86])
errors_pm25 = np.array([2 for _ in range(len(years))])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.errorbar(years, pm25_concentration, yerr=errors_pm25, fmt='-o', capsize=5, color='seagreen', alpha=0.8)
ax1.tick_params(axis='y', labelcolor='seagreen')

ax2 = ax1.twinx()
ax2.plot(years, asthma_cases, linestyle='--', marker='s', color='royalblue', alpha=0.8)
ax2.tick_params(axis='y', labelcolor='royalblue')

ax2.plot(years, respiratory_visits, linestyle='-.', marker='^', color='darkorange', alpha=0.8)

plt.tight_layout()
plt.show()