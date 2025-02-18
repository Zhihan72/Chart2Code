import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])

screen_time_data = {
    '12-13 years': np.array([3.4, 3.2, 4.2, 4.0, 4.5]),  # Swapped data within the group
    '14-15 years': np.array([4.3, 3.7, 3.5, 4.8, 4.5]),  # Swapped data within the group
    '16-17 years': np.array([4.7, 5.2, 4.0, 4.2, 4.9])   # Swapped data within the group
}

error_margins = {
    '12-13 years': np.array([0.3, 0.3, 0.4, 0.4, 0.5]), 
    '14-15 years': np.array([0.3, 0.3, 0.4, 0.4, 0.5]),
    '16-17 years': np.array([0.3, 0.3, 0.4, 0.4, 0.5])
}

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.25
positions = np.arange(len(years))

colors = ['#ff9999', '#99ff99', '#66b3ff']
markers = ['x', 'o', 's']
line_styles = ['-', '--', '-.']

for i, (age_group, data) in enumerate(screen_time_data.items()):
    ax.bar(positions + i * bar_width, data, bar_width,
           label=age_group, yerr=error_margins[age_group], capsize=5, color=colors[i], alpha=0.7)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Screen Time (Hours per Day)', fontsize=12)
ax.set_title('Average Daily Screen Time of Teenagers (2018-2022)', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width)
ax.set_xticklabels(years)
ax.legend(title='Age Group', loc='best', fancybox=True, shadow=True, frameon=False)

ax.grid(True, which='major', linestyle=line_styles[0], linewidth=0.75, alpha=0.6)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()

plt.show()