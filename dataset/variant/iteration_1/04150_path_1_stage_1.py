import matplotlib.pyplot as plt
import numpy as np

cities = ['City A', 'City B', 'City C', 'City D']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

flu_cases_data = {
    'City A': [30, 25, 40, 35, 50, 60, 45, 55, 65, 70, 75, 80],
    'City B': [20, 18, 25, 28, 30, 35, 40, 45, 50, 55, 60, 65],
    'City C': [15, 10, 20, 25, 30, 35, 40, 45, 55, 60, 70, 75],
    'City D': [10, 5, 8, 12, 18, 20, 25, 30, 40, 50, 55, 60]
}

data_for_box = [flu_cases_data[city] for city in cities]

fig, ax = plt.subplots(figsize=(12, 7))

# Changed the colors for different properties
box = ax.boxplot(data_for_box, patch_artist=True, notch=True, vert=True,
                 boxprops=dict(facecolor='blue', color='black'),  # Changed color
                 whiskerprops=dict(color='red'),                  # Changed color
                 capprops=dict(color='blue'),                      # Changed color
                 medianprops=dict(color='#D3D3D3'),                # Changed color
                 flierprops=dict(markerfacecolor='black', marker='o', markersize=5, alpha=0.6))  # Changed color

ax.set_title('Seasonal Flu Cases Distribution\n Across Different Cities (2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Cities', fontsize=12)
ax.set_ylabel('Number of Flu Cases', fontsize=12)

ax.set_xticks(np.arange(1, len(cities) + 1))
ax.set_xticklabels(cities, fontsize=11)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

total_flu_cases_per_month = [sum(month) for month in zip(*data_for_box)]

ax2 = ax.twinx()
ax2.plot(months, total_flu_cases_per_month, color='red', marker='o', linestyle='-', linewidth=2, markersize=6, label='Total Flu Cases')  # Changed color
ax2.set_ylabel('Total Flu Cases', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

handles = [plt.Line2D([0], [0], color='#D3D3D3', lw=2, label='Median'),  # Changed color
           plt.Line2D([0], [0], marker='o', color='w', label='Outliers', 
                      markerfacecolor='black', markersize=6),  # Changed color
           plt.Line2D([0], [0], color='red', lw=2, label='Total Flu Cases')]  # Changed color
ax.legend(handles=handles, loc='upper left', fontsize=10)

plt.tight_layout()

plt.show()