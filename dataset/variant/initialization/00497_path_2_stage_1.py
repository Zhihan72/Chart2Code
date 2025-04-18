import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

installations_state_a = np.array([10, 12, 14, 15, 17, 20, 23, 28, 35, 40, 45])
installations_state_c = np.array([5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40])

def calc_percentage_increase(data):
    return np.array([0] + [((data[i] - data[i-1]) / data[i-1]) * 100 for i in range(1, len(data))])

pct_increase_a = calc_percentage_increase(installations_state_a)
pct_increase_c = calc_percentage_increase(installations_state_c)

error_state_a = np.array([1.0, 1.5, 1.3, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.7, 3.0])
error_state_c = np.array([0.5, 0.7, 1.0, 1.1, 1.3, 1.5, 1.7, 1.9, 2.2, 2.5, 2.8])

fig, ax = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [2, 1]})

ax[0].errorbar(years, installations_state_a, yerr=error_state_a, label='State A', fmt='-o', capsize=5, color='blue', alpha=0.75)
ax[0].errorbar(years, installations_state_c, yerr=error_state_c, label='State C', fmt='-^', capsize=5, color='red', alpha=0.75)

ax[0].set_title("Solar Panel Installations (2010-2020):\nTracking Growth and Variability Across States", fontsize=14, weight='bold')
ax[0].set_xlabel("Year", fontsize=12)
ax[0].set_ylabel("Average Installations (in thousands)", fontsize=12)
ax[0].set_xticks(years)
ax[0].set_xlim(2009, 2021)
ax[0].set_ylim(0, 50)
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].legend(title="States", title_fontsize='13', fontsize='11', loc='upper left', frameon=True)

ax[0].annotate('Significant Increase', xy=(2018, 35), xytext=(2016, 40), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

ax[1].plot(years, pct_increase_a, '-o', label='State A Growth', color='blue', alpha=0.75)
ax[1].plot(years, pct_increase_c, '-^', label='State C Growth', color='red', alpha=0.75)

ax[1].set_title("Year-over-Year Percentage Growth", fontsize=12, pad=10)
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Percentage Increase (%)", fontsize=12)
ax[1].set_xticks(years)
ax[1].set_xlim(2009, 2021)
ax[1].grid(True, linestyle='--', alpha=0.6)
ax[1].legend(title="Growth Trends", title_fontsize='13', fontsize='11', loc='upper left', frameon=True)

plt.tight_layout()
plt.show()