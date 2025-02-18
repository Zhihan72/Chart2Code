import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

installations_state_a = np.array([10, 12, 14, 15, 17, 20, 23, 28, 35, 40, 45])
installations_state_b = np.array([8, 10, 12, 16, 21, 25, 30, 34, 39, 42, 44])
installations_state_c = np.array([5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40])

def calc_percentage_increase(data):
    return np.array([0] + [((data[i] - data[i-1]) / data[i-1]) * 100 for i in range(1, len(data))])

pct_increase_a = calc_percentage_increase(installations_state_a)
pct_increase_b = calc_percentage_increase(installations_state_b)
pct_increase_c = calc_percentage_increase(installations_state_c)

error_state_a = np.array([1.0, 1.5, 1.3, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.7, 3.0])
error_state_b = np.array([0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.1, 2.3, 2.6, 2.9, 3.1])
error_state_c = np.array([0.5, 0.7, 1.0, 1.1, 1.3, 1.5, 1.7, 1.9, 2.2, 2.5, 2.8])

fig, ax = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [2, 1]})

ax[0].errorbar(years, installations_state_a, yerr=error_state_a, label='State A', fmt='-x', capsize=3, color='navy', alpha=0.85)
ax[0].errorbar(years, installations_state_b, yerr=error_state_b, label='State B', fmt='--d', capsize=3, color='lime', alpha=0.85)
ax[0].errorbar(years, installations_state_c, yerr=error_state_c, label='State C', fmt='-.h', capsize=3, color='maroon', alpha=0.85)

ax[0].set_title("Solar Panel Installations (2010-2020)", fontsize=14, weight='bold')
ax[0].set_xlabel("Year", fontsize=12)
ax[0].set_ylabel("Installations (in thousands)", fontsize=12)
ax[0].set_xticks(years)
ax[0].set_xlim(2009, 2021)
ax[0].set_ylim(0, 50)
ax[0].grid(True, linestyle='-', linewidth=0.7, alpha=0.5)
ax[0].legend(title_fontsize='11', fontsize='9', loc='lower right', shadow=True, edgecolor='black')

ax[0].annotate('Note', xy=(2018, 35), xytext=(2016, 42),
               arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=9)

ax[1].plot(years, pct_increase_a, ':s', label='State A Growth', color='navy', alpha=0.85)
ax[1].plot(years, pct_increase_b, '--p', label='State B Growth', color='lime', alpha=0.85)
ax[1].plot(years, pct_increase_c, '-.*', label='State C Growth', color='maroon', alpha=0.85)

ax[1].set_title("Year-over-Year Percentage Growth", fontsize=12, pad=10)
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Percentage Increase (%)", fontsize=12)
ax[1].set_xticks(years)
ax[1].set_xlim(2009, 2021)
ax[1].grid(True, linestyle=':', linewidth=0.7, alpha=0.7)
ax[1].legend(title_fontsize='11', fontsize='9', loc='lower right', shadow=True, edgecolor='black')

plt.tight_layout()
plt.show()