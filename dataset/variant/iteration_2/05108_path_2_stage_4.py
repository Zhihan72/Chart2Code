import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
consumption = np.array([
    [110, 130, 125, 170, 185, 215, 205, 255, 275, 295, 305],
    [85, 120, 90, 115, 135, 160, 180, 175, 215, 225, 255],
    [75, 85, 95, 95, 115, 130, 125, 145, 155, 165, 180],
    [55, 50, 75, 85, 85, 95, 105, 115, 135, 125, 155],
    [35, 30, 45, 50, 55, 60, 50, 70, 75, 70, 85]
])

# New color set
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF']

fig, ax = plt.subplots(figsize=(10, 7))

bar_width = 0.12
indices = np.arange(len(years))

for i, age_group in enumerate(age_groups):
    ax.bar(
        indices + i * bar_width,
        consumption[i],
        width=bar_width,
        color=new_colors[i],  # Applied new colors
        label=age_group
    )

ax.set_title('Coffee Consumption Trends in Coffeeburg (2010-2020)', fontsize=14, weight='bold')
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Coffee Cups (thousands)', fontsize=12)
ax.set_xticks(indices + bar_width * (len(age_groups) - 1) / 2)
ax.set_xticklabels(years)

ax.legend(loc='best', fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()