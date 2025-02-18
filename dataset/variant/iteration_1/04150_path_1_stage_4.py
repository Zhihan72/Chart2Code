import matplotlib.pyplot as plt
import numpy as np

cities = ['A', 'B', 'C', 'D', 'E', 'F']

flu_cases_data = {
    'City A': [30, 25, 40, 35, 50, 60, 45, 55, 65, 70, 75, 80],
    'City B': [20, 18, 25, 28, 30, 35, 40, 45, 50, 55, 60, 65],
    'City C': [15, 10, 20, 25, 30, 35, 40, 45, 55, 60, 70, 75],
    'City D': [10, 5, 8, 12, 18, 20, 25, 30, 40, 50, 55, 60],
    'City E': [40, 35, 55, 50, 60, 65, 70, 75, 85, 90, 95, 100],
    'City F': [25, 22, 30, 28, 35, 40, 50, 60, 70, 80, 85, 90]
}

data_for_box = [
    flu_cases_data['City A'], 
    flu_cases_data['City B'], 
    flu_cases_data['City C'], 
    flu_cases_data['City D'], 
    flu_cases_data['City E'], 
    flu_cases_data['City F']
]

fig, ax = plt.subplots(figsize=(14, 8))

# Change here from vertical to horizontal by setting vert=False
box = ax.boxplot(data_for_box, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='blue', color='black'),
                 whiskerprops=dict(color='red'),
                 capprops=dict(color='blue'),
                 medianprops=dict(color='#D3D3D3'),
                 flierprops=dict(markerfacecolor='black', marker='o', markersize=5, alpha=0.6))

ax.set_title('2023 Flu Cases', fontsize=16, fontweight='bold')
ax.set_ylabel('City', fontsize=12)
ax.set_xlabel('Cases', fontsize=12)

ax.set_yticks(np.arange(1, len(cities) + 1))
ax.set_yticklabels(cities, fontsize=11)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()