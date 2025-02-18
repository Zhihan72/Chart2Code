import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array([10, 20, 30, 40, 50, 60, 70, 80])
average_steps = np.array([12000, 15500, 14500, 13000, 11000, 9000, 7000, 4000])

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
steps_per_month = np.array([
    [11000, 16000, 15000, 14000, 11000, 10000, 8000, 5000, 6000, 7000, 7500, 8000],
    [12000, 17000, 15500, 14500, 12000, 10500, 9000, 6000, 6500, 7500, 8000, 8500],
    [12500, 16500, 14800, 13800, 11500, 9500, 8500, 5500, 6200, 7000, 7600, 8200],
    [11500, 15000, 14000, 13000, 10800, 9000, 7500, 5000, 5700, 6600, 7200, 7700]
])

fig, ax = plt.subplots(2, 1, figsize=(12, 12))

# Line plot with altered styles
ax[0].plot(age_groups, average_steps, 's--', color='green', linestyle='--', linewidth=2.5, markersize=10, 
           markerfacecolor='yellow', markeredgewidth=1.5, markeredgecolor='darkgreen', label='Average Steps')
ax[0].set_title("Average Daily Steps by Age", fontsize=18, fontweight='bold', pad=15)
ax[0].set_xlabel("Age", fontsize=14)
ax[0].set_ylabel("Average Steps", fontsize=14)

for i in range(age_groups.size):
    ax[0].annotate(f'{average_steps[i]:,.0f}', xy=(age_groups[i], average_steps[i]), xytext=(-15, 5),
                   textcoords='offset points', fontsize=9, color='purple', bbox=dict(facecolor='lightblue', edgecolor='purple', pad=2))

ax[0].grid(False)
ax[0].tick_params(axis='both', which='major', labelsize=12)
ax[0].legend(loc='lower left', fontsize=12, frameon=False)

# Bar chart with altered styles
age_group_indices = [0, 1, 2, 3]
bar_width = 0.15
colors = ['c', 'm', 'y', 'k']
for idx, age_idx in enumerate(age_group_indices):
    ax[1].bar(np.arange(len(months)) + idx * bar_width, steps_per_month[age_idx], width=bar_width, color=colors[idx], label=f'Age {age_groups[age_idx]}')

ax[1].set_xticks(np.arange(len(months)) + bar_width * 1.5)
ax[1].set_xticklabels(months)
ax[1].set_xlabel("Month", fontsize=14)
ax[1].set_ylabel("Average Steps", fontsize=14)
ax[1].set_title("Monthly Steps by Age Group", fontsize=18, fontweight='bold', pad=10)
ax[1].legend(loc='upper left', fontsize=11, frameon=False)

plt.tight_layout()
plt.show()