import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

installations_state_a = np.array([10, 12, 14, 15, 17, 20, 23, 28, 35, 40, 45])
installations_state_b = np.array([8, 10, 12, 16, 21, 25, 30, 34, 39, 42, 44])

def calc_percentage_increase(data):
    return np.array([0] + [((data[i] - data[i-1]) / data[i-1]) * 100 for i in range(1, len(data))])

pct_increase_a = calc_percentage_increase(installations_state_a)
pct_increase_b = calc_percentage_increase(installations_state_b)

sorted_indices_a = np.argsort(installations_state_a)
sorted_indices_b = np.argsort(installations_state_b)

sorted_years_a = years[sorted_indices_a]
sorted_years_b = years[sorted_indices_b]

sorted_installations_a = installations_state_a[sorted_indices_a]
sorted_installations_b = installations_state_b[sorted_indices_b]

sorted_pct_increase_a = pct_increase_a[sorted_indices_a]
sorted_pct_increase_b = pct_increase_b[sorted_indices_b]

fig, ax = plt.subplots(1, 2, figsize=(14, 5), gridspec_kw={'width_ratios': [3, 2]})

# Left subplot: Installations
ax[0].bar(sorted_years_a, sorted_installations_a, label='A', color='navy', alpha=0.85)
ax[0].bar(sorted_years_b, sorted_installations_b, label='B', color='lime', alpha=0.85)

ax[0].set_title("Solar Installations (2010-2020)", fontsize=14, weight='bold')
ax[0].set_xlabel("Year", fontsize=12)
ax[0].set_ylabel("Installs (k)", fontsize=12)
ax[0].set_xticks(years)
ax[0].set_xlim(2009, 2021)
ax[0].set_ylim(0, 50)
ax[0].grid(True, linestyle='-', linewidth=0.7, alpha=0.5)
ax[0].legend(title_fontsize='11', fontsize='9', loc='lower right', shadow=True, edgecolor='black')

# Right subplot: Yearly Growth
ax[1].bar(sorted_years_a, sorted_pct_increase_a, label='A Growth', color='navy', alpha=0.85)
ax[1].bar(sorted_years_b + 0.2, sorted_pct_increase_b, width=0.4, label='B Growth', color='lime', alpha=0.85)

ax[1].set_title("Yearly Growth", fontsize=12, pad=10)
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Increase (%)", fontsize=12)
ax[1].set_xticks(years)
ax[1].set_xlim(2009, 2021)
ax[1].grid(True, linestyle=':', linewidth=0.7, alpha=0.7)
ax[1].legend(title_fontsize='11', fontsize='9', loc='lower right', shadow=True, edgecolor='black')

plt.tight_layout()
plt.show()