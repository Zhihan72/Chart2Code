import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

atlantic_temp = np.array([15.1, 15.3, 15.5, 15.6, 15.7, 15.9, 16.0, 16.1, 16.3, 16.4, 16.5])
pacific_temp = np.array([16.1, 16.2, 16.4, 16.5, 16.7, 16.8, 17.0, 17.1, 17.3, 17.4, 17.6])
indian_temp = np.array([24.1, 24.2, 24.3, 24.5, 24.6, 24.8, 24.9, 25.0, 25.2, 25.3, 25.5])

atlantic_err = np.array([0.2] * len(years))
pacific_err = np.array([0.3] * len(years))
indian_err = np.array([0.15] * len(years))

atlantic_inc = atlantic_temp[-1] - atlantic_temp[0]
pacific_inc = pacific_temp[-1] - pacific_temp[0]
indian_inc = indian_temp[-1] - indian_temp[0]

increases = [atlantic_inc, pacific_inc, indian_inc]
oceans = ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean']

sorted_increases, sorted_oceans = zip(*sorted(zip(increases, oceans), key=lambda x: x[0]))

colors = ['teal', 'maroon', 'purple']

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

ax1 = axes[0]
ax1.errorbar(years, atlantic_temp, yerr=atlantic_err, fmt='-o', color=colors[0], capsize=4)
ax1.errorbar(years, pacific_temp, yerr=pacific_err, fmt='-s', color=colors[1], capsize=4)
ax1.errorbar(years, indian_temp, yerr=indian_err, fmt='-^', color=colors[2], capsize=4)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')

# Remove borders from axes
for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in axes[1].spines.values():
    spine.set_visible(False)

ax2 = axes[1]
ax2.bar(sorted_oceans, sorted_increases, color=colors)

plt.tight_layout()
plt.show()