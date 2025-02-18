import matplotlib.pyplot as plt
import numpy as np

cities = ['Oceanview', 'Mountain Peak', 'Sunnyvale', 'Lake Town', 'Desert Hues']

rainfall_data = [
    [85, 78, 92, 110, 125, 140, 155, 145, 130, 115, 100, 90],
    [95, 88, 102, 120, 135, 150, 165, 155, 140, 125, 110, 100],
    [45, 40, 52, 60, 75, 80, 85, 75, 65, 55, 50, 45],
    [75, 68, 82, 90, 105, 120, 135, 125, 110, 95, 80, 70],
    [15, 10, 22, 30, 35, 40, 45, 35, 25, 20, 15, 10],
]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall_data = np.array(rainfall_data)

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

bar_width = 0.15
x = np.arange(len(months))

single_color = '#1f77b4'

for i, city in enumerate(cities):
    bars = axs[0].bar(x + i * bar_width, rainfall_data[i], bar_width, label=city, color=single_color)
    for bar in bars:
        axs[0].annotate(f'{bar.get_height()}',
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 3), textcoords='offset points',
                        ha='center', va='bottom', fontsize=9)

axs[0].set_xlabel('Months', fontsize=12)
axs[0].set_ylabel('Average Monthly Rainfall (mm)', fontsize=12)
axs[0].set_title('Rainfall Land: Average Monthly Rainfall by City (2023)', fontsize=14, fontweight='bold')
axs[0].set_xticks(x + bar_width * (len(cities) / 2 - 0.5))
axs[0].set_xticklabels(months, fontsize=10)
axs[0].legend(title='City', fontsize=10)
axs[0].yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

markers = ['o', 's', 'D', '^', 'v']

for i, city in enumerate(cities):
    axs[1].plot(months, rainfall_data[i], marker=markers[i], color=single_color, label=city)

axs[1].set_xlabel('Months', fontsize=12)
axs[1].set_ylabel('Average Monthly Rainfall (mm)', fontsize=12)
axs[1].set_title('Yearly Rainfall Trend by City (2023)', fontsize=14, fontweight='bold')
axs[1].legend(title='City', fontsize=10)
axs[1].yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()