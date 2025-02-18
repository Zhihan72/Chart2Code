import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
age_groups = ['26-35', '60+', '18-25', '46-60', '36-45']  # Altered group labels
consumption = np.array([
    [110, 130, 125, 170, 185, 215, 205, 255, 275, 295, 305],
    [85, 120, 90, 115, 135, 160, 180, 175, 215, 225, 255],
    [75, 85, 95, 95, 115, 130, 125, 145, 155, 165, 180],
    [55, 50, 75, 85, 85, 95, 105, 115, 135, 125, 155],
    [35, 30, 45, 50, 55, 60, 50, 70, 75, 70, 85]
])

# New color set
new_colors = ['#33FF57', '#A633FF', '#FF5733', '#FF33A6', '#3357FF']  # Aligned with new group order

fig, ax = plt.subplots(figsize=(10, 7))

bar_width = 0.12
indices = np.arange(len(years))

for i, age_group in enumerate(age_groups):
    ax.bar(
        indices + i * bar_width,
        consumption[i],
        width=bar_width,
        color=new_colors[i],
        label=age_group
    )

ax.set_title('Exploring Coffee Cup Mania in Coffeeburg (2010-2020)', fontsize=14, weight='bold')  # Altered title
ax.set_xlabel('Calendar Years', fontsize=12)  # Altered x-axis label
ax.set_ylabel('Cups Consumed (in thousands)', fontsize=12)  # Altered y-axis label
ax.set_xticks(indices + bar_width * (len(age_groups) - 1) / 2)
ax.set_xticklabels(years)

ax.legend(loc='best', fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()