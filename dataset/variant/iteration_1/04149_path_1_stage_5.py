import matplotlib.pyplot as plt
import numpy as np

quarters = ['Alpha', 'Beta', 'Gamma', 'Delta']  # Randomly altered quarter labels
agriculture_gdp = [5.5, 6.0, 6.8, 7.2]
manufacturing_gdp = [4.4, 4.9, 5.5, 6.1]
services_gdp = [6.2, 6.7, 7.1, 7.5]

cumulative_gdp = np.cumsum([sum(x) for x in zip(agriculture_gdp, manufacturing_gdp, services_gdp)])

fig, ax1 = plt.subplots(figsize=(14, 7))
height = 0.2
y_indices = np.arange(len(quarters))
single_color = 'tab:gray'

ax1.barh(y_indices - height, agriculture_gdp, height=height, color=single_color)
ax1.barh(y_indices, manufacturing_gdp, height=height, color=single_color)
ax1.barh(y_indices + height, services_gdp, height=height, color=single_color)

ax1.set_title('Quarterly Analysis of Planet Z: 2023 Edition', fontsize=16, fontweight='bold', pad=20)  # Randomly altered title
ax1.set_ylabel('Segment', fontsize=12)  # Randomly altered y-axis label
ax1.set_xlabel('Economic Output (in billions)', fontsize=12)  # Randomly altered x-axis label
ax1.set_yticks(y_indices)
ax1.set_yticklabels(quarters)

ax2 = ax1.twiny()
ax2.plot(cumulative_gdp, y_indices, color='black', marker='o', linestyle='-', linewidth=2)

for i, val in enumerate(cumulative_gdp):
    ax2.text(val, i, f'{val:.1f}', color='black', fontsize=10, va='center', ha='left')

plt.tight_layout()
plt.show()