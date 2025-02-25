import matplotlib.pyplot as plt
import numpy as np

# Updated city list without 'Desert Hues'
cities = ['Oceanview', 'Mountain Peak', 'Sunnyvale', 'Lake Town']

# Updated rainfall data without 'Desert Hues' data
rainfall_data = np.array([
    [85, 78, 92, 110, 125, 140, 155, 145, 130, 115, 100, 90],
    [95, 88, 102, 120, 135, 150, 165, 155, 140, 125, 110, 100],
    [45, 40, 52, 60, 75, 80, 85, 75, 65, 55, 50, 45],
    [75, 68, 82, 90, 105, 120, 135, 125, 110, 95, 80, 70],
])

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Horizontal bar chart setup
bar_height = 0.15
y = np.arange(len(months))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for i, city in enumerate(cities):
    bars = axs[0].barh(y + i * bar_height, rainfall_data[i], bar_height, label=city, color=colors[i])
    for bar in bars:
        axs[0].annotate(f'{bar.get_width()}',
                        xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
                        xytext=(5, 0), textcoords='offset points',
                        ha='left', va='center', fontsize=9)

axs[0].set_ylabel('Months', fontsize=12)
axs[0].set_xlabel('Average Monthly Rainfall (mm)', fontsize=12)
axs[0].set_title('Rainfall Land: Monthly Rainfall by City (2023)', fontsize=14, fontweight='bold')
axs[0].set_yticks(y + bar_height * (len(cities) / 2 - 0.5))
axs[0].set_yticklabels(months, fontsize=10)
axs[0].legend(title='City', fontsize=9, loc='upper right', frameon=False)
axs[0].xaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)

marker_styles = ['o', 'p', 'H', '^']

# Line chart setup
for i, city in enumerate(cities):
    axs[1].plot(months, rainfall_data[i], marker=marker_styles[i], linestyle='--', color=colors[i], label=city)

axs[1].set_xlabel('Months', fontsize=12)
axs[1].set_ylabel('Average Monthly Rainfall (mm)', fontsize=12)
axs[1].set_title('Yearly Rainfall Trend by City (2023)', fontsize=14, fontweight='bold')
axs[1].legend(title='City', fontsize=9, loc='upper right', frameon=True, shadow=True)
axs[1].yaxis.grid(True, linestyle=':', linewidth=0.8, alpha=0.9)

plt.tight_layout()
plt.show()