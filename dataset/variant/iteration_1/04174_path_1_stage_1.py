import matplotlib.pyplot as plt
import numpy as np

# Age groups (in years) and their average daily step count
age_groups = np.array([10, 20, 30, 40, 50, 60, 70, 80])
average_steps = np.array([12000, 15500, 14500, 13000, 11000, 9000, 7000, 4000])

# Monthly steps data for selected age groups
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
steps_per_month = np.array([
    [11000, 16000, 15000, 14000, 11000, 10000, 8000, 5000, 6000, 7000, 7500, 8000], # Age 10
    [12000, 17000, 15500, 14500, 12000, 10500, 9000, 6000, 6500, 7500, 8000, 8500], # Age 20
    [12500, 16500, 14800, 13800, 11500, 9500, 8500, 5500, 6200, 7000, 7600, 8200],  # Age 30
    [11500, 15000, 14000, 13000, 10800, 9000, 7500, 5000, 5700, 6600, 7200, 7700]   # Age 40
])

fig, ax = plt.subplots(2, 1, figsize=(12, 12))

# Line plot
ax[0].plot(age_groups, average_steps, 'o-', color='blue', linestyle='-', linewidth=2, markersize=8, 
           markerfacecolor='red', markeredgewidth=2, markeredgecolor='darkred', label='Avg Steps')
ax[0].set_title("Avg Daily Steps by Age", fontsize=16, fontweight='bold', pad=20)
ax[0].set_xlabel("Age", fontsize=12)
ax[0].set_ylabel("Avg Steps", fontsize=12)

for i in range(age_groups.size):
    ax[0].annotate(f'{average_steps[i]:,.0f}', xy=(age_groups[i], average_steps[i]), xytext=(-10, 10), 
                   textcoords='offset points', fontsize=10, color='black', bbox=dict(facecolor='yellow', edgecolor='none', pad=2))

ax[0].grid(True, which='both', linestyle='--', alpha=0.6)
ax[0].tick_params(axis='both', which='major', labelsize=10)
ax[0].legend(loc='upper right', fontsize=10, frameon=True)

# Bar chart
age_group_indices = [0, 1, 2, 3]
bar_width = 0.2
for idx, age_idx in enumerate(age_group_indices):
    ax[1].bar(np.arange(len(months)) + idx * bar_width, steps_per_month[age_idx], width=bar_width, label=f'Age {age_groups[age_idx]}')

ax[1].set_xticks(np.arange(len(months)) + bar_width * 1.5)
ax[1].set_xticklabels(months)
ax[1].set_xlabel("Month", fontsize=12)
ax[1].set_ylabel("Avg Steps", fontsize=12)
ax[1].set_title("Monthly Steps by Age", fontsize=16, fontweight='bold', pad=20)
ax[1].legend(loc='upper right', fontsize=10, frameon=True)

plt.tight_layout()
plt.show()